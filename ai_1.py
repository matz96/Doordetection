import cv2

# Load the input image
img = cv2.imread("input.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection to the grayscale image
edges = cv2.Canny(gray, 50, 100)

# Define the kernel for dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# Dilate the edges
dilated = cv2.dilate(edges, kernel)

# Find contours in the dilated image
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours and draw a rectangle around each one
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# Save the output image
cv2.imwrite("output.jpg", img)
