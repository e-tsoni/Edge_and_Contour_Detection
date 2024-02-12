import cv2


class EdgeDetection:
    def __init__(self, image_object):
        self.image = image_object.image

    def get_image(self):
        return self.image

    def edge_detection(self, t_lower, t_upper):
        if self.image.shape[2] == 3:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # first blur the image
        blurred = cv2.GaussianBlur(self.image, (3, 3), 0)
        # then find edges
        edged = cv2.Canny(blurred, t_lower, t_upper)

        return edged
