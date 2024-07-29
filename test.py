import subprocess
import os
# def get_recent_html_file(directory):
#     # Run the ls command to list files sorted by time
#     result = subprocess.run(['ls', '-lt', directory], capture_output=True, text=True)
#     if result.returncode == 0:
#         # Extract the first file name from the output
#         files = result.stdout.split('\n')
#         if len(files) >= 2:
#             recent_file = files[1].split()[-1]  # Get the first file name
#             return os.path.join(directory, recent_file)
#         else:
#             return None
#     else:
#         return None
    
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

usg_directory = "/var/lib/usg"
print(get_recent_html_file(usg_directory))