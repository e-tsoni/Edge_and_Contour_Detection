import os
from PIL import Image
from pathlib import Path

from ImageProperties.ImageProperties import ImageProperties
from EdgeDetection.EdgeDetection import EdgeDetection
from ContourDetection.ContourDetection import ContourDetection

if __name__ == "__main__":

    ############## PATHS FOR THE IMAGES ################################################################################

    # project_path = os.getcwd() # The folder of the project (root)
    project_path = Path(__file__).parent.parent  # The folder of the project (root)
    imgs_path = os.path.join(project_path, 'imgs', 'test_imgs')
    image_path = os.path.join(imgs_path, "office-desk-workspace-table-background.jpeg")
    edged_img_path = os.path.join(imgs_path, 'edged_image.jpeg')

    ############# PARAMETERS DEFINED BY USER ###########################################################################
    parameters_edge = {
        # method: 1 for Sobel, 2 for Canny
        'method': 2,
        'ksize': 3,  # only for Sobel method (default 3)
        'thresholds': (90, 190)  # only for Canny method (default (50, 100))
    }

    parameters_contour = {
        'mode': 1,  # 1=cv2.RETR_EXTERNAL, 2=cv2.RETR_LIST, 3=cv2.RETR_CCOMP, 4=cv2.RETR_TREE, 5=cv2.RETR_FLOODFILL
        'approx_mode': 2,  # 1=cv.CHAIN_APPROX_NONE, 2=cv.CHAIN_APPROX_SIMPLE, 3=cv.CHAIN_APPROX_TC89_L1,
        # 4=cv.CHAIN_APPROX_TC89_KCOS
        'kernel': 1,  # 1=cv2.MORPH_RECT, 2=cv2.MORPH_ELLIPSE, 3=cv2.MORPH_CROSS
        'ksize': (5, 5),
        'iterations': 7  # number of iterations
    }

    ############ EDGE DETECTION ########################################################################################
    image_object = ImageProperties(image_path)
    print(image_object.image_properties())
    edge_detection_object = EdgeDetection(image_object, parameters_edge)
    edged = edge_detection_object.edge_detection()
    # save edged image
    img_to_save = Image.fromarray(edged)
    img_to_save.save(edged_img_path)

    ########### CONTOUR DETECTION ######################################################################################
    contour_detection_object = ContourDetection(edged, image_object.image, parameters_contour)
    contour_detection_object.find_contours()
