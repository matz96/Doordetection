import cv2
import numpy as np

# Read the image and convert it to grayscale
image = cv2.imread('/home/matz/SynologyDrive/FHNW/bver/CODE/bver_projekt/bver_projekt/door1_Color.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use the Canny edge detector to find edges in the image
edges = cv2.Canny(gray, 100, 200)

# Use morphological operations to clean up the edge map
kernel = np.ones((3,3), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)
edges = cv2.erode(edges, kernel, iterations=1)

# Use Hough lines to detect lines in the edge map
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

# Draw the detected lines on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Show the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edge-detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


#This code is similar to the previous example, but it uses additional image processing techniques to clean up the edge map and make the detected door frames more distinct. It uses morphological operations (dilation and erosion) to fill in small gaps and remove noise from the edge map, and then uses the Hough lines algorithm to detect lines in the edge map. These detected lines are then drawn on the original image to show the detected door frames.

#As before, you would need to have the OpenCV library installed on your computer and replace the file path in the cv2.imread() call with the path to the image file you want to use. When you run the script, it should display the original and edge-detected images in separate windows, with the detected door frames overlaid on the original image in green.

#Note that this is just an example and may not produce reliable results on all images. You may need to adjust the parameters of the edge detector and image processing steps to optimize the performance for your specific images and door frames.

