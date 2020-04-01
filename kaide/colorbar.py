'''
Created on 2019/08/03

@author: Kai_Kudo
'''
import matplotlib.pyplot as plt
import numpy as np

red = np.array([0, 0, 103, 28, 115, 81, 160, 199, 255, 210, 255, 199, 255, 255, 157, 216], dtype=float)
green = np.array([131, 0, 26, 59, 115, 183, 160, 255, 255, 224, 255, 255, 131, 0, 0, 175], dtype=float)
blue = np.array([25, 0, 192, 207, 115, 166, 160, 116, 255, 191, 0, 116, 112, 0, 255, 255], dtype=float)
x0 = np.array([-8148, -6500, -5000, -3750, -2750, -2000, -1250, -750, -250, 250, 1000, 1750, 2750, 4000, 5500, 7093], dtype=float)

# plt.plot(x0, red, color="r")
# plt.plot(x0, green, color="g")
# plt.plot(x0, blue, color="b")
# plt.show()
num_r = 10
x_r = np.stack([np.power(x0,10), np.power(x0,9), np.power(x0,8), np.power(x0,7), np.power(x0,6), np.power(x0,5), np.power(x0,4), np.power(x0,3), np.power(x0,2), np.power(x0,1), np.power(x0,0)])
b_r = np.linalg.inv(x_r@x_r.T)@x_r@red.T 
num_g = 8
x_g = np.stack([np.power(x0,8), np.power(x0,7), np.power(x0,6), np.power(x0,5), np.power(x0,4), np.power(x0,3), np.power(x0,2), np.power(x0,1), np.power(x0,0)])
b_g = np.linalg.inv(x_g@x_g.T)@x_g@green.T
num_b = 9
x_b = np.stack([np.power(x0,9), np.power(x0,8), np.power(x0,7), np.power(x0,6), np.power(x0,5), np.power(x0,4), np.power(x0,3), np.power(x0,2), np.power(x0,1), np.power(x0,0)])
b_b = np.linalg.inv(x_b@x_b.T)@x_b@blue.T 

x1 = np.linspace(-8148, 7093, 1000)
y1_r = np.sum([b_r[i]*np.power(x1,num_r-i) for i in range(num_r+1)], axis=0)
y1_g = np.sum([b_g[i]*np.power(x1,num_g-i) for i in range(num_g+1)], axis=0)
y1_b = np.sum([b_b[i]*np.power(x1,num_b-i) for i in range(num_b+1)], axis=0)

print(f"red_param:{b_r}")
print(f"red_param:{b_g}")
print(f"red_param:{b_b}")

plt.plot(x1, y1_r, color="r")
plt.plot(x1, y1_g, color="g")
plt.plot(x1, y1_b, color="b")
plt.ylim([0,255])
plt.show()