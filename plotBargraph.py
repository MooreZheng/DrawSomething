# -*- coding: utf-8 -*-
"""
Created on Tue May 05 20:39:51 2015
plot bargraph
@author: zimu
"""
import scipy.stats
import numpy as np  
import matplotlib.pyplot as plt  
 
graph = 15
xfontsize = 60
yfontsize = 60
xlabelsize = 70
ylabelsize = 70
legendsize = 60
if graph == 14:#Fine-grained on floors without RFE, RFE 25% - 
#MSE of TPO-P without and with RFE.
    n_groups = 2
    mse = (2.85442982136, 2.67743721074)
    #mse = (9.22276195083, 2.67743721074)
    #Total, random 10, random 30, RFE 25%
#    n_groups = 4
#    mse = (2.85442982136, 2.91546933629, 2.82799128194, 2.67743721074)
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.3  
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(xfontsize)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(yfontsize)    
    plt.xlabel('Algorithms',size=xlabelsize)  
    plt.ylabel('Mean MSE', size=ylabelsize)  
    plt.xticks(0.55+ index + bar_width, ('TPO-P \n(without RFE)','TPO-P'))  
    plt.xlim(0,3)
    plt.ylim(2.5,3)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':legendsize})   
    #plt.tight_layout()  
    plt.show()
elif graph == 15:#overview 2a - different training time
    #TFO-P: Mean MSE as a function of training length
    n_groups = 6 
     
    mse = (10.8529139633, 4.07865387387, 3.38408769104, 3.06303387774,3.04027656595,2.74723547149)
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.4  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(xfontsize)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(yfontsize)    
    plt.xlabel('Training Length (month)',size=xlabelsize)  
    plt.ylabel('Mean MSE', size=ylabelsize)  
    plt.xticks(0.5+ index + bar_width, ('0.5','1','1.5','2','2.5','3'))  
    plt.xlim(0,7)
    plt.ylim(0,12)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':legendsize})   
    #plt.tight_layout()  
    plt.show() 
    
    
if graph == 1:
    n_groups = 4  
     
    means_occ = (8.60084219559 ,  0.000385731267841 ,  0.648762484776 ,  1.18649502677)  
    means_traf = (12.6118711793, 0.0929882253731, 1.18880715534, 0.483427359963)  
    
    i=0
    s = []
    for i in range(len(means_occ)):
        if means_traf[i]-means_occ[i] > 0:
            t = (means_traf[i]-means_occ[i])/means_traf[i]
        else:
            t = (means_traf[i]-means_occ[i])/means_occ[i]
        print t
        s.append(t)
    print 'mean t', np.mean(s)
    
    fig = plt.figure(figsize=(8,6),dpi=80)
    errorDis1 = plt.subplot(1,1,1)  
    index = np.arange(n_groups)  
    bar_width = 0.35  
      
    opacity = 0.4  
    rects1 = plt.bar(index, means_occ, bar_width,alpha=opacity, color='b',label= 'LWR-OT MSE')  
    rects2 = plt.bar(index + bar_width, means_traf, bar_width,alpha=opacity,color='g',label='LWR-T MSE') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(45)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(45)    
    plt.xlabel('Dates',size=45)  
    plt.ylabel('MSE', size=45)  
    plt.xticks(index + bar_width, ('8.1', '8.7', '8.18', '8.20'))  
    #xlim(16,24)
    ylim(0,13)  
    plt.legend(prop={'size':45})  
      
    #plt.tight_layout()  
    plt.show()  

