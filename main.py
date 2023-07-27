from conversor import pdf_para_png
from contornar import encontrar_contornos

embalagempdf = 'embalagem.pdf'
open('resultado.txt', 'w').close()

if __name__ == '__main__':
    print('Iniciando...')
    pdf_para_png(embalagempdf, 'embalagem') # Cria embalagem.png
    encontrar_contornos()
