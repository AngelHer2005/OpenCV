import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se encuentra una cámara.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se obtiene el frame. Saliendo...")
        break
    
    frame = cv2.line(frame, (0, 0), (frame.shape[1] - 1, frame.shape[0] - 1), (0, 0, 255), 5)

    cv2.imshow("Linea", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()