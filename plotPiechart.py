# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:35:44 2015
plot pie chart
@author: zimu
"""

import matplotlib.pyplot as plt

chart = 4

if chart == 0:
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    
    plt.show()
elif chart == 1:
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Covered Results', 'Uncovered Results'
    sizes = [90.476, 9.524]
    colors = ['yellowgreen','orange']
    explode = (0.1, 0) # only "explode" the 1st slice
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=-90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    
    plt.rcParams['axes.labelsize'] = 50
    plt.rcParams['font.size'] = 50
    #print plt.rcParams.keys() #if you do not know what parameters will work
    
    plt.show()
elif chart == 2:
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Covered Results', 'Uncovered Results'
    sizes = [57.143, 42.857]
    colors = ['yellowgreen','orange']
    explode = (0.1, 0) # only "explode" the 1st slice
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=-10)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    
    plt.rcParams['axes.labelsize'] = 50
    plt.rcParams['font.size'] = 50
    #print plt.rcParams.keys() #if you do not know what parameters will work
    
    plt.show()
elif chart == 3:#Probabilities - the exact number of group that a zone is contained in (totally 8 groups).
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Only 1 group', '2 groups', '3 groups', '4 groups', '5 groups'
    sizes = [15.625,31.25,31.25,15.625,6.25]
    colors = ['grey','yellowgreen','orange','yellow','pink']
    explode = (0.3, 0,0,0,0) # only "explode" the 1st slice
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=-80)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    #plt.title('The exact number of group that layers are contained in')
    plt.rcParams['axes.labelsize'] = 50
    plt.rcParams['font.size'] = 50
    #print plt.rcParams.keys() #if you do not know what parameters will work
    
    plt.show()
elif chart == 4:
     # The slices will be ordered and plotted counter-clockwise.
    labels = 'Not overlap', 'Overlap'
    sizes = [15.625, 84.375]
    colors = ['grey','orange']
    explode = (0.3, 0) # only "explode" the 1st slice
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=-80)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    
    plt.rcParams['axes.labelsize'] = 50
    plt.rcParams['font.size'] = 50
    #print plt.rcParams.keys() #if you do not know what parameters will work
    
    plt.show()