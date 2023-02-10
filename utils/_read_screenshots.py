import os
import cv2
import glob 

# def read_screenshots():
#     screenshot_map = {}
#     key = 0
#     folder_dir = "/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/"
#     for images in sorted(os.listdir(folder_dir)):
#         # check if the image ends with png or jpg or jpeg
#         key = key+1
#         if (images.endswith(".png") or images.endswith(".jpg")\
#             or images.endswith(".jpeg")):
#             # display
#             screenshot_map[key] = folder_dir + images
#     print('Loaded Screenshots')
#     return list(screenshot_map.keys())[4000], list(screenshot_map.keys())[20000], list(screenshot_map.values())[4000:20000]

def read_screenshots():
    images = []
    for cnt, im_path in enumerate(glob.glob('/Users/calebjonesshibu/Desktop/tom/exp_2023_02_03_10/tiger/screenshots/screenshots/*.*')):
        if cnt == 50:
            break
        images.append(cv2.imread(im_path))
    return 0, 50, images