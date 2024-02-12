import cv2


class ImageProperties:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.type = type(self.image)
        self.shape = self.image.shape
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        if self.image.shape[2] != 0:
            self.channels = self.image.shape[2]
        else:
            self.channels = 1
        self.pixels = self.image.shape[0] * self.image.shape[1]
        self.data_type = self.image.dtype

    def get_type(self):
        return self.type

    def get_shape(self):
        return self

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_channels(self):
        return self.channels

    def get_pixels(self):
        return self.pixels

    def get_data_type(self):
        return self.data_type

    def image_properties(self):
        print(f"Image Properties:\nType: {self.type}\nShape: {self.shape}\nHeight: {self.height}\nWidth: {self.width}\n"
              f"Channels: {self.channels}\nPixels: {self.pixels}\nDataType: {self.data_type}")

    def color_to_grayscale(self):
        copy_image = self.image.copy()
        gray_image = cv2.cvtColor(copy_image, cv2.COLOR_BGR2GRAY)

        return gray_image
