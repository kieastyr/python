import numpy as np
import matplotlib.pyplot as plt

def cm_moon(img):
    red_coeff =  [-1.64903754e-36, -2.81699625e-32,  7.24868536e-28,  5.20894510e-24, -6.17439033e-20, -2.52087872e-16,  1.82008814e-12,  3.15384582e-09, -2.05473014e-05,  1.97587418e-02,  2.28442477e+02]
    green_coeff = [-1.91231585e-28, -1.87006898e-24,  1.49660342e-20,  1.80884460e-16,  1.19408928e-14, -4.76772607e-09, -1.70751518e-05,  3.02167011e-02,  2.51984061e+02]
    blue_coeff = [-1.79232104e-31, -7.10519519e-28,  1.66525626e-23,  4.84614854e-20, -4.41751965e-16, -6.45627798e-13,  4.15638445e-09, -2.52220696e-06, -2.81728902e-02,  1.48304915e+02]
    
    img_red = np.sum([coeff*np.power(img,i) for i,coeff in enumerate(reversed(red_coeff))], axis=0)
    img_green = np.sum([coeff*np.power(img,i) for i,coeff in enumerate(reversed(green_coeff))], axis=0)
    img_blue = np.sum([coeff*np.power(img,i) for i,coeff in enumerate(reversed(blue_coeff))], axis=0)
    
    img_red = np.where(img_red<0, 0, img_red)
    img_red = np.where(img_red>255, 255, img_red)
    img_green = np.where(img_green<0, 0, img_green)
    img_green = np.where(img_green>255, 255, img_green)
    img_blue = np.where(img_blue<0, 0, img_blue)
    img_blue = np.where(img_blue>255, 255, img_blue)
    
    return np.array([img_red, img_green, img_blue]).T

x = np.linspace(-8148, 7093, 1000)
ones = np.ones([100,1000,3])
img = cm_moon(x)[np.newaxis,:,:]*ones
print(img.shape)
plt.imshow(img.astype(int), extent=[-8148, 7093, 0, 1000])
plt.show()
