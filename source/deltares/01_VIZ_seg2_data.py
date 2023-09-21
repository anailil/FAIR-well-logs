# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:36:10 2022

@author: obandohe
"""

import os
import glob
import numpy as np
import matplotlib.pylab as plt
path = r'G:\DAP_SURVEY\RESULTS\RAW_DATA'  # Replace by appropiate directory
os.chdir(path) 
import read_seg2
seg2files=glob.glob('.\PS_LOGGING\*.SG2')


ik = 1
segfile = seg2files[ik]
#print(segfile)
# Search for all tdms files contained in the directory.    
st=read_seg2._read_seg2(segfile)
print(st)

Rec_name = {}
fs = np.zeros(6)
n_samples = np.zeros(6)
time = {}
data = {}

ii = 0

while ii < 6:

    Rec_name[ii] = st[ii].stats.seg2.RECEIVER
    fs[ii] = st[ii].stats.sampling_rate
    n_samples[ii] = st[ii].stats.npts
    time[ii] = np.arange(0,st[ii].stats.npts)/st[ii].stats.sampling_rate*1000
    data[ii] = st[ii].data
    depth = float(round(float((st[ii].stats.seg2.RECEIVER_LOCATION)[16:23].replace(',','.')),2))

    ii+=1

#%%

P_near = data[0]
P_far = data[1]

S_near_r = data[2]
S_near_l = data[4]

S_far_r = data[3]
S_far_l = data[5]

fig, (ax0,ax1,ax2) = plt.subplots(3,1,figsize=(12,8))

ax0.plot(time[0],P_near,label=Rec_name[0],color='darkblue')
ax0.plot(time[1],P_far,label=Rec_name[1],color='orange')
ax0.set_xlabel('Time[ms]',fontsize=14)
ax0.set_ylabel('Amplitude',fontsize=14)
ax0.set_title(segfile + ' -- Depth ='+str(depth) + "m",fontsize=14)
ax0.legend(loc='upper right')
ax0.grid()

ax1.plot(time[2],S_near_r,label=Rec_name[2],color='darkblue')
ax1.plot(time[4],S_near_l,label=Rec_name[4],color='orange')
ax1.set_xlabel('Time[ms]',fontsize=14)
ax1.set_ylabel('Amplitude',fontsize=14)
ax1.legend(loc='upper right')
ax1.grid()

ax2.plot(time[3],S_far_r,label=Rec_name[3],color='darkblue')
ax2.plot(time[5],S_far_l,label=Rec_name[5],color='orange')
ax2.set_xlabel('Time[ms]',fontsize=14)
ax2.set_ylabel('Amplitude',fontsize=14)
ax2.legend(loc='upper right')
ax2.grid()
plt.tight_layout()

