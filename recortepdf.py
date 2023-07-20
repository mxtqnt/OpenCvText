from pypdf import PdfWriter, PdfReader
from pypdf.generic import RectangleObject

reader = PdfReader("balinhacompleta.pdf")
writer = PdfWriter()

page = reader.pages[0]
sourcepage = reader.pages[0]

# Pegar tamanho PDF
pdfw = sourcepage.mediabox.width
pdfh = sourcepage.mediabox.height

# Tamanhos do OpenCV
cvw = 1072
cvh = 641

# Cordenadas OpenCV
cvx1 = 267
cvy1 = 567
cvx2 = 458
cvy2 = 635

# Cordenadas PDF
pdfx1 = ((pdfw*cvx1)/cvw)
pdfy1 = ((pdfh*cvy1)/cvh)
pdfx2 = ((pdfw*cvx2)/cvw)
pdfy2 = ((pdfh*cvy2)/cvh)

# Definir área de corte
page.cropbox = RectangleObject((pdfx1, (pdfh - pdfy1), pdfx2, (pdfh - pdfy2)))

# Armazenar novo PDF
writer.add_page(reader.pages[0])
with open("cropped.pdf", "wb") as fp:
    writer.write(fp)