import os
from os import listdir
 
# get the path or directory
screenshot_map = {}
key = 0
folder_dir = "/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots"
for images in os.listdir(folder_dir):
    # check if the image ends with png or jpg or jpeg
    key = key+1
    if (images.endswith(".png") or images.endswith(".jpg")\
        or images.endswith(".jpeg")):
        # display
        screenshot_map[key] = images
        print(key)
        # print(images)
print(screenshot_map)