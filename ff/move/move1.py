'''
Created on 2019/12/11

UIのデモ映像をgifで表示するプログラム

@author: Kai_Kudo
'''
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as anime
import numpy as np

im_menu = Image.open('../menu2.png')
im_frame = Image.open('../frame.png')
im_back = Image.open('../back.png').resize(im_menu.size)
im_square = Image.new('RGBA', im_menu.size, (255,255,255,0))
im_square2 = Image.new('RGBA', im_menu.size, (255,255,255,0))
im_square3 = Image.new('RGBA', im_menu.size, (255,255,255,0))
im_square_temp = Image.open('../square.png')
im_square.paste(im_square_temp)
im_square2_temp = Image.open('../square2.png')
im_square2.paste(im_square2_temp)
im_square3_temp = Image.open('../square3.png')
im_square3.paste(im_square3_temp)
width, height = im_menu.size

phase1, phase2, phase3, phase4, phase_max = (30, 40, 50, 70, 100)

fig = plt.figure()
idol_place = [[70, 150], [190, 150], [310, 150], [430, 150], [550, 150]]
im_back_ani = []
im_idol = []
for i in range(5):
    im_idol.append(Image.open(f'../idol{i+1}.png'))
    
for num in range(0,phase_max):
    im_back2 = im_back.copy()
    for i in [1,3,2,0,4]:
        idol_place[i][0] += int(np.random.normal(scale=5))
        if i<2:
            idol_place[i][1] += int(np.random.normal(scale=5+i*10))
        im_back2.paste(im_idol[i], tuple(idol_place[i]), im_idol[i])
        print(idol_place[i])
    #顔の四角
    if phase2+1<=num<phase3+1:
        im_back2.paste(im_square, tuple(idol_place[0]), im_square)
    elif phase3+1<=num:
        im_back2.paste(im_square, tuple(idol_place[4]), im_square)
    if num<20:
        im_back2_big = im_back2.resize((width*(num+20)//20, height*(num+20)//20))
    else:
        im_back2_big = im_back2.resize((width*2, height*2))
    x, y = im_back2_big.size
    #ライブの切り出し
    if num<phase2+1:
        im_back2_cut = im_back2_big.crop(((x-width)//2,(y-height)//2,(x+width)//2,(y+height)//2))
    elif num<phase3+1:
        x1 = 10*idol_place[0][0]//4+200
        y1 = 10*idol_place[0][1]//4+500
        im_back2_cut = im_back2_big.crop(((x1-width)//2,(y1-height)//2,(x1+width)//2,(y1+height)//2))
    elif phase3+1<=num:
        x1 = 14*idol_place[4][0]//4+400
        y1 = 14*idol_place[4][1]//4+500
        im_back2_cut = im_back2_big.crop(((x1-width)//2,(y1-height)//2,(x1+width)//2,(y1+height)//2))
            
    if num<phase1:
        im_result = im_back2_cut
    else:
        im_menu2 = im_menu.copy()
        #モードの四角
        if num<=phase4:
            im_menu2.paste(im_back2_cut.resize((width*3//5, height*3//5)))
        else:
            im_back2_mode2 = im_back2_big.crop(((x-width)//2,(y-height)//2,(x+width)//2,(y+height)//2))
            im_back2_mode2.paste(im_frame.resize((width//2, height//2)),(width//2, 0))
            im_back2_mode2.paste(im_back2_cut.resize((width//2-8, height//2-8)), (width//2+4, 3))
            im_menu2.paste(im_back2_mode2.resize((width*3//5, height*3//5)))
            
        if num<phase4:
            im_menu2.paste(im_square3, (25, 368), im_square3)
        else:
            im_menu2.paste(im_square3, (165, 368), im_square3)
            
        #名前の四角
        if phase2<=num<phase3:   
            im_menu2.paste(im_square2, (480,85), im_square2)
        elif phase3<=num:
            im_menu2.paste(im_square2, (480,415), im_square2)
        im_result = im_menu2
    img = plt.imshow(im_result, animated=True)
    im_back_ani.append([img])

ani = anime.ArtistAnimation(fig, im_back_ani, interval=400)
plt.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)
ani.save("../mikke4.gif", writer='pillow')
plt.show()
#'''
