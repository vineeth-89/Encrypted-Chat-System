import socket
import threading

connected_users = {}  # {username: (connection, IP, listen_port)}

def broadcast_user_list():
    """Broadcast the updated user list to all connected clients."""
    user_list = "\n".join([f"{user} - {ip}:{listen_port}" for user, (conn, ip, listen_port) in connected_users.items()])
    for conn, _, _ in connected_users.values():
        conn.send(user_list.encode() if user_list else b"No users connected.")

def handle_client(conn, addr):
    username = None
    try:
        data = conn.recv(1024).decode().split(":")
        if len(data) != 2:
            conn.close()
            return
        
        username, listen_port = data[0], int(data[1])
        connected_users[username] = (conn, addr[0], listen_port)
        print(f"[SERVER] {username} registered from {addr[0]}:{listen_port}")
        broadcast_user_list()  # Notify all clients of the new user

        while True:
            request = conn.recv(1024).decode()
            if request == "LIST":
                user_list = "\n".join([f"{user} - {ip}:{listen_port}" for user, (conn, ip, listen_port) in connected_users.items()])
                conn.send(user_list.encode() if user_list else b"No users connected.")
            elif request == "EXIT":
                break

    except Exception as e:
        print(f"[ERROR] {username} encountered an error: {e}")
    finally:
        if username in connected_users:
            del connected_users[username]
        conn.close()
        broadcast_user_list()  # Broadcast updated list after disconnect
        print(f"[SERVER] {username} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 11001))
    server.listen(5)
    print("[SERVER] Running on port 11001...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
