import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from statistics import NormalDist

def sig_m(x,y,cf):
    s = len(x)
    m = cf[0]
    c = cf[1]
    sqdev = 0
    sum_x = 0
    sum_xx = 0
    
    for i in range(s):
        sqdev += (y[i]-m*x[i]-c)**2
        sum_x += x[i]
        sum_xx += (x[i])**2
    sig_y = (sqdev/(s-1))**0.5
    delta = s*sum_xx - (sum_x)**2
    sig_m = sig_y*(s/delta)**0.5
    
    return sig_m

f_list = ['dat_150k.txt', 'dat_300k.txt', 'dat_450k.txt', 'dat_600k.txt', 'dat_750k.txt']

for file in f_list:
    counts = np.loadtxt(file, delimiter=',', skiprows=1, dtype=int)
    avg_count = sum(counts)/len(counts)
    print(avg_count)
    print(np.std(counts))

Y = [7.4671, 9.4232, 11.0942, 13.1648, 15.6163]
X = [150, 300, 450, 600, 750]

x_1 = 50
x_2 = 900

coef = np.polyfit(X, Y, 1)
poly1d_fn = np.poly1d(coef)

err = sig_m(X,Y,coef)

plt.scatter(X, Y, label='Data points', color='black', zorder=3)
plt.plot([x_1,x_2], [coef[0]*x_1+coef[1],coef[0]*x_2+coef[1]],'--k', linewidth=1, label='Best fit line', color='black', zorder=2)
plt.text(100, 14, 'y = 0.01336x + 5.34112') #, rotation=35)

print(coef)

plt.xlabel('Resistance in kOhm')
plt.ylabel('Average pulsewidth')
plt.title('Pulsewidth variation with quenching resistance')
plt.grid(True)
plt.show()
