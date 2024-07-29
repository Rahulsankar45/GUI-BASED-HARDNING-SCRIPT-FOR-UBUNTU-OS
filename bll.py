# import os

# def block_website(website_list):
#     hosts_path = '/etc/hosts'
#     with open(hosts_path, 'r+') as file:
#         content = file.read()
#         for website in website_list:
#             if website not in content:
#                 file.write('127.0.0.1 {}\n'.format(website))
#                 print('{} has been blocked.'.format(website))
#             else:
#                 print('{} is already blocked.'.format(website))

# def unblock_website(website_list):
#     hosts_path = '/etc/hosts'
#     with open(hosts_path, 'r') as file:
#         lines = file.readlines()
#     with open(hosts_path, 'w') as file:
#         for line in lines:
#             if not any(website in line for website in website_list):
#                 file.write(line)
#         print('Websites unblocked.')


# websites_to_block = ['www.amazon.in','www.youtube.com','www.facebook.com']
# # block_website(websites_to_block)

# unblock_website(websites_to_block)


# import tkinter as tk
# from tkinter import messagebox
# import subprocess

# def UrlBlocker(root):
#     def block_website():
#         website = website_entry.get().strip()
#         if website:
#             if website not in website_list:
#                 website_list.append(website)
#                 update_blocked_list()
#                 # with open(hosts_path, 'a') as file:
#                 #     file.write('127.0.0.1 {}\n'.format(website))
#                 subprocess.run(['sudo', 'sh', '-c', f'echo "127.0.0.1 {website}" >> /etc/hosts'])
#                 messagebox.showinfo("Website Blocked", "{} has been blocked.".format(website))
#                 messagebox.showinfo("Website Blocked", "{} has been blocked.".format(website))
#             else:
#                 messagebox.showinfo("Website Already Blocked", "{} is already blocked.".format(website))
#         else:
#             messagebox.showerror("Error", "Please enter a website to block.")

#     def unblock_website():
#         # Execute sudo command to read the hosts file
#         result = subprocess.run(['sudo', 'cat', '/etc/hosts'], capture_output=True, text=True)
#         current_content = result.stdout

#         # Modify the content to remove blocked websites
#         website = website_entry.get().strip()
#         new_content = ""
#         for line in current_content.split('\n'):
#             if not website in line:
#                 new_content += line + '\n'

#         website_list.remove(website)
#         update_blocked_list()

#         # Execute sudo command to write the modified content back to the hosts file
#         subprocess.run(['sudo', 'sh', '-c', f'echo "{new_content.strip()}" > /etc/hosts'])

#         messagebox.showinfo("Websites Unblocked", "Websites unblocked.")
#         update_blocked_list()

#     def update_blocked_list():
#         blocked_listbox.delete(0, tk.END)
#         for website in website_list:
#             blocked_listbox.insert(tk.END, website)

#     hosts_path = '/etc/hosts'
#     website_list = []

#     # root = tk.Tk()
#     # root.title("Website Blocker")

#     # Label and Entry for entering website
#     website_label = tk.Label(root, text="Enter website:")
#     website_label.grid(pady=5)
#     website_entry = tk.Entry(root)
#     website_entry.grid(pady=5)

#     # Buttons for blocking and unblocking websites
#     block_button = tk.Button(root, text="Block Website", command=block_website)
#     block_button.grid(pady=5)
#     unblock_button = tk.Button(root, text="Unblock Website", command=unblock_website)
#     unblock_button.grid(pady=5)

#     # Label for showing blocked websites
#     blocked_label = tk.Label(root, text="Blocked Websites:")
#     blocked_label.grid(pady=5)
#     blocked_listbox = tk.Listbox(root, height=5, width=50)
#     blocked_listbox.grid(pady=5)

#     # Initial update of blocked websites list
#     update_blocked_list()

# # root.mainloop()


import tkinter as tk
from tkinter import messagebox
import subprocess

def UrlBlocker(root):
    def block_website():
        website = website_entry.get().strip()
        if website:
            if website not in website_list:
                website_list.append(website)
                update_blocked_list()
                subprocess.run(['sudo', 'sh', '-c', f'echo "127.0.0.1 {website}" >> /etc/hosts'])
                messagebox.showinfo("Website Blocked", "{} has been blocked.".format(website))
            else:
                messagebox.showinfo("Website Already Blocked", "{} is already blocked.".format(website))
        else:
            messagebox.showerror("Error", "Please enter a website to block.")

    def unblock_website():
        result = subprocess.run(['sudo', 'cat', '/etc/hosts'], capture_output=True, text=True)
        current_content = result.stdout

        website = website_entry.get().strip()
        new_content = ""
        for line in current_content.split('\n'):
            if not website in line:
                new_content += line + '\n'

        website_list.remove(website)
        update_blocked_list()

        subprocess.run(['sudo', 'sh', '-c', f'echo "{new_content.strip()}" > /etc/hosts'])

        messagebox.showinfo("Websites Unblocked", "Websites unblocked.")
        update_blocked_list()

    def update_blocked_list():
        blocked_listbox.delete(0, tk.END)
        for website in website_list:
            blocked_listbox.insert(tk.END, website)

    website_list = []

    root_bg_color = root.cget("bg")  # Get the background color of the root window

    heading_label = tk.Label(root, text="URL Blocking", font=("Arial", 20), bg=root_bg_color)  # Set background color to root background color
    heading_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # Create a spacer label to push the button to the right
    spacer_label = tk.Label(root, text="", bg=root_bg_color)  # Set background color to root background color
    spacer_label.grid(row=0, column=1, sticky="we")  # Column weight is set to expand the spacer

    # Text label with smaller font
    text_label = tk.Label(root, text="Block or unblock websites by entering their URLs below.", font=("Arial", 12), wraplength=550, justify="left", bg=root_bg_color)  # Set background color to root background color
    text_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=10, pady=5)

    # Column weight to expand the spacer
    root.grid_columnconfigure(1, weight=1)

    # Label and Entry for entering website
    website_label = tk.Label(root, text="Enter website:", bg=root_bg_color)  # Set background color to root background color
    website_label.grid(row=2, column=0,sticky="w",padx=10, pady=5)

    website_entry = tk.Entry(root)
    website_entry.grid(row=3, sticky="w",column=0,padx=10, pady=5)

    # Buttons for blocking and unblocking websites
    block_button = tk.Button(root, text="Block Website", command=block_website)
    block_button.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="w")  # Adjust padx to add space between buttons

    unblock_button = tk.Button(root, text="Unblock Website", command=unblock_website)
    unblock_button.grid(row=4, column=1, pady=5, sticky="w")


    # Label for showing blocked websites
    blocked_label = tk.Label(root, text="Blocked Websites:", bg=root_bg_color)  # Set background color to root background color
    blocked_label.grid(row=5, column=0,padx=10, pady=5)

    blocked_listbox = tk.Listbox(root, height=5, width=50)
    blocked_listbox.grid(row=6, column=0,padx=10, pady=5)

    # Initial update of blocked websites list
    update_blocked_list()
# Example usage
# root = tk.Tk()
# root.title("URL Blocking")
# UrlBlocker(root)
# root.mainloop()
