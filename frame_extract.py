import cv2
import os
import time
import numpy as np
import argparse

parser = argparse.ArgumentParser(
                    prog='pavement data processing',
                    description='extracting frames from video')
parser.add_argument('--video_dir',type=str,default='/home/cagis/pavement/video/4K120fpsLinear.MP4')
parser.add_argument('--out_folder_dir',type=str,default='/home/cagis/pavement/frame')
parser.add_argument('--start_index',type=int,default=0)
parser.add_argument('--nframes',type=int,default=1000)
args=parser.parse_args()

video_dir=args.video_dir
out_folder_dir=args.out_folder_dir
start_index=args.start_index
nframes=args.nframes
# load video using cv2
cam = cv2.VideoCapture(video_dir)
# frame
cam.set(cv2.CAP_PROP_POS_FRAMES,start_index)

print(f'video directory: {video_dir}')
length=cam.get(cv2.CAP_PROP_FRAME_COUNT)
print(f' # frame in total: {length}')
fps=length=cam.get(cv2.CAP_PROP_FPS)
print(f'frame per second: {fps}')
shutter=length=cam.get(cv2.CAP_PROP_XI_SHUTTER_TYPE)
print(shutter)

currentframe=start_index
for i in range(nframes):
    out_name=os.path.join(out_folder_dir,f'frame{currentframe}.jpg')
    ret,frame=cam.read()
    if ret==0:
        break
    cv2.imwrite(out_name, frame)
    currentframe+=1

