import cv2
import glob
from utils import reset_folder


def video_to_pics(video_file: str):
    capture = cv2.VideoCapture(video_file)
    frame_number = 0
    reset_folder("videoout")

    while True:
        success, frame = capture.read()
        if success:
            cv2.imwrite("%s/frame_%s.jpg" % ("videoout", frame_number), frame)
        else:
            break

        frame_number = frame_number + 1

    capture.release()


def pics_to_video(output_video: str):
    frameSize = (480, 360)

    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

    for filename in glob.glob("video/*.png"):
        img = cv2.imread(filename)
        out.write(img)

    out.release()


