import cv2
# LEER, VISUALIZAR Y GUARDAR UNA IMAGEN

# Este método leerá la imagen y como segundo parámetro puedes colocarle 0 si quieres que esté en escala de grises.
imagen = cv2.imread("Ejercicio1\melody6.png")

# Este método muestra la imagen en cuestión nombrando el título de programa como primer parámetro.
cv2.imshow("Imagen", imagen)

# Este método permite guardar la imagen leída; además de eso, puedes cambiar el formato de imagen.
cv2.imwrite("Ejercicio1\Imagen GOD.jpg", imagen)

# Este método permite detener el código en milísegundos, si quieres que se detenga presionando cualquier tecla, pon 0.
cv2.waitKey(10000)

# Este método destruye todas las ventanas generadas por el código.
cv2.destroyAllWindows()