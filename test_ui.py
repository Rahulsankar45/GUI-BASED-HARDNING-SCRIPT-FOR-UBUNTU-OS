import tkinter as tk

def on_button_click():
    print("Button clicked")

root = tk.Tk()
root.title("UI Example")

# Set the initial size of the window
root.geometry("600x400")

# Heading label with big font
heading_label = tk.Label(root, text="FireWall", font=("Arial", 20))
heading_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# Create a spacer label to push the button to the right
spacer_label = tk.Label(root, text="")
spacer_label.grid(row=0, column=1, sticky="we")  # Column weight is set to expand the spacer

# Button at the extreme right side
button = tk.Button(root, text="Enable", command=on_button_click)
button.grid(row=0, column=2, sticky="e", padx=10, pady=10)

# Text label with smaller font
text_label = tk.Label(root, text="Control network ports and firewall rules with ufw. Allow/Deny specific ports protocols and enable/disable ssh. Configure manage and ensure network security through the firewall configuration.", font=("Arial", 12), wraplength=550, justify="left")
text_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=10, pady=5)

# Column weight to expand the spacer
root.grid_columnconfigure(1, weight=1)

root.mainloop()
