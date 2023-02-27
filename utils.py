import os


def reset_folder(folder_name: str):
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)
        os.remove(file_path)

# reset_folder("video")
