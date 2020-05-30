import numpy as np

data = np.array([[161, 163, 165, 173, 182, 180, 165, 171],
	[58, 63, 51, 69, 75, 63, 56, 70]])

x = np.array([np.ones(8,), data[0], data[0]**2]).T
y = data[1].T

a = np.linalg.inv(x.T@(x))@(x.T)@(y)
print(a)

res = y-(a[0]+a[1]*data[0]+a[2]*data[0]**2)
sigma = np.std(res)

z = np.mean(res)/(sigma/np.sqrt(8))
print(z)