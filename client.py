import socket
import threading

HOST = '127.0.0.1'  # Server IP address
PORT = 12345        # Must match the server port

# This function constantly listens for incoming messages from the server
def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(f"[SERVER]: {msg}")
        except:
            break
# This function sends messages to the server from user input
def send_messages(sock):
    while True:
        msg = input()
        if msg.lower() == 'exit':
            sock.close()
            break
        sock.sendall(msg.encode())

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print("[CONNECTED] Connected to the server.")
    except ConnectionRefusedError:
        print("[ERROR] Could not connect to server. Is it running?")
        return

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    # Main thread handles sending messages
    send_messages(client)

if __name__ == "__main__":
    main()
  