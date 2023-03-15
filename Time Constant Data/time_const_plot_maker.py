import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from statistics import NormalDist

filename = 'dat_150k.txt'
counts = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=int)

low_limiter = 15
bin_count = 25

#eliminate data below low_limiter
count_prime = []
for count in counts:
    if count>=low_limiter:
        count_prime.append(count)

#make log histogram
n, bins, patches = plt.hist(count_prime, bin_count, facecolor='r', log=True, alpha=0.75)

#get histogram points with bin_count number of bins
ax = plt.gca()
p = ax.patches
p[0].get_xy()
p[0].get_width()
p[0].get_height()
heights = [patch.get_height() for patch in p]
print(heights)

#linear regression
Y = []
for h in heights:
    if h==0:
        Y.append(0)
    else:
        Y.append(np.log(h))
        
X = []
for i in range(len(Y)):
    X.append(i)

#x_1 = 0
#x_2 = 1.2

coef = np.polyfit(X, Y, 1)
poly1d_fn = np.poly1d(coef)
print(coef)

plt.xlabel('Time between counts')
plt.ylabel('Counts')
plt.title('Pulsewidth in milliseconds')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
