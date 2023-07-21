
# OpenCvText
#### **Validação automática de embalagens.**
Usando visão computacional e inteligência artificial para validar embalagens de produtos.

_Nota: A imagem de exemplo NÃO é uma embalagem real por segurança._



## **Overview**

#### Imagem para testes:
![](https://github.com/mxtqnt/OpenCvText/blob/main/testes.PNG?raw=true)

#### **Fases do projeto:**
* Encontrar parágrafos;
    
* Fazer o fatiamento;
* Normalizar alinhamento;
* Aplicar o reconhecimento de caracteres;
* Identificar erros;
* Desenvolver interface para uso.


## Encontrar parágrafos
Primeiro fazemos o tratamento de imagem:
```bash
gray = cv2.cvtColor(pngcompleto, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
```
Depois a dilatação pra enfim encontrar os contornos:
```bash
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh, kernel, iterations=4)
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
```
![](https://github.com/mxtqnt/OpenCvText/blob/main/imgreadme/tratamento.png?raw=true)

## Resultado:
![](https://github.com/mxtqnt/OpenCvText/blob/main/imgreadme/resultado.png?raw=true)

## Fazer o fatiamento
Nessa parte fiz o fatiamento do arquivo PDF com base na normalização das cordenadas dos parágrafos, assim não perdi a qualidade da imagem melhorando o desempenho da leitura pelo EasyOCR.

**Passado pelo EasyOCR:**

```bash
Using CPU. Note: This module is much faster with a GPU.
No mundo atual, a adoção de políticas descentralizadoras talvez venha a ressaltar a relatividade do remanejamento dos quadros funcionais. (08 182)
```
## Tecnologias
**Linguagem:** Python.

**Bibliotecas:** OpenCV, EasyOCR, PyPDF e Pdf2Image.

**API:** Google Sheets.

