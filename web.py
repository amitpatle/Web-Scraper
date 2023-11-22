import os
import shutil

def copy_files(source_folder, destination_folder, file_type):
    """
    Copy files of a certain type from a source folder to a destination folder.

    Args:
        source_folder (str): The source folder from which the files will be copied.
        destination_folder (str): The destination folder to which the files will be copied.
        file_type (str): The type of files to be copied.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file_name in os.listdir(source_folder):
        if file_name.endswith(file_type):
            source_file_path = os.path.join(source_folder, file_name)
            destination_file_path = os.path.join(destination_folder, file_name)
            shutil.copy2(source_file_path, destination_file_path)

# Example usage:

# Set the source and destination folders for each file type
source_audio_folder = '/path/to/source/audio/folder'
destination_audio_folder = '/path/to/destination/audio/folder'

source_video_folder = '/path/to/source/video/folder'
destination_video_folder = '/path/to/destination/video/folder'

source_img_folder = '/path/to/source/img/folder'
destination_img_folder = '/path/to/destination/img/folder'

# Set the file types to be scraped
audio_file_type = '.wav'
video_file_type = '.mp4'
img_file_type = '.jpg'

# Call the copy_files function to perform the file scraping
copy_files(source_audio_folder, destination_audio_folder, audio_file_type)
copy_files(source_video_folder, destination_video_folder, video_file_type)
copy_files(source_img_folder, destination_img_folder, img_file_type)
