import tkinter as tk
from tkinter import messagebox
import subprocess
import tkinter.simpledialog

def FireWall(root):

    def firewall():
        current_text = button.cget("text")
        if current_text == "Enable":
            button.config(text="Disable")
            # Call the function for enabling
            enable_firewall()
        elif current_text == "Disable":
            button.config(text="Enable")
            # Call the function for disabling
            disable_firewall()

    def enable_firewall():
        # subprocess.run(['sudo', 'ufw', 'enable'])
        # status_label.config(text="Firewall Enabled")
        password = tkinter.simpledialog.askstring("Password", "Enter your password:", show='*')
        if password:
            # Run the command with sudo and password
            sudo_command = f'echo {password} | sudo -S ufw enable'
            subprocess.run(sudo_command, shell=True)
            status_label.config(text="Firewall Enabled")
            show_current_rules()
        # show_current_rules()

    def disable_firewall():
        subprocess.run(['sudo', 'ufw', 'disable'])
        status_label.config(text="Firewall Disabled")
        show_current_rules()

    def apply_configurations():
        deny_ports = deny_port_entry.get().split(',')
        allow_ports = allow_port_entry.get().split(',')
        allow_ips = allow_ip_entry.get().split(',')
        deny_ips = deny_ip_entry.get().split(',')
        
        for port in deny_ports:
            if port.strip():
                subprocess.run(['sudo', 'ufw', 'deny', port.strip()])
        for port in allow_ports:
            if port.strip():
                subprocess.run(['sudo', 'ufw', 'allow', port.strip()])
        for ip in allow_ips:
            if ip.strip():
                subprocess.run(['sudo', 'ufw', 'allow', 'from', ip.strip()])
        for ip in deny_ips:
            if ip.strip():
                subprocess.run(['sudo', 'ufw', 'deny', 'from', ip.strip()])
        
        messagebox.showinfo("Configuration Applied", "Configuration applied successfully!")
        clear_fields()
        show_current_rules()

    def clear_fields():
        deny_port_entry.delete(0, tk.END)
        allow_port_entry.delete(0, tk.END)
        allow_ip_entry.delete(0, tk.END)
        deny_ip_entry.delete(0, tk.END)

    def allow_ssh():
        subprocess.run(['sudo', 'ufw', 'allow', 'ssh'])
        messagebox.showinfo("Rule Applied", "SSH allowed successfully!")
        show_current_rules()

    def delete_ssh():
        subprocess.run(['sudo', 'ufw', 'delete', 'allow', 'ssh'])
        messagebox.showinfo("Rule Deleted", "SSH rule deleted successfully!")
        show_current_rules()

    def reset_firewall():
        # subprocess.run(['sudo', 'ufw', 'reset'])
        # messagebox.showinfo("Firewall Reset", "Firewall reset successfully!")
        process = subprocess.Popen('sudo ufw reset', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response = messagebox.askyesno("Confirmation", "Resetting all rules to installed defaults. Proceed with operation?")
        if response:
            process.stdin.write(b"y\n")  # Respond 'y' to confirmation prompt
            process.stdin.flush()
        else:
            process.stdin.write(b"n\n")  # Respond 'n' to confirmation prompt
            process.stdin.flush()
            
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            button.config(text="Enable")
            messagebox.showinfo("Reset Successfull", f"Configuration are reset to default!")
        else:
            messagebox.showerror("Operation Failed", f"Command failed with error:\n{stderr.decode()}")
        show_current_rules()

    def show_current_rules():
        print('dfbehdf')
        result = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
        current_rules_text.config(state=tk.NORMAL)
        current_rules_text.delete("1.0", tk.END)
        current_rules_text.insert(tk.END, result.stdout)
        current_rules_text.config(state=tk.DISABLED)


    root_bg_color = root.cget("bg")  # Get the background color of the root window

    heading_label = tk.Label(root, text="FireWall", font=("Arial", 20), bg=root_bg_color)  # Set background color to root background color
    heading_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # Create a spacer label to push the button to the right
    spacer_label = tk.Label(root, text="", bg=root_bg_color)  # Set background color to root background color
    spacer_label.grid(row=0, column=1, sticky="we")  # Column weight is set to expand the spacer

    # Button at the extreme right side
    button = tk.Button(root, text="Enable", command=firewall)
    button.grid(row=0, column=2, sticky="e", padx=10, pady=10)

    # Text label with smaller font
    text_label = tk.Label(root, text="Control network ports and firewall rules with ufw. Allow/Deny specific ports protocols and enable/disable ssh. Configure manage and ensure network security through the firewall configuration.", font=("Arial", 12), wraplength=550, justify="left", bg=root_bg_color)  # Set background color to root background color
    text_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=10, pady=5)

    # Column weight to expand the spacer
    root.grid_columnconfigure(1, weight=1)

    # Firewall Status
    status_label = tk.Label(root, text="Firewall Status: ", bg=root_bg_color)  # Set background color to root background color
    status_label.grid(row=2, column=0, sticky="W", padx=10, pady=5)

    # Configuration Fields
    deny_port_label = tk.Label(root, text="Deny Ports (comma separated):", bg=root_bg_color)  # Set background color to root background color
    deny_port_label.grid(row=3, column=0, sticky="W", padx=10, pady=5)
    deny_port_entry = tk.Entry(root)
    deny_port_entry.grid(row=3, column=1, padx=10, pady=5)

    allow_port_label = tk.Label(root, text="Allow Ports (comma separated):", bg=root_bg_color)  # Set background color to root background color
    allow_port_label.grid(row=4, column=0, sticky="W", padx=10, pady=5)
    allow_port_entry = tk.Entry(root)
    allow_port_entry.grid(row=4, column=1, padx=10, pady=5)

    deny_ip_label = tk.Label(root, text="Deny IP Addresses (comma separated):", bg=root_bg_color)  # Set background color to root background color
    deny_ip_label.grid(row=5, column=0, sticky="W", padx=10, pady=5)
    deny_ip_entry = tk.Entry(root)
    deny_ip_entry.grid(row=5, column=1, padx=10, pady=5)

    allow_ip_label = tk.Label(root, text="Allow IP Addresses (comma separated):", bg=root_bg_color)  # Set background color to root background color
    allow_ip_label.grid(row=6, column=0, sticky="W", padx=10, pady=5)
    allow_ip_entry = tk.Entry(root)
    allow_ip_entry.grid(row=6, column=1, padx=10, pady=5)

    apply_button = tk.Button(root, text="Apply Configurations", command=apply_configurations)
    apply_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    # Additional Rules
    allow_ssh_button = tk.Button(root, text="Allow SSH", command=allow_ssh)
    allow_ssh_button.grid(row=8, column=0, padx=10, pady=5)

    delete_ssh_button = tk.Button(root, text="Delete Allow SSH", command=delete_ssh)
    delete_ssh_button.grid(row=8, column=1, padx=10, pady=5)

    reset_button = tk.Button(root, text="Reset Firewall", command=reset_firewall)
    reset_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    # Display Current Rules
    current_rules_label = tk.Label(root, text="Current Rules:", bg=root_bg_color)  # Set background color to root background color
    current_rules_label.grid(row=10, column=0, sticky="W", padx=10, pady=5)

    current_rules_text = tk.Text(root, height=10, width=50)
    current_rules_text.grid(row=11, column=0, columnspan=2, padx=10, pady=5)
    current_rules_text.config(state=tk.DISABLED)

    show_current_rules()

    # root.mainloop()
