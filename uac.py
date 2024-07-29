import tkinter as tk
from tkinter import messagebox
import subprocess
from tkinter import simpledialog
def UAC(root):
    def list_users():
        result = subprocess.run(['getent', 'passwd'], capture_output=True, text=True)
        users = subprocess.run(['awk', '-F:', '$3 >= 1000 {print $1}'], input=result.stdout, capture_output=True, text=True)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "List of human users:\n")
        output_text.insert(tk.END, users.stdout)
        output_text.config(state=tk.DISABLED)

    def remove_user():
        username = username_entry.get().strip()
        if username:
            result = subprocess.run(['sudo', 'userdel', '-r', username], capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo("User Removed", f"User {username} has been removed.")
            else:
                messagebox.showerror("Error", f"Failed to remove user {username}.")
        else:
            messagebox.showerror("Error", "Please enter a username to remove.")

    def check_password_strength():
        password = password_entry.get().strip()
        if password:
            strength = "Strong" if (len(password) >= 8 and any(char.isdigit() for char in password)
                                   and any(char.isupper() for char in password)
                                   and any(char.islower() for char in password)
                                   and any(char in "!@#$%^&*()_+.," for char in password)) else "Weak"
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"Password strength: {strength}\n")
            output_text.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Please enter a password to check its strength.")

    # def update_password():
    #     username = username_entry.get().strip()
    #     if username:
    #         result = subprocess.run(['sudo', 'passwd', username], capture_output=True, text=True)
    #         if result.returncode == 0:
    #             messagebox.showinfo("Password Updated", f"Password for user {username} has been updated.")
    #         else:
    #             messagebox.showerror("Error", f"Failed to update password for user {username}.")
    #     else:
    #         messagebox.showerror("Error", "Please enter a username to update the password.")

    def update_password():
        username = simpledialog.askstring("Update Password", "Enter the username to update the password:")
        if username:
            new_password = simpledialog.askstring("Update Password", "New password:", show="*")
            if new_password:
                confirm_password = simpledialog.askstring("Update Password", "Retype new password:", show="*")
                if new_password == confirm_password:
                    # Using subprocess to run the passwd command
                    passwd_command = ['sudo', 'passwd', username]
                    passwd_process = subprocess.Popen(passwd_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # Inputting the new password and its retype
                    passwd_process.communicate(input=f"{new_password}\n{confirm_password}\n".encode())
                    if passwd_process.returncode == 0:
                        messagebox.showinfo("Password Updated", f"Password for user {username} has been updated.")
                    else:
                        messagebox.showerror("Error", f"Failed to update password for user {username}.")
                else:
                    messagebox.showerror("Password Mismatch", "Passwords do not match. Please try again.")
            else:
                messagebox.showerror("Error", "Please enter a new password.")
        else:
            messagebox.showerror("Error", "Please enter a username to update the password.")


    # root.title("UAC: User Account Control")

    root_bg_color = root.cget("bg") 

    heading_label = tk.Label(root, text="UAC: User Account Control", font=("Arial", 20),bg=root_bg_color)
    heading_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    description_label = tk.Label(root, text="Manage user accounts and passwords.",bg=root_bg_color)
    description_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    list_users_button = tk.Button(root, text="List all users", command=list_users)
    list_users_button.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    username_label = tk.Label(root, text="Enter username:",bg=root_bg_color)
    username_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    username_entry = tk.Entry(root)
    username_entry.grid(row=3, column=1, padx=10, pady=5)

    remove_user_button = tk.Button(root, text="Remove User", command=remove_user)
    remove_user_button.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    password_label = tk.Label(root, text="Enter password:",bg=root_bg_color)
    password_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=5, column=1, padx=10, pady=5)

    check_password_button = tk.Button(root, text="Check Password Strength", command=check_password_strength)
    check_password_button.grid(row=6, column=0, sticky="w", padx=10, pady=5)

    update_password_button = tk.Button(root, text="Update Password", command=update_password)
    update_password_button.grid(row=7, column=0, sticky="w", padx=10, pady=5)

    output_text_label = tk.Label(root, text="Output:",bg=root_bg_color)
    output_text_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)
    output_text = tk.Text(root, height=5, width=50)
    output_text.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
    output_text.config(state=tk.DISABLED)

# Example usage
# root = tk.Tk()
# UAC(root)
# root.mainloop()
