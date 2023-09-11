import os
import requests
import gzip

def download_and_save_file(url, folder):
    """
    Download a file from a given URL, save it to the specified folder,
    and decompress it if it's a gzip file.

    Args:
        url (str): The URL of the file to download.
        folder (str): The folder where the file should be saved.

    Returns:
        str: The path to the saved and decompressed file, or None if the download failed.
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Extract the filename from the URL
    filename = os.path.basename(url)

    # Define the path to save the downloaded file
    file_path = os.path.join(folder, filename)

    # Download the file from the URL
    response = requests.get(url)

    # Check if the download was successful
    if response.status_code == 200:
        # Save the downloaded file
        with open(file_path, "wb") as file:
            file.write(response.content)

        # Check if it's a gzip file and decompress if needed
        if filename.endswith(".gz"):
            decompressed_file_path = os.path.join(folder, filename[:-3])  # Remove the ".gz" extension
            with gzip.open(file_path, 'rb') as gz_file:
                decompressed_data = gz_file.read()

            # Save the decompressed file
            with open(decompressed_file_path, "wb") as file:
                file.write(decompressed_data)

            return decompressed_file_path
        else:
            return file_path
    else:
        print(f"Failed to download the file from {url}")
        return None

