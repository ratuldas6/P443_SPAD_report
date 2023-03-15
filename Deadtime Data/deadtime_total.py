import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

X = [150, 300, 450, 600]
Y = [2.94, 1.32, 1.43, 2.25]

plt.plot(X, Y, color='g', marker='o', zorder=3)

plt.xlabel('Quenching resistance (in kOhm)')
plt.ylabel('Time constant (in ms)')
plt.title('Variation of dead time with quenching resistance')
plt.grid(True)
plt.show()
