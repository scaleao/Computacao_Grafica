import cv2

path = "D:\\Users\\si46407520835\\Desktop\\comp_grafica\\tiger.jpg"

img = cv2.imread(path)

h, w = img.shape[:2]
print("Tamanho da IMG: LARGURA: " + str(w) + "ALTURA: " + str(h))

hnew = int(h/4) #controla a escala da imagem ALTURA
wnew = int(w/4) #controla a escala da imagem LARGURA

resized = cv2.resize(img, (wnew, hnew))
cv2.imshow("Imagem: ", resized)
cv2.waitKey(0)
