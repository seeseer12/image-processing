import cv2
# Read the image
a=input("enter the name of image")
img = cv2.imread(a)

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Show the image
    cv2.imshow("My Image", img)

    
    # cv2.waitKey(0)
    cv2.waitKey(5000)  # waits 5000 milliseconds (5 seconds)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
