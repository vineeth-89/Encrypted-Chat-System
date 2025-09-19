import socket
import threading
import sys
import os
import random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
import base64

p = int(os.getenv('P', 23))  # prime modulus
q = int(os.getenv('Q', 5))   # base 

# Each party chooses a private key 
private_key = random.randint(1, p-1)

# Compute public key
public_key = pow(q, private_key, p)

def key_exchanges(rec_socket, sender_username):
    """Performs Diffie-Hellman key exchange before chat starts."""
    rec_socket.send(str(public_key).encode())
    peer_public_key = int(rec_socket.recv(1024).decode())
    #  shared secret key
    shared_secret_key = pow(peer_public_key, private_key, p)
    
    # Derive AES key from shared secret using scrypt
    aes_key = scrypt(shared_secret_key.to_bytes((shared_secret_key.bit_length() + 7) // 8, 'big'), b'salt', 32, N=2**14, r=8, p=1)
    
    # Print usernames dynamically during key exchange
    print(f"[{sender_username}] Private Key (a): {private_key}")
    print(f"[{sender_username}] Public Key (A): {public_key}")
    print(f"[{sender_username}] [SECURITY] Shared Secret Key Computed: {shared_secret_key}")
    return aes_key

def encrypt_message(aes_key, message):
    """Encrypt the message using AES."""
    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    
    # Return ciphertext and nonce (for later decryption)
    return cipher.nonce + tag + ciphertext

def decrypt_message(aes_key, encrypted_message):
    """Decrypt the message using AES."""
    nonce = encrypted_message[:16]
    tag = encrypted_message[16:32]
    ciphertext = encrypted_message[32:]

    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
    
    return decrypted_message.decode()

def receive_messages(sock, aes_key):
    try:
        while True:
            encrypted_message = sock.recv(1024)
            if encrypted_message == b"EOM":
                print("\nConnection closed by peer.\n Please Enter any key to get menu")
                break
            
            print(f"\n[Received][Cipher]: {base64.b64encode(encrypted_message).decode()}")
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"[Plain]: {decrypted_message}\n[Send]: ", end="", flush=True)  # Print received message
            sys.stdout.flush()  # Ensure immediate display
    except Exception as e:
        print(f"[ERROR] Error receiving message: {e}")
    finally:
        sock.close()
        print("Connection terminated.")
        return ""

def send_messages(sock, aes_key):
    try:
        while True:
            message = input("[Send]: ")
            encrypted_message = encrypt_message(aes_key, message)
            sock.send(encrypted_message)
            sys.stdout.flush()  # Flush output for immediate display
            
            print(f"[Cipher]: {base64.b64encode(encrypted_message).decode()}")
            if message == "EOM":
                break
    except Exception as e:
        print(f"[ERROR] Error sending message: {e}")
    finally:
        sock.send("EOM".encode())  # Ensure both sides close connection
        sock.close()
        print("Connection closed.\n Please Enter any key to get menu")
        return ""

def p2p_chat(peer_ip, peer_port, sender_username):
    """Initiates peer-to-peer chat."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((peer_ip, peer_port))
        print("Connected. Type 'EOM' to exit.")
        aes_key = key_exchanges(sock, sender_username)

        # Start receiving messages in a separate thread
        recv_thread = threading.Thread(target=receive_messages, args=(sock, aes_key))
        recv_thread.start()

        send_messages(sock, aes_key)
    except Exception as e:
        print("Connection rejected.\n Please Enter any key to get menu")
        return ""
    finally:
        sock.close()
        return ""
def act_as_listener(listen_port, sender_username):
    """Handles incoming connection and listens for messages."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", listen_port))
    server_socket.listen(1)
    print(f"Waiting for connections on port {listen_port}...")

    try:
        client_socket, addr = server_socket.accept()
        print(f"Connection request received from {addr}")
        
        # Ask if the user wants to accept or reject the connection
        accept_connection = input("Do you want to accept the connection? (yes/no): ").strip().lower()
        
        if accept_connection == 'yes':
            print("Connection established.")
            aes_key = key_exchanges(client_socket, sender_username)

            # Start receiving messages in a separate thread
            recv_thread = threading.Thread(target=receive_messages, args=(client_socket, aes_key))
            recv_thread.start()

            send_messages(client_socket, aes_key)
        else:
            client_socket.send("EOM".encode())
            print("Connection rejected.")
            client_socket.close()
    except Exception as e:
        print(f"Listener error: {e}", prefix="[ERROR]")
    finally:
        server_socket.close()


def start_client():
    server_ip = input("Enter server IP: ")
    server_port=int(input("Enter Server Port Number: "))

    username = input("Enter your username: ")
    listen_port = int(input("Enter your listening port: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    sock.send(f"{username}:{listen_port}".encode())

    while True:
        print("\n1. List users\n2. Act as Listener\n3. Connect to User\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            sock.send(b"LIST")
            print("Fetching list of connected users...")
            print(sock.recv(1024).decode())

        elif choice == "2":
            act_as_listener(listen_port, username)

        elif choice == "3":
            target_ip = input("Enter peer IP: ")
            target_port = int(input("Enter peer port: "))
            p2p_chat(target_ip, target_port, username)

        elif choice == "4":
            sock.send(b"EXIT")
            print("Exiting...")
            break

    sock.close()

if __name__ == "__main__":
    start_client()
