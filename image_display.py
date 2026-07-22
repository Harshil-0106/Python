import cv2
image=cv2.imread(r"C:\Users\Harshil Tank\OneDrive\Pictures\Saved Pictures\Wallpaper.jpg")
if image is None:
    print("Error: Could not read the image.")
else:   
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()