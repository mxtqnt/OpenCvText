import pdf2image

poppler_path = r'C:\Users\ana.santos\Documents\poppler-23.07.0'

# Store Pdf with convert_from_path function
images = pdf2image.convert_from_path('_cropped.pdf', use_cropbox=True)
 
print(type(images))
images[0].save('paragrafo' + '.png', 'PNG')