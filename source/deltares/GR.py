# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:32:57 2022

@author: loesv
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import pylab
import pandas as pd
import csv

log = pd.read_excel(r'C:\Users\loesv\OneDrive\Bureaublad\BEP\LAS_final.xlsx')

### SHALE VOLUME ###
# define minimum and maximum depth for plotting
minimum_depth = min(log['DEPT[M]'])
maximum_depth = max(log['DEPT[M]'])

# define the linewidth
lw = 0.8

# define the figure size (width, height, in [cm])
plt.rcParams['figure.figsize'] = [10, 20]

# make a figure consisting of 6 subplots that share the depth axis (y)
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.set_ylim(maximum_depth, minimum_depth)

# plot the 4 methods + combined
ax1.plot(log['K'],log['DEPT[M]'],linewidth=lw, color = "red")
ax1.plot(log['U'],log['DEPT[M]'],linewidth=lw, color = "blue")
ax1.plot(log['TH'],log['DEPT[M]'],linewidth=lw, color = "green")
ax1.grid(which='minor', color='#EEEEEE', linewidth=1)
ax1.minorticks_on()
ax1.grid()
ax1.set_title('Clay bound water')
ax1.set_xlabel('%')
ax1.set_ylabel('depth [m]')

ax2.plot(log['GR'],log['DEPT[M]'],linewidth=lw, color = "black")
ax2.grid(which='minor', color='#EEEEEE', linewidth=1)
ax2.minorticks_on()
ax2.grid()
ax2.set_title('Moveable water')
ax2.set_xlabel('%')
ax2.set_ylabel('depth [m]')

GR = log['GR']

GR_max = max(GR)
GR_min = min(GR)

VSh = np.zeros(len(GR))
for i in range(len(GR)):
    VSh[i] = (GR[i] - GR_min)/(GR_max - GR_min)
print(VSh)

ax3.plot(VSh,log['DEPT[M]'],linewidth=lw, color = "darkorange")
ax3.grid(which='minor', color='#EEEEEE', linewidth=1)
ax3.minorticks_on()
ax3.grid()
ax3.set_title('Moveable water')
ax3.set_xlabel('%')
ax3.set_ylabel('depth [m]')
