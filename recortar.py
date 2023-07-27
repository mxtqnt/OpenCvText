# Recebe PDF de encontrarcontornos.py
# Salva PDF recorte.pdf
import cv2
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from conversor import pdf_para_png

def recortar_parafo(x, y, w, h):
    print('Recortando com cordenadas')
    reader = PdfReader("embalagem.pdf") # Receber de app.py
    writer = PdfWriter()

    page = reader.pages[0]
    sourcepage = reader.pages[0]

    # Pegar tamanho PDF
    pdfw = sourcepage.mediabox.width
    pdfh = sourcepage.mediabox.height

    # Tamanhos do OpenCV
    embalagem = cv2.imread('embalagem.png')
    cvh, cvw, c = embalagem.shape

    # Cordenadas OpenCV
    cvx1 = x
    cvy1 = y
    cvx2 = x + w
    cvy2 = y + h

    # Cordenadas PDF
    pdfx1 = ((pdfw*cvx1)/cvw)
    pdfy1 = ((pdfh*cvy1)/cvh)
    pdfx2 = ((pdfw*cvx2)/cvw)
    pdfy2 = ((pdfh*cvy2)/cvh)

    reader = PdfReader('embalagem.pdf')
    page = reader.pages[0]
    sourcepage = reader.pages[0]
    
    # Definir área de corte
    page.cropbox = RectangleObject((pdfx1, (pdfh - pdfy1), pdfx2, (pdfh - pdfy2)))

    # Armazenar novo PDF
    writer.add_page(reader.pages[0])
    with open("recorte.pdf", "wb") as fp:
        writer.write(fp)
