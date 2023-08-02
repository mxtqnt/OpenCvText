import cv2
import easyocr
from sheetsgpt import conferir_texto
#from corrigir import corretor

open('resultado.txt', 'w').close()
texto=True    

def ler_texto(recorte, c):
    print('Começando leitura')
    angulo = 0
    recorte = cv2.imread('recorte.png')

    #embalagem = recorte[y:(y+h), x:(x+w)] não precisa

    while angulo <= 270:
        reader = easyocr.Reader(['pt', 'pt'], gpu=False)
        result = reader.readtext(recorte,  paragraph="True", detail='False')

        if len(result) <= 0:
            print('Nenhuma palavra encontrada')
            c = c + 1
            return c
        
        for res in result:
            top_left = (int(res[0][0][0]), int(res[0][0][1])) # convert float to int
            bottom_right = (int(res[0][2][0]), int(res[0][2][1])) # convert float to int
            recorte = cv2.putText(recorte, res[1], (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 255), 1)
            for item in result:
                textoparagrafo = str(item[1])
                #texto = conferir_texto(textoparagrafo)
                print(texto)
                if texto:
                    with open('resultado.txt', 'a',  encoding="UTF-8") as f:
                        f.write(item[1]+ ' ')
                    angulo = 360
                else:
                    recorte = cv2.rotate(recorte, cv2.ROTATE_90_CLOCKWISE)
                    angulo = angulo + 90
        
        with open('resultado.txt', 'a',  encoding="UTF-8") as f:
            f.write('\n')
