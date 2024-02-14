<img src="imgs\UML\Requirements.jpg"/>

## Requirements / Main Functionality

- The user can upload a photo.
- The user can choose between different parameters for edge detection, contour detection and object counting.  
- The app checks and print the photo's properties.
- The app find the edges and saves the edged picture in the disc.
- The app shows contours of objects in user's screen.
- The app counts the objects in the picture (based on the input parameters).

## User Input

Dictionaries:
- parameters_edge{}
- parameters_contour{}

For more details regarding the parameters, please visit:
[OpenCV documentation](https://docs.opencv.org/3.4/index.html)
- [Canny Edge Detection](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html)
- [Sobel Edge Detection](https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html)
- [Contours](https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html)


## How to use:
In the "edge_and_contour_detection.py":
1. give the right parameters (dictionaries).
2. run the script.

## Packages

- Image.__version__ == 10.2.0
- cv2.__version__ == 4.8.1
- np.__version__ == 1.26.0

## Use Cases

<img alt="N|Use Cases" src="imgs\UML\UC_edges_and_contours.png"/>

## Class Diagram 

<img alt="N|Class Diagram" src="imgs\UML\ClassDiagram.png"/>
