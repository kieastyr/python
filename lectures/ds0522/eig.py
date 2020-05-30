import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

data = [[173, 69, 85],
		[163, 64, 83],
		[165, 55, 63],
		[161, 57, 88],
		[171, 71, 76],
		[165, 51, 90],
		[180, 63, 89],
		[182, 72, 69]]
		
npdata = np.array(data)
s = np.corrcoef(npdata.transpose())
print(np.cov(npdata.transpose()))
print(s)
w, v = LA.eig(s)
print(w)
print(v)
new = np.zeros((8,3))
for i in range(8):
	new[i,0] = np.dot(npdata[i,:],v[0,:])
	new[i,1] = np.dot(npdata[i,:],v[2,:])
	new[i,2] = np.dot(npdata[i,:],v[1,:])
	
print(new)

plt.scatter(new[:,0],new[:,1])
plt.show()
plt.scatter(new[:,0],new[:,2])
plt.show()