import numpy as np
import cv2

img = cv2.imread("OpenCV\captura_camara.png")

img = cv2.rectangle(img, (149,256), (357,49), (255,0,0),3)

cv2.imshow("Rectangulo", img)

cv2.waitKey(0)

cv2.destroyAllWindows()