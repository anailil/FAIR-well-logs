# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:40:09 2022

@author: obandohe
"""

import numpy as np
import matplotlib.pyplot as plt
import os


#path=r"..\data\raw\"  # Replace by appropiate directory 
#os.chdir(path)

import las_reader

a = las_reader.readlas3('../data/raw/DAPGEO-02_500m_PHASE3_FWS.las')
b = a.readdata()

def smooth(y, box_pts):
    'function to smooth data points based on convolution. \
    Uses numpy.concolve.\
    Returns an array of the smoothed function. box_pts = the \
    amount of points used. Recommended = 1 m. Used to smooth gamma\
    ray measurements'
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


depth = b["LOG_DEFINITION[21]"]["DEPTH"][1]

#dz = np.diff(depth)


indx_name1 = ["RX1-1A"+"["+str(ii+1)+"]" for ii in range(0,1000)]
indx_name2 = ["RX2-1A"+"["+str(ii+1)+"]" for ii in range(0,1000)]
indx_name3 = ["RX3-1A"+"["+str(ii+1)+"]" for ii in range(0,1000)]


signals_RX01 = np.zeros((1000,3945))
signals_RX02 = np.zeros((1000,3945))
signals_RX03 = np.zeros((1000,3945))


iz = 0

while iz < 1000:
    

    signals_RX01[iz,:] = b["LOG_DEFINITION[109]"][indx_name1[iz]][1]
    signals_RX02[iz,:] = b["LOG_DEFINITION[110]"][indx_name2[iz]][1]
    signals_RX03[iz,:] = b["LOG_DEFINITION[111]"][indx_name3[iz]][1]
    
    
    iz+=1
    
dt = 4/1e6
fs = 1/dt

time = np.arange(0,1000)*dt*1000

#%%

fig, (ax0,ax1,ax2) = plt.subplots(3,1,figsize=(18,12))

index = 20 # Index according to the disired depth

ax0.plot(time,signals_RX01[:,index],label='RX01',color='red')
ax0.set_xlabel('Time[ms]',fontsize=14)
ax0.set_ylabel('Amplitude',fontsize=14)
ax0.set_title('Depth = ' + str(depth[index])+' m',fontsize=14)
ax0.set_xlim(0,2.0)
ax0.legend()
ax0.grid()

ax1.plot(time,signals_RX02[:,index],label='RX02',color='darkblue')
ax1.set_xlabel('Time[ms]',fontsize=14)
ax1.set_ylabel('Amplitude',fontsize=14)
ax1.set_xlim(0,2.0)
ax1.legend()
ax1.grid()

ax2.plot(time,signals_RX03[:,index],label='RX03',color='darkgreen')
ax2.set_xlabel('Time[ms]',fontsize=14)
ax2.set_ylabel('Amplitude',fontsize=14)
ax2.set_xlim(0,2.0)
ax2.legend()
ax2.grid()

plt.tight_layout()

#%%






