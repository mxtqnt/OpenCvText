import cv2
from recortar import recortar_parafo
from conversor import pdf_para_png
from leitor import ler_texto
from conversor import redimencionar

def encontrar_contornos():
    print('Encontrando contornos')
    # Tratamento de imagem
    image = cv2.imread('embalagem.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Dilatação para encontrar parágrafos
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
    dilate = cv2.dilate(thresh, kernel, iterations=4)
    
    cv2.imshow('thresh', cv2.resize(thresh, (960, 540)) )
    cv2.imshow('dilate', cv2.resize(dilate, (960, 540)) )
    cv2.imshow('image', cv2.resize(image, (960, 540)) )
    
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        print('Contorno')
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,255), 2)

        recortar_parafo(x, y, w, h)

        # Transformar recorte de PDF em PNG
        pdf_para_png('recorte.pdf', 'recorte')
        
        recorte = cv2.imread('recorte.png')

        # Mostrar recorte a ser lido
        wh = redimencionar('recorte.png', 80)
        resize = cv2.resize(recorte, wh) 

        c = ler_texto(recorte, c)
        
        cv2.imshow('Area de leitura', resize)
        cv2.waitKey()