import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import os
import re

def run_audit():
    loading_label.pack()
    audit_button.config(state=tk.DISABLED)
    loading_thread = threading.Thread(target=run_audit_command)
    loading_thread.start()

def get_recent_html_file(directory):
    # Run the ls command to list files sorted by time
    result = subprocess.run(['ls', '-lt', directory], capture_output=True, text=True)
    if result.returncode == 0:
        # Extract the file names from the output
        files = result.stdout.split('\n')
        for file_info in files[1:]:
            file_info = file_info.split()
            if len(file_info) > 8 and file_info[-1].endswith('.html'):
                return os.path.join(directory, file_info[-1])
        return None
    else:
        return None


def run_audit_command():
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        tailor_xml_path = os.path.join(current_directory, "tailor.xml")
        
        # Run the audit command with the full path to tailor.xml
        # result = subprocess.run(['sudo', 'usg', 'audit', '--tailoring-file', tailor_xml_path], capture_output=True, text=True)
        
         # Extract the path to the HTML report from the output
        usg_directory = "/var/lib/usg"
        html_report_path = get_recent_html_file(usg_directory)
        print(html_report_path)
        if html_report_path!=None:
            # result = subprocess.run(['whoami'], capture_output=True, text=True)
            result='noob'
            if result!='':
                # current_user = result.stdout.strip()
                current_user = result
                print("Current user:", current_user)
                basename = os.path.basename(html_report_path)
                print(basename)
                subprocess.run([f'sudo cp {html_report_path} /home/{current_user}/Desktop'], capture_output=True, text=True)
                subprocess.run([f'sudo chown {current_user}:users /home/{current_user}/Desktop/{basename}'], capture_output=True, text=True)
            else:
                print("Error:", result.stderr)
            messagebox.showinfo("Audit Complete", f"Audit process completed successfully! HTML report: {html_report_path}")
        else:
            messagebox.showwarning("Audit Complete", "Audit process completed successfully, but HTML report path not found.")

    
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        loading_label.pack_forget()
        audit_button.config(state=tk.NORMAL)

# def extract_html_report_path(output):
#     # Define a regular expression pattern to match the HTML report path
#     pattern = r'/var/lib/usg/usg-report-\d+.\d+.html'
#     # Search for the pattern in the output
#     match = re.search(pattern, output)
#     if match:
#         return match.group(0)
#     else:
#         return None

root = tk.Tk()
root.title("Audit Tool")

audit_button = tk.Button(root, text="Run Audit", command=run_audit)
audit_button.pack(pady=10)

loading_label = tk.Label(root, text="Running audit, please wait...", font=("Arial", 12))

root.mainloop()
