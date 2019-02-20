import argparse
from tqdm import tqdm
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
                help="path to video folder")
args = vars(ap.parse_args())
vidcap = cv2.VideoCapture(args['video'])
success, image = vidcap.read()
count = 0
skip = 40

length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

for i in tqdm(range(0, length, skip)):
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, i-1)
    success, image = vidcap.read()

    cv2.imwrite("input_images/img_%d.jpg" % count, image)  # save frame as JPEG file
    count += 1
