import os
import subprocess

def download_website():
    # Define the target URL
    url = "https://nu-msr.github.io/ros_notes/index.html"
    print(f"Downloading website from: {url}")
    
    # Get the user's Documents directory
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    target_folder = os.path.join(documents_folder, "ros_notes")
    
    print(f"Target folder for download: {target_folder}")
    
    # Create the target directory if it doesn't exist
    try:
        os.makedirs(target_folder, exist_ok=True)
        print(f"Created target directory: {target_folder}")
    except Exception as e:
        print(f"Error creating directory: {e}")
        return
    
    # Construct the wget command
    wget_command = [
        "wget",
        "--mirror",                 # Enable recursive download
        "--convert-links",          # Adjust links for offline use
        "--adjust-extension",       # Ensure proper file extensions
        "--page-requisites",        # Include all assets
        "--no-parent",              # Don't ascend to parent directories
        "-P", target_folder,        # Set the target folder for download
        url                         # The website to download
    ]
    
    print(f"Running wget command: {' '.join(wget_command)}")
    
    try:
        # Run the wget command
        subprocess.run(wget_command, check=True)
        print(f"Website successfully downloaded to {target_folder}")
    except subprocess.CalledProcessError as e:
        print("An error occurred while downloading the website:")
        print(e)

if __name__ == "__main__":
    download_website()
