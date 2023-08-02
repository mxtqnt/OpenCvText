import easyocr
import cv2
from conversor import redimencionar

image = cv2.imread('embalagem.png')

reader = easyocr.Reader(['pt', 'pt'], gpu=False)
result = reader.readtext(image, paragraph="False")

new_image = image

if len(result) <= 0:
    print('Nenhuma palavra encontrada')
    exit(1)

for res in result:
    top_left = (int(res[0][0][0]), int(res[0][0][1])) # convert float to int
    bottom_right = (int(res[0][2][0]), int(res[0][2][1])) # convert float to int
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 255))
    cv2.putText(image, res[1], (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 255), 2)

# Mostrar recorte a ser lido
wh = redimencionar('recorte.png', 400)
resize = cv2.resize(image, wh) 

cv2.imshow('Resultado', resize)
cv2.waitKey(0)
