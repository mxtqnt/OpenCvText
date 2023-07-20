import aspose.pdf as ap

alturapag = 641
largurapag = 1072

iniciox = 296
inicioy = 234
finalx = 374
finaly = 258

#Rectangle(left, bottom, width, height)
left = iniciox
bottom = (alturapag - finaly) - 30
width = (finalx - iniciox) - 60
height = ((alturapag - inicioy) - (alturapag - finaly)) + 30

# Carregar arquivo PDF
document = ap.Document("balinhacompleta.pdf")

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
