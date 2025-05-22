import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[UDP Server] Listening on {HOST}:{PORT}")
    
    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode()
        print(f"[UDP Server] Received from {addr}: {message}")

        # Simpan ke log file
        with open("log_udp.txt", "a") as log_file:
            log_file.write(f"{addr} - {message}\n")