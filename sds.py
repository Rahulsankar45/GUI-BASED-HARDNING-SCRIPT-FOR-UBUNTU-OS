import tkinter as tk
from tkinter import messagebox
import subprocess
import tkinter.simpledialog
from uwf import FireWall
from bll import UrlBlocker
from ssh import SSHHardening
from usb import USBPortControl
from uac import UAC

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("IronShield!")
        self.geometry("1000x800")

        # Create the left side menu
        self.left_menu = tk.Frame(self, bg="lightgray", width=330)
        self.left_menu.pack(side="left", fill="y")

        # Logo
        self.logo = tk.Label(self.left_menu, text="IronShield", font=("Arial", 20), bg="lightgray")
        self.logo.pack(pady=20)

        # Buttons
        buttons = [
            "FireWall", "Url Blocker","UAC","Security Audit", "SSH Hardening", "USB Blocking"
        ]
        for text in buttons:
            button = tk.Button(self.left_menu, text=text, command=lambda t=text: self.show_screen(t))
            button.pack(pady=5, fill="x")

        # Main section
        self.main_section = tk.Frame(self, bg="white", width=600)
        self.main_section.pack(side="left", fill="both", expand=True)

        # Initial screen
        self.current_screen = tk.Label(self.main_section, text="Welcome to IronShield!", font=("Arial", 24), bg="white")
        self.current_screen.pack(expand=True)

    def show_screen(self, screen_name):
        # Remove current screen
        self.current_screen.destroy()

        # Display the selected screen
        if screen_name == "FireWall":
            self.current_screen = tk.Frame(self.main_section, bg="white")
            FireWall(self.current_screen)

        elif screen_name == "Url Blocker":
            self.current_screen = tk.Label(self.main_section, bg="white")
            UrlBlocker(self.current_screen)

        elif screen_name == "UAC":
            self.current_screen = tk.Label(self.main_section, bg="white")
            UAC(self.current_screen)

        elif screen_name == "Security Audit":
            self.current_screen = tk.Label(self.main_section, bg="white")
            big_text = tk.Label(self.current_screen, text="Schedule Security Audit", font=("Arial", 20))
            big_text.grid(row=0, column=0, padx=10, pady=10, sticky="w")

            # Small paragraph below the big text
            small_para = tk.Label(self.current_screen, text="Run Security Audit to check for vulnerabilities", wraplength=300)
            small_para.grid(row=1, column=0, padx=10, pady=5, sticky="w")

            # Button to the right
            button = tk.Button(self.current_screen, text="Run Audit")
            button.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        
        elif screen_name == "SSH Hardening":
            self.current_screen = tk.Label(self.main_section, bg="white")
            SSHHardening(self.current_screen)
        
        elif screen_name == "USB Blocking":
            self.current_screen = tk.Label(self.main_section, bg="white")
            USBPortControl(self.current_screen)


        self.current_screen.pack(expand=True)



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
