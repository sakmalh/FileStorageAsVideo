from binaryPic import binfile_to_pics, read_binary_pics
from video_utils import video_to_pics, pics_to_video
from zip_utils import binary_to_zip, zip_to_binary_file


def create_a_video(zip_file: str):
    zip_to_binary_file(zip_file=zip_file)
    binfile_to_pics("file.bin")
    pics_to_video("testzip.avi")


# create_a_video("/home/akmal/Downloads/Afrin_cv.zip")


def video_to_file(video_file: str):
    video_to_pics(video_file)
    read_binary_pics()
    binary_to_zip(restore_zip="Test")


# video_to_file("testzip.avi")
