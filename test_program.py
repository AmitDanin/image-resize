import base64
import os
import sys
import time
import cv2
import client


def get_frames(video):
    dirname = os.path.dirname(video)
    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    count = 0
    frames = []
    while success:
        success, image = vidcap.read()
        img_path = os.path.join(dirname, "frame%d.jpg" % count)
        cv2.imwrite(img_path, image)  # save frame as JPEG file
        frames.append(img_path)
        count += 1
    return frames


def run_scenario(videos, delay):
    splitted_video = {}
    for video in videos:
        splitted_video[video] = get_frames(video)

    # post task requests
    processed_images = {}
    for video, frames in splitted_video.iteritems():
        for frame in frames:
            processed_images[frame] = client.resize_async(frame)
        time.sleep(delay)

    # get and write resized images
    while processed_images:
        for frame, task in processed_images.iteritems():
            if task.ready():
                content = base64.b64decode(task.get())
                resized_name = os.path.join(os.path.dirname(frame), "resized_" + os.path.basename(frame))
                with open(resized_name, "wb") as f:
                    f.write(content)
                processed_images.pop(frame)
        time.sleep(1)


if __name__ == '__main__':
    number_of_videos = int(sys.argv[1])
    delay = int(sys.argv[2])
    videos = sys.argv[3:3 + number_of_videos]

    run_scenario(videos, delay)
