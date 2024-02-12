import sys as s
import os
import cv2

from pathlib import Path

if __name__ == "__main__":

    # for key in s.modules:
    #     print(key)

    project_path = os.getcwd() # Current Working Directory, the folder that the Python is running in (root)
    print(project_path)
    imgs_path = os.path.join(project_path, 'imgs', 'test_imgs')
    print(imgs_path)
    image_path = os.path.join(imgs_path, "office-desk-workspace-table-background.jpeg")
    print(image_path)

    image = cv2.imread(image_path)
