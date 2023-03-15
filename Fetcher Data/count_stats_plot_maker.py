import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from scipy.optimize import curve_fit

#gaussian definition
G = lambda x,A,sigma,mu: A*np.exp(-(x-mu)**2/sigma)

#file import
filename = 'fetch_dat_1.txt'
counts = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=int)

n, bins, patches = plt.hist(counts, 13, facecolor='r', alpha=0.75)

ax = plt.gca()
p = ax.patches
p[0].get_xy()
p[0].get_width()
p[0].get_height()
heights = [patch.get_height() for patch in p]
print(heights)

binlist = []
for i in range(len(heights)):
    binlist.append(i)

x=np.array(binlist)
y=np.array(heights)
parameters,covariance=curve_fit(G,x,y) #p0=[10,2,0]

A = parameters[0]
sigma = parameters[1]
mu = parameters[2]

fit_x=np.arange(x[0],x[-1],0.01)
fit_y=G(fit_x,A,sigma,mu)

plt.scatter(fit_x,fit_y,label='Best fit')

print('sigma=',sigma)
print('mu=',mu)

plt.show()

'''
plt.xlabel('Counts')
plt.ylabel('Frequency of counts')
plt.title('Histogram of 20ms data in ambient light')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
'''
