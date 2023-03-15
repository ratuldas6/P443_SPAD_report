import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from statistics import NormalDist

filename = 'dat_600k.txt'
counts = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=int)

low_limiter = 25
bin_count = 20

#eliminate data below low_limiter
count_prime = []
for count in counts:
    if count>=low_limiter:
        count_prime.append(count)

#make log histogram
n, bins, patches = plt.hist(count_prime, bin_count, facecolor='r', alpha=0.75)

#get histogram points with bin_count number of bins
ax = plt.gca()
p = ax.patches
p[0].get_xy()
p[0].get_width()
p[0].get_height()
heights = [patch.get_height() for patch in p]

#linear regression
Y = []
for h in heights:
    if h==0:
        Y.append(0)
    else:
        Y.append(np.log(h))
print(Y)

X = []
for i in range(len(Y)):
    X.append(i)
print(X)

plt.xlabel('Time between counts')
plt.ylabel('Counts')
plt.title('Counts vs Time between counts for 600k' + r'$\Omega$')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
