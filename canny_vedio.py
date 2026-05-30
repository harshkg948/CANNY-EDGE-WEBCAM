import cv2 
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    canny = cv2.Canny(frame,threshold1=30,threshold2=150)
    cv2.imshow("blunder",canny)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break
cap.release()
cv2.destroyAllWindows()    
    
    