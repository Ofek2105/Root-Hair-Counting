import cv2
import numpy as np


"""
This file will grab and plot an image 
and allow the user to check the rgb value of any clicked pixel.
the value will appear in the terminal 
"""

# Function to handle mouse clicks
def click_event(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    # Get the HSV values of the clicked pixel
    pixel_hsv = hsv_image[y, x]
    # print(f"HSV Values at ({x}, {y}): Hue={pixel_hsv[0]}, Saturation={pixel_hsv[1]}, Value={pixel_hsv[2]} => ")
    print(f"({pixel_hsv[0]}, {pixel_hsv[1]}, {pixel_hsv[2]}), ", end="")


if __name__ == '__main__':
  image = cv2.imread(r'results/type_3/arb_sr_x4.png')
  hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  # Create a window and set the mouse callback function
  cv2.imshow('Image', image)
  cv2.setMouseCallback('Image', click_event)

  # Display the img until a key is pressed
  cv2.waitKey(0)
  cv2.destroyAllWindows()
