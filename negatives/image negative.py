import cv2

# Read image
img = cv2.imread("test2.jpeg")

# Create negative
negative = 255 - img

# Save and show
cv2.imwrite("negative2.jpeg", negative)
cv2.imshow("Negative Image", negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
