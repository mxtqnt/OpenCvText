import pdf2image
import cv2

poppler_path = r'C:\Users\ana.santos\Documents\poppler-23.07.0'

def pdf_para_png(embalagempdf, nome):
    print('Convertendo pdf para png')
    images = pdf2image.convert_from_path(str(embalagempdf), use_cropbox=True)
    images[0].save(str(nome) + '.png', 'PNG') 

def redimencionar(imagem, escala):
    src = cv2.imread(str(imagem), cv2.IMREAD_UNCHANGED)

    width = int(src.shape[1] * escala / 100)
    height = int(src.shape[0] * escala / 100)

    wh = (width, height)

    return wh