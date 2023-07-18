import aspose.pdf as ap

alturapag = 641
largurapag = 1072

iniciox = 177
inicioy = 485
finalx = 407
finaly = 700

#Rectangle(left, bottom, width, height)
left = iniciox
bottom = alturapag - finaly
width = finalx - iniciox
height = (alturapag - inicioy) - bottom

# Carregar arquivo PDF
document = ap.Document("balinhacom.pdf")

# Criar um novo retângulo
newBox = ap.Rectangle(left, bottom, width, height, True)

# Modifique o tamanho da primeira página em PDF
document.pages[1].crop_box = newBox
document.pages[1].trim_box = newBox
document.pages[1].art_box = newBox
document.pages[1].bleed_box = newBox

# Salve o PDF atualizado
document.save("cropped.pdf")
print (left, bottom, width, height)
