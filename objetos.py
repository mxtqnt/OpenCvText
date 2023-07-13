import cv2

imagem = cv2.imread('fatiada.png')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
limiar, imagem_binaria = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 2)
cv2.imshow('Objetos Pretos', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
