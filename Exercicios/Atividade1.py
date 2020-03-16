import cv2

path = "C:\\Users\\Public\\Pictures\\tiger.jpg"

img = cv2.imread(path)

h, w = img.shape[:2]
print("Tamanho da IMG: LARGURA: " + str(w) + "ALTURA: " + str(h))

hnew = int(h/2) #controla a escala da imagem ALTURA
wnew = int(w/2) #controla a escala da imagem LARGURA

resized = cv2.resize(img, (wnew, hnew))
cv2.imshow("Imagem: ", resized)
cv2.waitKey(0)

#INTERPOLAÇÃO é o processo de redimencionamento da imagem atraves de algoritmo de interpolação

#FORMAÇÃO DAS CORES a gente enxerga um vectro eletromagnetico de cores limitado, Isaac Newton comprovou isso com o
#experimento de espectro de cores atraves do prisma.

#A percepção da cor de um objeto é equivalente ao compromento de onde que este objeto reflete quando ele é submetido
# ao processo de iluminação

#SHAPE DA IMAGEM NO OPENCV --> shape(Altura = y, Comprimento = x, canais = BGR ou RGB)

#Na hora de converter um imagem para cinza o canais do Verde é o que mais trás da percepção de realidade

#ANALISE DE HISTOGRAMA, equalização das cores e melhor distribuição de cores, faz com que as cores fiquem mais proximas
#das cores reais, FOTO DA LENA

#ESPAÇOS DE COR, Sensações de cor: brilho, matiz, coloração, luminância, croma e saturação
#ESPAÇOS DE CORE = RBG, CMYK, YCbCr, YUV

#ESCALA DE CINZA 0.30 * R/ 0,11 * B/ 0,59 * G