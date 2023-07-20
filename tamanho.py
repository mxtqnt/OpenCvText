import PIL 
from PIL import Image 
img = PIL.Image.open("balinhacompleta.png") 
wid, hgt = img.size 
print(str(wid) + "x" + str(hgt))