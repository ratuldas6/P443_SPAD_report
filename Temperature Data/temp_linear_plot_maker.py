import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

temps = [25, 32, 39, 46, 53, 60, 67]
peaks = [4330, 4800, 5070, 5240, 5520, 5810, 6050]

x_1 = 20
x_2 = 80

coef = np.polyfit(temps, peaks, 1)
poly1d_fn = np.poly1d(coef)

print(coef)

plt.scatter(temps, peaks, label='Data points', color='black', zorder=3)
plt.plot([x_1,x_2], [coef[0]*x_1+coef[1],coef[0]*x_2+coef[1]],'--k', linewidth=1, label='Best fit line', color='black', zorder=2)

plt.title('Peak dark count plot with temperature')
plt.xlabel('Temp (in ' + r'$^\circ$' + 'C)')
plt.ylabel('Peak Count')
#leg = plt.legend()
#plt.legend(loc='upper left',shadow=True)
plt.text(25, 6000, 'y = 38.93x + 3469.29') #, rotation=35)
plt.grid(zorder=1)
plt.show()
