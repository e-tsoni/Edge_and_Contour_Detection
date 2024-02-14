import sys as s
import os
import cv2
from PIL import Image
import numpy as np
from pathlib import Path

from ImageProperties.ImageProperties import ImageProperties
from EdgeDetection.EdgeDetection import EdgeDetection


if __name__ == "__main__":

    ############## PATHS FOR THE IMAGES ################################################################################

    # project_path = os.getcwd() # The folder of the project (root)
    project_path = Path(__file__).parent.parent  # The folder of the project (root)
    imgs_path = os.path.join(project_path, 'imgs', 'test_imgs')
    image_path = os.path.join(imgs_path, "office-desk-workspace-table-background.jpeg")
    edged_img_path = os.path.join(imgs_path, 'edged_image.jpeg')

    ############# PARAMETERS DEFINED BY USER ###########################################################################
    parameters_dic = {
        # method: 1 for Sobel, 2 for Canny
        'method': 2,
        'ksize': 3,  # only for Sobel method (default 3)
        'thresholds': (50, 100)  # only for Canny method (default (50, 100))
    }

    ############ EDGE DETECTION ########################################################################################
    image_object = ImageProperties(image_path)
    print(image_object.image_properties())

    edge_detection_object = EdgeDetection(image_object, parameters_dic)
    edged = edge_detection_object.edge_detection()

    img_to_save = Image.fromarray(edged)
    edged_img_path = os.path.join(imgs_path, 'edged_image.jpeg')
    img_to_save.save(edged_img_path)
