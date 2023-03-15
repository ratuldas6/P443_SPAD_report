import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from statistics import NormalDist

Y = [7.891704659330107, 7.589335823170617, 7.00033446027523, 6.42648845745769, 5.834810737062605, 5.267858159063328, 4.919980925828125, 4.343805421853684, 3.6888794541139363, 3.4657359027997265, 3.1780538303479458, 2.772588722239781, 2.1972245773362196, 1.9459101490553132, 1.3862943611198906, 1.791759469228055]
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

x_1 = -0.5
x_2 = 15.5

coef = np.polyfit(X, Y, 1)
poly1d_fn = np.poly1d(coef)
print(coef)

plt.xlabel('Bin number in histogram')
plt.ylabel('log(Counts)')
plt.title('Log(Counts) vs Time between counts for 600 k' + r'$\Omega$')
plt.scatter(X,Y)
plt.plot([x_1,x_2], [coef[0]*x_1+coef[1],coef[0]*x_2+coef[1]],'--k', linewidth=1, label='Best fit line', color='black', zorder=2)
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
plt.text(4.5, 6, 'log(y) = -0.4451x + 7.6949') #, rotation=35)
plt.grid(True)
plt.show()
