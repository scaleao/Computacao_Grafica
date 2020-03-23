import cv2
import numpy as np

path = "C:\\Users\\Public\\Pictures\\tiger.jpg"

img = cv2.imread(path)
h, w = img.shape[:2]

cv2.imshow("Imagem", img)

imgCopy = img.copy()
#imagem normalizada
imgCopy = imgCopy/255

imgCMYK = np.zeros((h, w, 4), np.float)
# 0 C = Ciano =   (1 - red - black ) / (1 - black)
# 1 M = Magenta = (1 - green) - black) / (1 - black)
# 2 Y = Yellow =  (1 - blue - black) / (1 - black)
# 3 K = Black = (minCiano, minMagenta, minYellow)

for i in range(h):
    for j in range(w):
        black = np.min([imgCopy[i, j, 0], imgCopy[i, j, 1], imgCopy[i, j, 2]])
        if (1 - black) == 0:
            black = 0.99998
        blue = imgCopy[i, j, 0]
        green = imgCopy[i, j, 1]
        red = imgCopy[i, j, 2]

        imgCMYK[i, j, 3] = black
        imgCMYK[i, j, 0] = (1 - red - black) / (1 - black)
        imgCMYK[i, j, 1] = (1 - green - black) / (1 - black)
        imgCMYK[i, j, 2] = (1 - blue - black) / (1 - black)

imgCMYK = (imgCMYK * 255).astype("uint8")
cv2.imshow("Black", imgCMYK[:, :, 3])
cv2.imshow("Ciano", imgCMYK[:, :, 0])
cv2.imshow("Magenta", imgCMYK[:, :, 1])
cv2.imshow("Yellow", imgCMYK[:, :, 2])
cv2.waitKey(0)