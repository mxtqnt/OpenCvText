import cv2

# Carregar a imagem
imagem = cv2.imread('cookiefull.png', 0)  # 0 para carregar em escala de cinza

# Aplicar o threshold
limiar, imagem_threshold = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

# Exibir a imagem original e a imagem com o threshold aplicado
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem com Threshold', imagem_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
