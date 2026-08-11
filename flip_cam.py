import cv2

cap = cv2.VideoCapture(0)

# Flip modes:
# 1  = horizontal
# 0  = vertical
# -1 = both
# None = normal
flip_mode = None


def mouse_callback(event, x, y, flags, param):
    global flip_mode

    if event == cv2.EVENT_LBUTTONDOWN:
        if flip_mode == 1:
            flip_mode = None
        else:
            flip_mode = 1


cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", mouse_callback)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access webcam")
        break

    # Apply selected flip
    if flip_mode is not None:
        frame = cv2.flip(frame, flip_mode)

    cv2.imshow("Webcam", frame)

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF

    if key == ord('h'):
        flip_mode = 1          # Horizontal

    elif key == ord('v'):
        flip_mode = 0          # Vertical

    elif key == ord('b'):
        flip_mode = -1         # Both

    elif key == ord('n'):
        flip_mode = None       # Normal

    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()