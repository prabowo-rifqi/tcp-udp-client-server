import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f"[TCP Server] Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"[TCP Server] Received from {addr}: {message}")
            conn.sendall(b"[TCP Server] Pesan diterima")

            # Simpan ke log file
            with open("log_tcp.txt", "a") as log_file:
                log_file.write(f"{addr} - {message}\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[TCP Server] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()