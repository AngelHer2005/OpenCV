import cv2
import os

# Esté código graba con la cámara y toma captura con 'Enter'.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se encuentra una cámara.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se obtiene el frame. Saliendo...")
        break

    text = "'Enter' para tomar captura - 'Esc' para salir."
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.7
    font_color = (47, 117, 44) 
    thickness = 2
    line_type = cv2.LINE_AA

    cv2.putText(frame, text, (38, 470), font, font_scale, font_color, thickness, line_type)

    cv2.imshow("Camara", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 13:
        img_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captura_camara.png")
        cv2.imwrite(img_name, frame)
        print(f"Imagen guardada como '{img_name}'")
    elif key == 27:
        os.system('cls')
        print("Saliendo...")
        break

cap.release()
cv2.destroyAllWindows()