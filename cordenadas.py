import cv2

im = cv2.imread('balinhacompleta.png')

print(type(im))
print(im.shape)
print(type(im.shape))
h, w, c = im.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)
h, w, _ = im.shape
print('width: ', w)
print('height:', h)
print('width: ', im.shape[1])
print('height:', im.shape[0])
print(im.shape[1::-1])