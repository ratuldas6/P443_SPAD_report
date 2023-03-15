import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from scipy.optimize import curve_fit
from scipy.special import factorial

def func(X,C,X_mean,sigma):
    return C*np.exp(-(X-X_mean)**2/(2*sigma**2))

def poisson(k, lamb, scale):
    return scale*(lamb**(k)/factorial(k))*np.exp(-lamb)

filename = 'fetch_dat_3_200ms.txt'
counts = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=int)
n, bins, patches = plt.hist(counts, 20, alpha=0.75)

bin_heights, bin_borders, _ = plt.hist(counts, 20, facecolor='b', alpha=0.75)
bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
popt1, _ = curve_fit(func, bin_centers, bin_heights,[400,4400,10])

x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
plt.plot(x_interval_for_fit, func(x_interval_for_fit, *popt1), label='Gaussian fit')
#plt.plot(x_interval_for_fit, poisson(x_interval_for_fit, *par), label='Poisson fit')
plt.legend()
plt.xlabel('No. of incident counts')
plt.ylabel('Frequency of Counts')
plt.title('Histogram of counts taken for 200ms window')
plt.text(4325, 350, 'y = 394.06exp[' + r'$\frac{(x-4478.19)}{34.08^2}$' + ']') #, rotation=35)
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
print(popt1)
print(bin_centers,bin_heights)
print(np.mean(counts))
print(_)
