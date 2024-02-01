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
parser.add_argument('--start_index',type=int,default=20000)
parser.add_argument('--ns',type=int,default=3)
parser.add_argument('--nfps',type=int,default=5)
parser.add_argument('--sampling',action='store_true')
parser.add_argument('--nframes',type=int,default=10)
args=parser.parse_args()

video_dir=args.video_dir
out_folder_dir=args.out_folder_dir
start_index=args.start_index
nframes=args.nframes
sampling=args.sampling
ns=args.ns
nfps=args.nfps
# load video using cv2
cam = cv2.VideoCapture(video_dir)
# frame
cam.set(cv2.CAP_PROP_POS_FRAMES,start_index)
print(f'video directory: {video_dir}')
length=cam.get(cv2.CAP_PROP_FRAME_COUNT)
print(f'number of frames: {length}')
fps=cam.get(cv2.CAP_PROP_FPS)
print(f'frame per second: {fps}')

focus=cam.get(cv2.CAP_PROP_FOCUS)
print(f'focus: {focus}')

focal_length=cam.get(cv2.CAP_PROP_OPENNI_FOCAL_LENGTH)
print(f'focal_length: {focal_length}')

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f'width and height: {width} {height}')

currentframe = start_index
if sampling:
    nframes=ns*nfps
    for i in range(nframes):
        out_name = os.path.join(out_folder_dir, f'frame{currentframe}.jpg')
        ret, frame = cam.read()
        if ret==0:
            break
        cv2.imwrite(out_name, frame)
        interval=int(fps/nfps)
        currentframe+=interval
        cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)



else:
    for i in range(nframes):
        out_name=os.path.join(out_folder_dir,f'frame{currentframe}.jpg')
        ret,frame=cam.read()
        if ret==0:
            break
        cv2.imwrite(out_name, frame)
        currentframe+=1

