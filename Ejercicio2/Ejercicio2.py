import cv2

# Capturar, guardar y leer un vídeo.


# Este método permitirá usar tu cámara que estás usando, el parámetro especifica cual cámara utilizará.
capturaV = cv2.VideoCapture(1)

# Este método permite guardar el vídeo.
video = cv2.VideoWriter("Ejercicio2/video.mp4", cv2.VideoWriter_fourcc(*"mp4v"),20.0,(640,480))

# Permitimos el vídeo con un bucle while.
while(capturaV.isOpened()):
    # Leemos el vídeo, ret verifica si recibimos una imagen.
    ret, imagen = capturaV.read()
    if ret==True:
        # Mostraremos la imagen.
        cv2.imshow("video", imagen) 
        
        # Guardamos el vídeo.
        video.write(imagen)
        
        # La documentación indica que se tiene que realizar de la siguiente manera.
        # Si quieres cerrar con escape, en vez de ord("[letra]"), coloca 27 que es escape en código ASCII
        if cv2.waitKey(30) & 0xFF == ord("s"):
            break
    else: break
# Finalizamos el vídeo o la cámara.
capturaV.release()
video.release()
cv2.destroyAllWindows()


# Y para leer el vídeo que hemos creado.
capturaV = cv2.VideoCapture('Ejercicio2/video.mp4')

while(capturaV.isOpened()):
    ret, imagen = capturaV.read()
    if ret==True:
        cv2.imshow("video", imagen) 
        if cv2.waitKey(30) & 0xFF == ord("s"):
            break
    else: break
        
capturaV.release()
cv2.destroyAllWindows()