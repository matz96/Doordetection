#«write python code who detects a door in a picture and calculate the the size of the door»
#«create additionally a output picture where the door is red framed»

import cv2

# Read the image
image = cv2.imread('/home/matz/SynologyDrive/FHNW/bver/CODE/bver_projekt/bver_projekt/door1_Color.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges in the image using Canny edge detection
edges = cv2.Canny(gray, 50, 100)

# Find contours in the edge map
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours
for contour in contours:
    # Check if the contour is a rectangle
    if cv2.isContourConvex(contour) and len(contour) == 4:
        # Calculate the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the aspect ratio of the bounding box is close to 1:2 (typical aspect ratio of a door)
        if abs(w / h - 1 / 2) < 0.1:
            # Calculate the size of the door
            size = (w + h) / 2
            print('Door size:', size)

            # Draw a red rectangle around the door in the output image
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Save the output image
cv2.imwrite('output.jpg', image)

