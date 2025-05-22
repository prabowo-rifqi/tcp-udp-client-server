import tkinter as tk
from tkinter import messagebox
import socket

# Konfigurasi server
TCP_HOST = UDP_HOST = '127.0.0.1'
TCP_PORT = 65432
UDP_PORT = 65433

# Fungsi Kirim Pesan
def send_message():
    protocol = protocol_var.get()
    message = message_entry.get()

    if not message:
        messagebox.showwarning("Peringatan", "Pesan tidak boleh kosong.")
        return

    if protocol == "TCP":
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((TCP_HOST, TCP_PORT))
                s.sendall(message.encode())
                data = s.recv(1024)
                result_label.config(text=f"Respon TCP: {data.decode()}")
        except Exception as e:
            messagebox.showerror("Error TCP", str(e))

    elif protocol == "UDP":
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.sendto(message.encode(), (UDP_HOST, UDP_PORT))
                result_label.config(text=f"Pesan UDP dikirim.")
        except Exception as e:
            messagebox.showerror("Error UDP", str(e))

    else:
        messagebox.showerror("Error", "Protokol tidak dikenali.")

# UI
root = tk.Tk()
root.title("TCP/UDP Client")
root.geometry("400x250")

# Protokol Dropdown
protocol_var = tk.StringVar(value="TCP")
protocol_label = tk.Label(root, text="Pilih Protokol:")
protocol_label.pack(pady=(10, 0))
protocol_menu = tk.OptionMenu(root, protocol_var, "TCP", "UDP")
protocol_menu.pack()

# Input pesan
message_label = tk.Label(root, text="Pesan:")
message_label.pack(pady=(10, 0))
message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

# Tombol kirim
send_button = tk.Button(root, text="Kirim", command=send_message)
send_button.pack(pady=10)

# Hasil respon
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

# Jalankan aplikasi
root.mainloop()