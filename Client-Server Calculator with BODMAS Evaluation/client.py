import socket

def start_client():
    # Connect to the server
    server_ip = input("Enter Server IP: ")
    server_port = int(input("Enter Server Port Number: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    print("Enter expression (or 'END' to quit):")
    while True:
        # Read user input
        expression = input("[INPUT]  ")

        if expression.strip().lower() == "end":
            sock.send(expression.encode())
            print("Exiting...")
            break
        
        # Send the expression to the server
        sock.send(expression.encode())
        
        # Receive the result from the server
        result = sock.recv(1024).decode()
        print("[OUTPUT]",result)
    
    sock.close()

if __name__ == "__main__":
    start_client()
