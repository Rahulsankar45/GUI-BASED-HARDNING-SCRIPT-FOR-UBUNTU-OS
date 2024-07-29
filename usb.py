import tkinter as tk
import subprocess

def USBPortControl(root):
    def list_usb_devices():
        command = "lsusb"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            devices = [line.strip() for line in result.stdout.split("\n") if line.strip()]
            if devices:
                # Display the list of USB devices
                output_text.config(state=tk.NORMAL)
                output_text.delete(1.0, tk.END)  # Clear the device list
                output_text.insert(tk.END, "\n".join(devices))
                output_text.config(state=tk.DISABLED)
                status_label.config(text="USB devices listed successfully.")
            else:
                status_label.config(text="No USB devices found.")
        else:
            status_label.config(text="Failed to list USB devices.")

    def block_all_usb_ports():
        command = "lsusb | awk '{print $6}' | sudo xargs -I{} usbguard block-device {}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            status_label.config(text="All USB ports blocked successfully.")
        else:
            status_label.config(text="Failed to block USB ports.")

    def unblock_all_usb_ports():
        command = "lsusb | awk '{print $6}' | sudo xargs -I{} usbguard allow-device {}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            status_label.config(text="All USB ports unblocked successfully.")
        else:
            status_label.config(text="Failed to unblock USB ports.")

    # root.title("USB Port Control")
    root_bg_color = root.cget("bg") 

    # Create heading for USB Blocking
    heading_label = tk.Label(root, text="USB Blocking", font=("Arial", 20), bg=root_bg_color)
    heading_label.pack(pady=10, anchor="w")

    # Description line
    description_label = tk.Label(root, text="Control USB device access by blocking or unblocking USB ports.", bg=root_bg_color)
    description_label.pack(anchor="w")

    # Buttons for blocking all ports and unblocking all ports
    block_button = tk.Button(root, text="Block All Ports", command=block_all_usb_ports)
    block_button.pack(pady=5, anchor="w")
    unblock_button = tk.Button(root, text="Unblock All Ports", command=unblock_all_usb_ports)
    unblock_button.pack(pady=5, anchor="w")
    list_button = tk.Button(root, text="List USB Devices", command=list_usb_devices)
    list_button.pack(pady=5, anchor="w")

    # Create label for status messages
    status_label = tk.Label(root, text="", bg=root_bg_color)
    status_label.pack(pady=5, anchor="w")

    # Create text widget to display USB devices
    device_list_label = tk.Label(root, text="USB Devices:", bg=root_bg_color)
    device_list_label.pack(pady=5, anchor="w")
    output_text = tk.Text(root, height=10, width=50, bg=root.cget("bg"), state=tk.DISABLED)
    output_text.pack(anchor="w")

# Example usage
# root = tk.Tk()
# USBPortControl(root)
# root.mainloop()
