import cv2
import easyocr
from pypdf import PdfWriter, PdfReader
from pypdf.generic import RectangleObject
import pdf2image

poppler_path = r'C:\Users\ana.santos\Documents\poppler-23.07.0'
open('result.txt', 'w').close()

# Arquivo Mãe
fpdf = "embalagem.pdf"

# PDF
reader = PdfReader(fpdf)
writer = PdfWriter()
sourcepage = reader.pages[0]

# Pegar tamanho PDF
pdfw = sourcepage.mediabox.width
pdfh = sourcepage.mediabox.height

# PDF completo para PNG completo 
images = pdf2image.convert_from_path(fpdf, use_cropbox=True)
images[0].save('balinhacompleta' + '.png', 'PNG')
pngcompleto = cv2.imread('balinhacompleta.png')

# Altura e Largura Imagem
h, w, c = pngcompleto.shape
cvw = w
cvh = h
print('width:  ', w)
print('height: ', h)

# Tratamento de imagem
gray = cv2.cvtColor(pngcompleto, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Dilatação para encontrar parágrafos
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh, kernel, iterations=4)
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    # Cordenadas do parágrafo no OpenCV
    x,y,w,h = cv2.boundingRect(c)
    cvx1 = x
    cvy1 = y
    cvx2 = x + w
    cvy2 = y + h

    # Delimitar parágrafos
    cv2.rectangle(pngcompleto, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Cordenadas PDF
    pdfx1 = ((pdfw*cvx1)/cvw)
    pdfy1 = ((pdfh*cvy1)/cvh)
    pdfx2 = ((pdfw*cvx2)/cvw)
    pdfy2 = ((pdfh*cvy2)/cvh)

    reader = PdfReader(fpdf)
    page = reader.pages[0]
    sourcepage = reader.pages[0]
    
    # Definir área de corte
    page.cropbox = RectangleObject((pdfx1, (pdfh - pdfy1), pdfx2, (pdfh - pdfy2)))

    # Armazenar novo PDF
    writer.add_page(reader.pages[0])
    with open("paragrafo.pdf", "wb") as fp:
        writer.write(fp)

    # Convertendo PDF para PNG
    images = pdf2image.convert_from_path("paragrafo.pdf", use_cropbox=True)
    images[0].save('paragrafo' + '.png', 'PNG')
    paragrafo = cv2.imread('paragrafo.png')

    cv2.imshow('Paragrafo', paragrafo)
    cv2.waitKey()

    # Leitura do conteúdo
    reader = easyocr.Reader(['pt', 'pt'], gpu=False)
    result = reader.readtext(paragrafo, paragraph="False", detail='False')
    for item in result:
        with open('result.txt', 'a', encoding="UTF-8") as f:
            f.write(item[1])
            f.write('\n')

cv2.imshow('dilate', dilate)
cv2.imshow('Embalagem', pngcompleto)
cv2.waitKey()