elif graph == 2:#'6.5','6.6','6.9','6.10'
    n_groups = 17  
     
    #means_occ = (8.23930025342, 0.00487798881758, 0.130378965028, 0.0513135815451, 0.793479898284, 0.0200491543588, 0.803675403146, 8.98697367721, 0.4465224392, 0.0174612097073, 1.1153500868, 0.603382735784, 6.89893044555, 0.0103801798561, 0.00781042017206, 1.21247385261, 2.38459701201)  
    means_occ = (8.23930025342, 0.130378965028, 0.130378965028, 0.130378965028, 0.793479898284, 0.130378965028, 0.803675403146, 8.98697367721, 0.4465224392, 0.130378965028, 1.1153500868, 0.603382735784, 6.89893044555, 0.130378965028, 0.130378965028, 1.21247385261, 2.38459701201)  
    means_traf = (13.9186390533, 0.534023668639, 0.534023668639, 0.534023668639, 2.99556213018, 0.534023668639, 0.534023668639, 0.0724852071006, 2.99556213018, 2.99556213018, 0.534023668639, 0.534023668639, 13.918639053, 0.534023668639, 0.534023668639, 2.99556213018, 0.0724852071006)  
    
    i=0
    s = []
    for i in range(len(means_occ)):
        if means_traf[i]-means_occ[i] > 0:
            t = (means_traf[i]-means_occ[i])/means_traf[i]
        else:
            t = (means_traf[i]-means_occ[i])/means_occ[i]
        print t
        s.append(t)
    a = []
    for j in range(len(s)):
        if s[j] == min(s) or s[j]==max(s):
            continue
        a.append(s[j])
    limit = 5
    lower_limit = np.percentile(s, limit) # computes the qth percentile (5th in this case) of the data in the array a
    upper_limit = np.percentile(s, 100-limit)
    print limit, '% Truncated mean', scipy.stats.tmean(s, limits=(lower_limit,upper_limit ), inclusive=(True, True)) # inclusive determines whether values exactly equal to the lower or upper limits are included
    print 'mean t', np.mean(a)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.4  
      
    opacity = 1 
    rects1 = plt.bar(index, means_occ, bar_width,alpha=opacity, color='#87CEFA',label= 'TFO-TT')  
    rects2 = plt.bar(index + bar_width, means_traf, bar_width,alpha=opacity,color='#FA8072',label='TF-T') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Dates',size=50)  
    plt.ylabel('MSE', size=50)  
    plt.xticks(index + bar_width, ('6.5','6.6','6.9','6.10','6.12','6.23','6.24','6.25','6.30',
    '7.3','7.7','7.10','7.15','7.17','7.21','7.23','7.28','8.1', '8.7', '8.18', '8.20'))  
    plt.ylim(0,14)  
    plt.legend(bbox_to_anchor=(0.47, 1), prop={'size':40})  
      
    #plt.tight_layout()  
    plt.show() 
elif graph == 2.1:#'6.5',  '6.25',  '7.21',  '8.1'
    n_groups = 4  
    means_occ = (8.23930025342, 8.98697367721, 6.89893044555, 8.14490350008)
    means_traf = (13.9286390533, 0.0724852071006, 13.9186390533, 13.9486390533)
    
    i=0
    s = []
    for i in range(len(means_occ)):
        if means_traf[i]-means_occ[i] > 0:
            t = (means_traf[i]-means_occ[i])/means_traf[i]
        else:
            t = (means_traf[i]-means_occ[i])/means_occ[i]
        print t
        s.append(t)
    a = []
    for j in range(len(s)):
        if s[j] == min(s) or s[j]==max(s):
            continue
        a.append(s[j])
    limit = 5
    lower_limit = np.percentile(s, limit) # computes the qth percentile (5th in this case) of the data in the array a
    upper_limit = np.percentile(s, 100-limit)
    print limit, '% Truncated mean', scipy.stats.tmean(s, limits=(lower_limit,upper_limit ), inclusive=(True, True)) # inclusive determines whether values exactly equal to the lower or upper limits are included
    print 'mean t', np.mean(a)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.2  
      
    opacity = 1 
    rects1 = plt.bar(0.3 + index, means_occ, bar_width,alpha=opacity, color='#87CEFA',label= 'TFO-TT')  
    rects2 = plt.bar(0.3 + index + bar_width, means_traf, bar_width,alpha=opacity,color='#FA8072',label='TF-T') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Dates',size=50)  
    plt.ylabel('MSE', size=50)  
    plt.xticks(0.3 + index + bar_width, ('6.5',  '6.25',  '7.21',  '8.1'))  
    #plt.ylim(0,14)  
    plt.legend(bbox_to_anchor=(0.5, 1), prop={'size':40})  
      
    #plt.tight_layout()  
    plt.show()  
elif graph == 3:
    n_groups = 4  
     
    corr = (0.60034, 0.51766, 0.4261, 0.31872)
    corrWd = (0.63432, 0.53022, 0.42718, 0.37254)
    #corrWk = (0.41212, 0.38766, 0.33548, 0.251)

    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.4  
      
    opacity = 0.7 
    rects1 = plt.bar(0.65+index, corr, bar_width,alpha=opacity, color='#87CEFA',label= 'All days')  
    rects2 = plt.bar(0.65+index + bar_width, corrWd, bar_width,alpha=opacity,color='#FA8072',label='Weekdays') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Areas (km$^2$)',size=50)  
    plt.ylabel('Correlation', size=50)  
    plt.xticks(0.65+index + bar_width, ('1','4','36','144'))  
    plt.xlim(0,4.5)
    plt.ylim(-0,0.7)  
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':40})  
      
    #plt.tight_layout()  
    plt.show()  

