import cv2


class ContourDetection:
    def __init__(self, edged, or_img, parameters_contour):
        self.edged = edged
        self.image = or_img
        # self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        self.mode = parameters_contour['mode']
        self.approx_mode = parameters_contour['approx_mode']
        if parameters_contour['kernel'] == 1:
            self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, parameters_contour['ksize'])
        elif parameters_contour['kernel'] == 2:
            self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, parameters_contour['ksize'])
        elif parameters_contour['kernel'] == 3:
            self.kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, parameters_contour['ksize'])
        else:
            print("Invalid kernel")
        self.iterations = parameters_contour['iterations']

    def get_or_img(self):
        return self.image

    def get_edged(self):
        return self.edged

    def find_contours(self):
        dilate = cv2.dilate(self.edged, self.kernel, iterations=self.iterations)
        contours, _ = cv2.findContours(dilate, self.mode, self.approx_mode)
        cv2.drawContours(self.image, contours, -1, (0, 255, 0), 2)
        print(len(contours), "objects were found in this image.")
        cv2.imshow("Edged image", self.edged)
        cv2.imshow("contours", self.image)
        cv2.waitKey(0)
