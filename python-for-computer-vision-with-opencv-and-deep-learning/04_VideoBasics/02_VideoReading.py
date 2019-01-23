import cv2

cap = cv2.VideoCapture('mysupervideo.mp4')

if cap.isOpened() == False:
    print("File not found or Wrong codec")

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
    
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()