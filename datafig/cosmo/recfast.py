import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import quad

x49=np.loadtxt("/Users/daubert/Project/cosmo/om49.dat")
x10=np.loadtxt("/Users/daubert/Project/cosmo/om10.dat")
x100=np.loadtxt("/Users/daubert/Project/cosmo/om100.dat")

plt.plot(x49[:,0],x49[:,1])
plt.plot(x10[:,0],x10[:,1])
plt.plot(x100[:,0],x100[:,1])
plt.legend(['ob=0.049','ob=0.01','ob=0.1'],loc=4)
plt.yscale('log')
plt.xlabel('redshift z')
plt.ylabel('x_e')
plt.show()