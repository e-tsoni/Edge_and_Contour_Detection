import sys as s
import os
import cv2

from pathlib import Path
from edge_and_contour_detection.ImageProperties.ImageProperties import ImageProperties

if __name__ == "__main__":

    # for key in s.modules:
    #     print(key)

    project_path = os.getcwd() # The folder of the project (root)
    # project_path = Path(__file__).parent.parent # The folder of the project (root)
    print(project_path)
    imgs_path = os.path.join(project_path, 'imgs', 'test_imgs')
    print(imgs_path)
    image_path = os.path.join(imgs_path, "office-desk-workspace-table-background.jpeg")
    print(image_path)

    # image = cv2.imread(image_path)
    image_object = ImageProperties(image_path)
    print(image_object.image_properties())

    gray_image = image_object.color_to_grayscale()
    print(gray_image)
