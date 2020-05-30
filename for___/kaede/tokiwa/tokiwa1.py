'''
Created on 2018/10/08

@author: Kai_Kudo
'''

from PIL import Image as im
image = im.open('tokiwa.jpg')
size = image.size
new_image = im.new("RGB",size)
a = 256//4
for x in range(size[0]):
    rate = int(x/size[0]*100)+1
    print(f'{rate}%dane!')
    for y in range(size[1]):
        r, g, b = image.getpixel((x,y))
        r = a*(r//a)
        g = a*(g//a)
        b = a*(b//a)
        new_image.putpixel((x,y), (r,g,b))

new_image.save('tokiwa1.jpg')