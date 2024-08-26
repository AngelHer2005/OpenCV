import numpy as np
import cv2

img = cv2.imread("OpenCV\captura_camara.png")

img = cv2.circle(img, (260,143), 120, (255, 0, 0), 3)

cv2.imshow("Circulo", img)

cv2.waitKey(0)

cv2.destroyAllWindows()