from segment_anything import sam_model_registry
import torch
import cv2
from segment_anything import SamAutomaticMaskGenerator

DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
MODEL_TYPE = "vit_h"

CHECKPOINT_PATH=r'/home/cagis/pavement/sam/sam_vit_h_4b8939.pth'
'''
official model pth:
base SAM: /home/cagis/pavement/sam/sam_vit_b_01ec64.pth
Large SAM: /home/cagis/pavement/sam/sam_vit_l_0b3195.pth
Huge SAM: /home/cagis/pavement/sam/sam_vit_h_4b8939.pth
'''
sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH)
sam.to(device=DEVICE)

