import subprocess
import tkinter as tk
import os
import shutil


def SSHHardening(root):

    def backup_ssh_config():
        backup_file = "/etc/ssh/sshd_config.bak"
        if not os.path.exists(backup_file):
            subprocess.run(['sudo', 'cp', '/etc/ssh/sshd_config', backup_file])

    def update_ssh_config(option):
        sshd_config_path = "/etc/ssh/sshd_config"
        if option == 1:
            subprocess.run(['sudo', 'sed', '-i', 's/#PasswordAuthentication yes/PasswordAuthentication no/', sshd_config_path])
        elif option == 2:
            subprocess.run(['sudo', 'sed', '-i', 's/#PermitEmptyPasswords no/PermitEmptyPasswords no/', sshd_config_path])
        elif option == 3:
            subprocess.run(['sudo', 'sed', '-i', 's/#PermitUserEnvironment no/PermitUserEnvironment no/', sshd_config_path])
        elif option == 4:
            subprocess.run(['sudo', 'sed', '-i', 's/X11Forwarding yes/X11Forwarding no/', sshd_config_path])
        elif option == 5:
            subprocess.run(['sudo', 'sed', '-i', 's/#AllowTcpForwarding yes/AllowTcpForwarding no/', sshd_config_path])
        elif option == 6:
            new_port = new_port_entry.get().strip()
            subprocess.run(['sudo', 'sed', '-i', f's/#Port 22/Port {new_port}/', sshd_config_path])
            subprocess.run(['sudo', 'ufw', 'allow', 'in', new_port])
            subprocess.run(['sudo', 'ufw', 'allow', 'out', new_port])
        else:
            print("Invalid option.")

    def restore_original_config():
        backup_file = "/etc/ssh/sshd_config.bak"
        if os.path.exists(backup_file):
            subprocess.run(['sudo', 'cp', backup_file, '/etc/ssh/sshd_config'])
            restart_ssh_service()
            print("Original SSH configuration restored.")
        else:
            print("Backup file not found. Unable to restore original configuration.")

    def restart_ssh_service():
        if shutil.which("systemctl"):
            subprocess.run(['sudo', 'systemctl', 'restart', 'ssh'])
        elif shutil.which("service"):
            subprocess.run(['sudo', 'service', 'ssh', 'restart'])
        else:
            print("Unable to restart SSH service. Please restart it manually.")

    def on_option_selected():
        selected_option = int(option_var.get())
        if selected_option == 6:
            new_port_entry.config(state=tk.NORMAL)
        else:
            new_port_entry.config(state=tk.DISABLED)

    # root = tk.Tk()
    # root.title("SSH Hardening")
    # root.geometry("400x400")
    
    root_bg_color = root.cget("bg") 

    heading_label = tk.Label(root, text="SSH Hardening", font=("Arial", 16),bg=root_bg_color)
    heading_label.pack(pady=10)

    desc_label = tk.Label(root, text="Secure your SSH configuration by applying the following hardening measures:",bg=root_bg_color)
    desc_label.pack(pady=5)

    option_var = tk.StringVar()

    options_frame = tk.Frame(root,bg=root_bg_color)
    options_frame.pack(pady=10)

    options = [
        "Disable Password Authentication: Disables password-based login and requires the use of SSH keys.",
        "Disable Empty Passwords: Prohibits users from logging in with empty passwords.",
        "Disable User Environment: Prevents users from setting environment variables through SSH.",
        "Disable X11 Forwarding: Disables X11 forwarding, which is used for remote graphical applications.",
        "Disable TCP Forwarding: Disables TCP forwarding, which can be used for port forwarding.",
        "Change SSH Port: Allows you to change the default SSH port for added security."
    ]

    for i, option in enumerate(options, start=1):
        radio = tk.Radiobutton(options_frame, text=option, variable=option_var, value=i, command=on_option_selected,bg=root_bg_color)
        radio.grid(row=i, column=0, sticky="w", padx=10, pady=5)

    new_port_entry = tk.Entry(root, state=tk.DISABLED)
    new_port_entry.pack(pady=5)

    button_frame = tk.Frame(root,bg=root_bg_color)
    button_frame.pack(pady=10)

    apply_button = tk.Button(button_frame, text="Apply Hardening", command=lambda: update_ssh_config(int(option_var.get())))
    apply_button.grid(row=0, column=0, padx=5)

    restore_button = tk.Button(button_frame, text="Restore Original Config", command=restore_original_config)
    restore_button.grid(row=0, column=1, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)
    exit_button.grid(row=0, column=2, padx=5)

    # root.mainloop()
