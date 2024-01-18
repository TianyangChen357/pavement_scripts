import cv2
import os
import time
import numpy as np
basedir=r'/home/cagis/pavement'
video_folder=os.path.join(basedir,'video')
frame_folder=os.path.join(basedir,'frame')
start=time.time()
# one video for testing
video_dir=os.path.join(video_folder,'4K120fpsLinear.MP4')
# load video using cv2
cam = cv2.VideoCapture(video_dir)
# frame
currentframe = 0
ret, frame = cam.read()
print(ret)
print(frame.shape)

length=cam.get(cv2.CAP_PROP_FRAME_COUNT)
print(f' # frame in total: {length}')

fps=length=cam.get(cv2.CAP_PROP_FPS)
print(f'frame per second: {fps}')

shutter=length=cam.get(cv2.CAP_PROP_XI_SHUTTER_TYPE)
print(shutter)


# for i in range(100):
#     name=os.path.join(frame_folder,f'frame{currentframe}.jpg')
#     ret,frame=cam.read()
#     cv2.imwrite(name, frame)
#     currentframe+=1

for i in range(10):
    name=os.path.join(frame_folder,f'frame{currentframe}.npy')
    ret,frame=cam.read()
    np.save(name,frame)
    currentframe+=1
end=time.time()

print(f'computing time: {end-start}')
