# To-Do
# Make a function to plot well logs.

f0, ax1 = plt.subplots(figsize=(16,16))
#curve_names = ['Gamma', 'Deep Res', 'Density', 'Neutron']
#Set up the plot axes
ax1 = plt.subplot2grid((1,4), (0,0), rowspan=1, colspan = 1) 
ax2 = plt.subplot2grid((1,4), (0,1), rowspan=1, colspan = 1)
#ax3 = plt.subplot2grid((1,4), (0,2), rowspan=1, colspan = 1)
#ax4 = plt.subplot2grid((1,4), (0,3), rowspan=1, colspan = 1)
ax3 = ax2.twiny()
ax4 = ax2.twiny()

#Set up the individual log tracks / subplots

#ax1.plot(p2_kut['GR.API'], p2_kut['DEPTH.M'], color = "red", lw = 0.5)
ax1.plot(p2_kut['GR.API'], p2_kut['DEPTH.M'], color = "red", lw = 0.5)
ax1.set_xlim(0, 200)
ax1.set_xlabel('GR (API)')

ax2.plot(k, p2_kut['DEPTH.M'], color = "red", lw = 0.5)
ax2.set_xlim(0, 5)
ax2.set_xlabel('K (%)')

ax3.plot(u, p2_kut['DEPTH.M'], color = "green", lw = 0.5)
ax3.set_xlim(0, 20)
ax3.set_xlabel('U (PPM)')

ax4.plot(t, p2_kut['DEPTH.M'], color = "blue", lw = 0.5)
ax4.set_xlim(0, 20)
ax4.set_xlabel('TH (PPM)')

#Set up the common elements between the subplots
for i, ax in enumerate(f0.axes):
    #ax.set_ylim(0, 250) # Set the depth range
    
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    
    if i >= 2:
        ax.spines["top"].set_position(("axes", 0.96+(i/20)))
    else:
        ax.grid()

#Hide tick labels on the y-axis 
for ax in [ax2, ax3, ax4]:
    plt.setp(ax.get_yticklabels(), visible = False)

#Reduce the space between each subplot
f0.subplots_adjust(wspace = 0.05)