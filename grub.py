import subprocess
import tkinter as tk
from tkinter import messagebox

def set_grub_password():
    # Check if the script is run as root
    if not is_root():
        messagebox.showerror("Error", "Please run this script as root or using sudo.")
        return
    
    # Check if GRUB_PASSWORD already exists in the GRUB configuration file
    grub_cfg = "/etc/default/grub"
    # if grep_grub_password(grub_cfg):
    #     messagebox.showinfo("Info", "GRUB password is already set. Exiting.")
    #     return
    
    # Prompt user for the GRUB password
    grub_password = password_entry.get()
    
    grub_password_hash = subprocess.run(
        ["grub-mkpasswd-pbkdf2"],
        input=f"{grub_password}\n{grub_password}\n",
        capture_output=True,
        text=True
    ).stdout.split(": ")[1].strip()

    print(grub_password_hash)

    
    # Backup the GRUB configuration file
    subprocess.run(["cp", grub_cfg, f"{grub_cfg}.bak"])
    
    # Add the GRUB_PASSWORD line in the GRUB configuration file
    with open(grub_cfg, "a") as f:
        f.write(f"GRUB_PASSWORD={grub_password_hash}\n")
    
    # Update GRUB
    subprocess.run(["update-grub"])
    
    messagebox.showinfo("Info", "GRUB password protection is set.")

def is_root():
    return subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip() == "0"

def grep_grub_password(file_path):
    return subprocess.run(["grep", "-q", "^GRUB_PASSWORD=", file_path]).returncode == 0

# GUI
root = tk.Tk()
root.title("Set GRUB Password")

password_label = tk.Label(root, text="Enter GRUB password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

set_password_button = tk.Button(root, text="Set Password", command=set_grub_password)
set_password_button.pack()

root.mainloop()
