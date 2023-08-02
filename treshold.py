import cv2
from conversor import redimencionar

pngcompleto = cv2.imread('embalagem.png')
# Aplicar o threshold
limiar, imagem_threshold = cv2.threshold(pngcompleto, 127, 255, cv2.THRESH_BINARY)
# Exibir a imagem original e a imagem com o threshold aplicado
gray = cv2.cvtColor(pngcompleto, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Dilatação para encontrar parágrafos
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,1))
dilate = cv2.dilate(thresh, kernel, iterations=4)

# Find contours and draw rectangle
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(pngcompleto, (x, y), (x + w, y + h), (255,0,255), 2)
    cv2.putText(pngcompleto, ("("+str(x)+", "+str(y)+")"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 100), 1)
    cv2.putText(pngcompleto, ("("+str(x + w)+", "+str(y + h)+")"), (x + w, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 100), 1)


cv2.imwrite('contorno.png', pngcompleto)
# cv2.imwrite('gray.png', gray)
# cv2.imwrite('blur.png', blur)
# cv2.imwrite('thresh.png', thresh)
# cv2.imwrite('dilate.png', dilate)

wh = redimencionar('contorno.png', 50)
resize = cv2.resize(pngcompleto, wh) 

cv2.imshow('Area de leitura', resize)
cv2.waitKey()

# cv2.imshow('original.png', pngcompleto)
# cv2.imshow('gray.png', gray)
# cv2.imshow('blur.png', blur)
# cv2.imshow('thresh.png', thresh)
# cv2.imshow('dilate.png', dilate)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
