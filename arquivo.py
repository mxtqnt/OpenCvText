#-*- coding:utf-8 -*-
import cv2
import numpy as np
import easyocr
from senha import API_KEY
import requests
import json

headers = {'Authorization': f'Bearer {API_KEY}'}
link = 'https://api.openai.com/v1/models'
requisicao = requests.post(link, headers)

print(requisicao)



open('result.txt', 'w').close()

# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('testes.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Create rectangular structuring element and dilate
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh, kernel, iterations=4)

# Find contours and draw rectangle
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    #cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,255), 2)
    #cv2.putText(image, ("("+str(x)+", "+str(y)+")"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 100), 2)
    #cv2.putText(image, ("("+str(x + w)+", "+str(y + h)+")"), (x + w, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 100), 2)
    
    # Cropping an image
    cropped_image = image[y:(y+h), x:(x+w)]
    reader = easyocr.Reader(['pt', 'pt'], gpu=False)
    result = reader.readtext(cropped_image, paragraph="False", detail='False')

    new_image = cropped_image

    if len(result) <= 0:
        print('Nenhuma palavra encontrada')
        exit(1)

    for res in result:
        top_left = (int(res[0][0][0]), int(res[0][0][1])) # convert float to int
        bottom_right = (int(res[0][2][0]), int(res[0][2][1])) # convert float to int
        #cv2.putText(cropped_image, res[1], (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 255), 1)
        for item in result:
            with open('result.txt', 'a', encoding="UTF-8") as f:
                f.write(item[1])
                f.write('\n')
            #print(item[1])

#cv2.imshow('thresh', thresh)
#cv2.imshow('dilate', dilate)
cv2.imshow('image', image)
cv2.waitKey()