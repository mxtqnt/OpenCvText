import easyocr
import cv2

image = cv2.imread('zoomcokie.png')

reader = easyocr.Reader(['pt', 'pt'], gpu=True)
result = reader.readtext(image)

new_image = image

if len(result) <= 0:
    print('Nenhuma palavra encontrada')
    exit(1)

for word in result:
    # print(word)
    print(word[1], word[0])
    start_point = (int(word[0][0][0]), int(word[0][0][1]))
    end_point = (int(word[0][2][0]), int(word[0][2][1]))
    color = (0, 0, 255)
    thickness = 2

    new_image = cv2.rectangle(new_image, start_point, end_point, color, thickness)

cv2.imshow('Palavras encontradas', new_image)
cv2.waitKey(0)