import cv2
import numpy as np


class EdgeDetection:
    def __init__(self, image_object, parameters_dic):
        self.image = image_object.image
        self.method = parameters_dic['method']
        self.ksize = parameters_dic['ksize']
        self.threshold = parameters_dic['thresholds']

    def get_image(self):
        return self.image

    def edge_detection(self):
        if self.image.shape[2] == 3:
            img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
        else:
            img_blur = cv2.GaussianBlur(self.image, (3, 3), 0)

        if self.method == 1:
            sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0,
                               ksize=self.ksize)  # Sobel Edge Detection on the X axis
            sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1,
                               ksize=self.ksize)  # Sobel Edge Detection on the Y axis
            sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1,
                                ksize=self.ksize)  # Combined X and Y Sobel Edge Detection

            cv2.imshow('Sobel X', sobelx)
            cv2.imshow('Sobel Y', sobely)
            cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
            cv2.waitKey(0)

            cv2.destroyAllWindows()

            return sobelxy.astype(np.uint8)

        if self.method == 2:
            edged = cv2.Canny(img_blur, self.threshold[0], self.threshold[1])

            cv2.imshow('Canny Edge Detection', edged)
            cv2.waitKey(0)

            cv2.destroyAllWindows()

            return edged
