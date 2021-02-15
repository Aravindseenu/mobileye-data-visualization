#python script to display camera view
import numpy as np
import cv2

cap = cv2.VideoCapture(-1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    # Display the resulting frame
    cv2.imshow('V-tron cam',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