elif graph == 4:#Monday ~ Sunday and all
    n_groups = 8 
     
    mse = (3.92131554895, 4.03734144634, 5.03314074227, 5.39731402174, 5.64238752328, 12.4017041452, 7.69503911491, 7.56257021281)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.5  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Days',size=50)  
    plt.ylabel('Mean MSE', size=50)  
    plt.xticks(0.5+ index + bar_width, ('Mon','Tue','Wed','Thu','Fri','Sat','Sun','All'))  
    #plt.ylim(-0,0.7)  
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':40})  
      
    #plt.tight_layout()  
    plt.show() 


#elif graph == 6:#Temporary vs Permanent - 2a - different training time
#    n_groups = 5
#    #mse = (14.2177786334, 4.42757176108, 3.96293832033, 3.00336627551, 2.99212143795)
#    #mse = (11.3630137637, 8.30783926981, 7.40331461664, 6.7372113718, 4.53503860232, 4.53503860232, 4.53503860232, 4.53503860232)
#    fig, ax = plt.subplots()  
#    index = np.arange(n_groups)  
#    bar_width = 0.4  
#      
#    opacity = 0.7 
#    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
#    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
#    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
#    ax=plt.gca()
#    for tick in ax.xaxis.get_major_ticks():
#        tick.label1.set_fontsize(40)
#    for tick in ax.yaxis.get_major_ticks():
#        tick.label1.set_fontsize(40)    
#    plt.xlabel('Training Length (week)',size=50)  
#    plt.ylabel('Mean MSE', size=50)  
#    plt.xticks(0.5+ index + bar_width, ('1','2','3','4','6','8','10','12'))  
#    plt.xlim(0,6)
#    #plt.ylim(0,15.5)
#    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
#    #plt.tight_layout()  
#    plt.show()
elif graph == 7:#Temporary vs Permanent - 3a - May vs June for July
    n_groups = 2
    mse = (4.42760649074, 2.89195517687)
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.4  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('training time(Month)',size=50)  
    plt.ylabel('mean MSE', size=50)  
    plt.xticks(0.5+ index + bar_width, ('May','June'))  
    plt.xlim(0,3)
    plt.ylim(0,5)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    plt.show()
elif graph == 8:#Temporary vs Permanent - 3a - May vs June vs July for August
    n_groups = 3
    mse = (5.69160192947, 3.80397755331, 3.96293832033)
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.4  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('training time(Month)',size=50)  
    plt.ylabel('mean MSE', size=50)  
    plt.xticks(0.5+ index + bar_width, ('May','June','July'))  
    plt.xlim(0,4)
    plt.ylim(0,7)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    plt.show()
elif graph == 9:#TFO-TT / TF-T
    n_groups = 9 
     
    mse = (1.3288798632019381, 2.3299636296757691, 2.2165000327253259, 3.3373095525097929, 1.8801378014210286, 2.9050446434401778, 1.7676430073562168, 0.88693142833407723, 2.5658502366593181)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.5  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Time',size=50)  
    plt.ylabel('Ratio Mean', size=50)  
    plt.xticks(0.5+ index + bar_width, ('16.0','17.0','18.0','19.0','20.0','21.0','22.0','23.0','24.0'))  
    #plt.ylim(-0,0.7)  
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':40})  
      
    #plt.tight_layout()  
    plt.show() 
elif graph == 10:#Fine-grained on floors Total, RFE 25% - 
#MSE of TPO-P without and with RFE.
    n_groups = 2
    mse = (2.85442982136, 2.67743721074)
    
    #Total, random 10, random 30, RFE 25%
#    n_groups = 4
#    mse = (2.85442982136, 2.91546933629, 2.82799128194, 2.67743721074)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.3  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Algorithms',size=50)  
    plt.ylabel('Mean MSE', size=50)  
    plt.xticks(0.5+ index + bar_width, ('TFO-PT','TFO-PT (RFE)'))  
    plt.xlim(0,3)
    plt.ylim(2.5,3)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    plt.show()

elif graph == 10.2:#Fine-grained on floors Total, RFE 25% - 
#MSE of TPO-T without and with RFE.

    n_groups = 2
    mse = (3.03595447335, 2.81896390127)
    
    #Total, random 10, random 30, RFE 25%
