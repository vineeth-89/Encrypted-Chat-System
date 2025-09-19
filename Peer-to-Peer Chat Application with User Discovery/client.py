import socket
import threading
import sys


def receive_messages(sock):
    try:
        while True:
            message = sock.recv(1024).decode()
            if message == "EOM":
                print("\nConnection closed by peer.\n Please Enter any key to get menu")
                return ""
            print(f"\n[Received]: {message}\n[Send]: ", end="", flush=True) # Print the received message and enable send function

            sys.stdout.flush()  # Ensure immediate display
    except Exception as e:
        print(f"[ERROR] Error receiving message: {e}")
    finally:
        sock.close()
        return ""

def send_messages(sock):
    try:
        while True:
            message = input("[Send]: ")
            sock.send(message.encode())
            sys.stdout.flush()  # Flush output for immediate display
            if message == "EOM":
                break
    except Exception as e:
        print(f"[ERROR] Error sending message: {e}")
    finally:
        sock.send("EOM".encode())  # Ensure both sides close connection
        sock.close()
        print("Connection closed.")
        return ""


def p2p_chat(peer_ip, peer_port):
    """Initiates peer-to-peer chat."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((peer_ip, peer_port))
        print("Connected. Type 'EOM' to exit.")

        # Start receiving messages in a separate thread
        recv_thread = threading.Thread(target=receive_messages, args=(sock,))
        recv_thread.start()
        send_messages(sock)
    except Exception as e:
        print("Connection rejected.\n Please Enter any key to get menu")
        return ""
    finally:
        sock.close()
        return ""
def act_as_listener(listen_port):
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
            
            # Start receiving messages in a separate thread
            recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
            recv_thread.start()

            send_messages(client_socket)
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
            act_as_listener(listen_port)

        elif choice == "3":
            target_ip = input("Enter peer IP: ")
            target_port = int(input("Enter peer port: "))
            p2p_chat(target_ip, target_port)

        elif choice == "4":
            sock.send(b"EXIT")
            print("Exiting...")
            break

    sock.close()

if __name__ == "__main__":
    start_client()
