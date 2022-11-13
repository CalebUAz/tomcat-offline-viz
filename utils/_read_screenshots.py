import os

def read_screenshots():
    screenshot_map = {}
    key = 0
    folder_dir = "./screenshots/"
    for images in os.listdir(folder_dir):
        # check if the image ends with png or jpg or jpeg
        key = key+1
        if (images.endswith(".png") or images.endswith(".jpg")\
            or images.endswith(".jpeg")):
            # display
            screenshot_map[key] = folder_dir + images
    print('Loaded Screenshots')
    return list(screenshot_map.keys())[0], list(screenshot_map.keys())[-1], list(screenshot_map.values())