#    n_groups = 4
#    mse = (2.85442982136, 2.91546933629, 2.82799128194, 2.67743721074)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.3  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Algorithms',size=50)  
    plt.ylabel('Mean MSE', size=50)  
    plt.xticks(0.5+ index + bar_width, ('TFO-T','TFO-T (RFE)'))  
    plt.xlim(0,3)
    plt.ylim(2.5,3.1)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    plt.show()
elif graph == 10.3:#Fine-grained on time slot, lasso 
#MSE of TPO-P without and with lasso.
    n_groups = 2
    mse = (127.880889311, 2.81896390127)
#    n_groups = 4
#    mse = (2.85442982136, 2.91546933629, 2.82799128194, 2.67743721074)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.3  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Algorithms',size=50)  
    plt.ylabel('Mean MSE', size=50)  
    plt.xticks(0.5+ index + bar_width, ('TFO-P \n(without Lasso)','TFO-P'))  
    plt.xlim(0,3)
    plt.ylim(0,130)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    plt.show()
elif graph == 11:#overall - running time  #Running Time of different scheme components.
    n_groups = 3
    mse = (24, 432, 1)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.3  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Scheme Components',size=50)  
    plt.ylabel('Running Time (Minutes)', size=50)  
    plt.xticks(0.55+ index + bar_width, ('Feature \nSelection','Feature \nExtraction','Learning and \nForecasting'))  
    plt.xlim(0,3.5)
    #plt.ylim(2.5,3)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    #plt.grid(True, which = 'major', axis = 'y', linewidth=2.5, solid_joinstyle='bevel')
    plt.show()
elif graph == 12:#cut loading apart - running time  #Running Time of different scheme components, a more detailed view.
    n_groups = 5
    mse = (80, 1, 8, 280, 1)
    
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.3  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(40)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(40)    
    plt.xlabel('Scheme Components',size=50)  
    plt.ylabel('Running Time (Minutes)', size=50)  
    plt.xticks(0.55+ index + bar_width, ('Data \nLoading','LASSO','RFE','DTW-OT','LWR'))  
    #plt.xlim(0,3.5)
    #plt.ylim(2.5,3)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    #plt.grid(True, which = 'major', axis = 'y', linewidth=2.5, solid_joinstyle='bevel')
    plt.show()
elif graph == 13:#|S - \tilde(S)| |S - \bar(S)| |S - S_K| 
    n_groups = 3
    mse = (0, 8.77439156301, 40.1666666667)
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.3  
      
    opacity = 0.7 
    rects1 = plt.bar(0.7+index, mse, bar_width,alpha=opacity, color='#87CEFA')  
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='w') 
    #rects2 = plt.bar(index + 2*bar_width, corrWk, bar_width,alpha=opacity,color='g',label='Weekends') 
    ax=plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontweight('bold')
        tick.label1.set_fontsize(45)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(45)
    ax.tick_params(direction='out', pad=15)
    plt.xlabel('Different Measurements of $S$',size=50)  
    plt.ylabel('Mean Square Error', size=50)  
    plt.xticks(0.55+ index + bar_width, (r'$S = \widetilde{S}$',r'$S = \overline{S}$','$S = S_c$'), fontsize = 50)  
    plt.xlim(0,3.5)
    #plt.ylim(2.5,3)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size':50})   
    #plt.tight_layout()  
    #plt.grid(True, which = 'major', axis = 'y', linewidth=2.5, solid_joinstyle='bevel')
#time = [1,2,3]
#occ = [8.60084219559 ,  0.000385731267841 ,  0.648762484776]
#ha = [12.6118711793, 0.0929882253731, 1.18880715534]

area = [1,4,36,144]
corrWd = [0.63432, 0.53022, 0.42718, 0.37254]
corr = [0.60034, 0.51766, 0.4261, 0.31872]
corrWk = [0.41212, 0.38766, 0.33548, 0.251]

time=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#1.48608153238
occ=[8.23930025342, 0.00487798881758, 0.130378965028, 0.0513135815451, 0.793479898284, 0.0200491543588, 0.4465224392, 0.0174612097073, 6.89893044555, 0.0103801798561, 0.00781042017206, 1.21247385261]
#3.5853057199
ha=[13.9186390533, 0.534023668639, 0.534023668639, 0.534023668639, 2.99556213018, 0.534023668639, 2.99556213018, 2.99556213018, 13.918639053, 0.534023668639, 0.534023668639, 2.99556213018]
