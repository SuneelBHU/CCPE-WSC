import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
#......THIS SNIPPET IS TO ANALYSYS THE EFFECT OF AGING TECHNIQUE ON A LIST OF WEIGHTS .......
#..... HERE, WE HAVE SELECTED TWO LIST OF WEIGHTS...................
#.....THE ONE LIST OF WEIGHT IS OF THAT WORKER WHOSE WEIGHTS ARE CONTINOUSLY INCREASING.......
#.....THE SECOND LIST OF WORKER WEIGHTS IS OF THAT WORKER WHOSE DYNAMIC WEIGHTS ARE CONTINOUSLY DECRASING......
def Aging_Technique(decay_rate,list_of_data):
    wf=[]
    list1=list_of_data
    age=[0]*len(list1)
    lam=decay_rate
    ###..............Estimating the ages with the version of the reviews...............##
    for i in range(len(list1)):
        age[i]=len(list1)-i    
    ### ..............Calculating the weight factors by using decay function..........##
    sum_wf=0
    for i in range(len(list1)):             
        wf.append(math.exp(-lam*age[i]))
        sum_wf+=wf[i]        
    ##print("weight factor's sumation: ",round(sum_wf,3))   
    ##..............Calculating Normalised weight of weight factors..................##
    nw=[]    
    for i in range(len(list1)):
        nw.append(round(wf[i]/sum_wf,4))        
    ##..............calculating desired reslting weight ............................##
    rw=[]  
    sum_rw=0
    for i in range(len(list1)):
        rw.append(round(wf[i]*nw[i],4))
        sum_rw+=rw[i]
    #print("Sum of Resulting weight",round(sum_rw,3))        
    ##.................  Scalling the resulting weight..............................##   
    max_review=max(list1)
    min_review=min(list1)
    # print(sum_rw)
    # print(max_review)
    # print(min_review)
    Resulting_weight=(max_review-min_review)*sum_rw+min_review
    return Resulting_weight
# FUNCTION WHICH FINDS THE WORKER AND HIS/HER LIST OF WEIGHT WHICH CONTINUESLY INCREASING
#BEGIN
def Increasing_dynamic_weight_worker(w11):
    w1=w11;  temp=0; weight_list=[]
    for i in range(len(updateDF)):
        if w1==updateDF['Worker_Id'][i]:
            temp=updateDF.iloc[i,2]
            if len(weight_list)==0:
                weight_list.append(temp)            
            else:
                if weight_list[-1]<temp:
                    weight_list.append(temp)      
    # print("list of values:",weight_list)
    return weight_list
#END
# FUNCTION WHICH FINDS THE WORKER AND HIS/HER LIST OF WEIGHTS WHICH CONTINUESLY DECREASING 
# BEGIN 
def Decreasing_dynamic_weight_worker(w22):
    w1=w22;  temp=0; weight_list=[]
    for i in range(len(updateDF)):
        if w1==updateDF['Worker_Id'][i]:
            temp=updateDF.iloc[i,2]
            if len(weight_list)==0:
                weight_list.append(temp)            
            else:
                if weight_list[-1]>temp:
                    weight_list.append(temp)    
    # print("list of values:",weight_list)
    return weight_list 
def Random_dynamic_weight(w33):
    print("Random function....")
    w1=w33;  temp=0; weight_list=[]
    for i in range(len(updateDF)):
        if w1==updateDF['Worker_Id'][i]:
            temp=updateDF.iloc[i,2]            
            weight_list.append(temp)
            if len(weight_list)==6:
                return weight_list                  
#END
# THIS FUNCTION FINDS THE STATIC WEIGHT OF THAT WORKER FOR WHOME WORKING IS IN PROGRESS
def Find_first_static_weight(w):
    swt=0
    for i in range(len(updateDF)):
        if w==updateDF.iloc[i,0]:
            swt=updateDF.iloc[i,1]         
            break
    return swt
# SELECTING A WORKER WHOSE WEIGHTS ARE CONTINUESLY INCREASING
def Find_worker1():   
    w=str()
    for i in range(len(updateDF)):
        w=updateDF.iloc[i,0]        
        wt_list=Increasing_dynamic_weight_worker(w)
        if len(wt_list)==6:                     
            return wt_list,w
# SELECTING A WORKER WHOSE WEIGHTS ARE CONTINUESLY DECREASING     
def Find_worker2():   
    w=str()
    for i in range(len(updateDF)):
        w=updateDF.iloc[i,0]        
        wt_list=Decreasing_dynamic_weight_worker(w)
        if len(wt_list)==6:            
            return wt_list,w
def Find_worker3():
    w=str()
    for i in range(len(updateDF)):
        w=updateDF.iloc[i,0]        
        wt_list=Random_dynamic_weight(w)
        if len(wt_list)==6:            
            return wt_list,w        
# THIS FUNCTION DISTRIBUTES THE WEIGHTS......
def slice_data(input_list): 
    if len(input_list)==7:
        data2=input_list[:2]
        data3=input_list[:3]
        data4=input_list[:4]
        data5=input_list[:5]
        data6=input_list[:6]
        data7=input_list[:7]
        data=[data2,data3,data4,data5,data6,data7]
    else: print("data is out of range on x axis and y axis")
    return data
# THIS FUNCTION WILL PLOT THE BAR GRAPH ON THE BASIS OF PROVIDED INFORMATION AS THE PARAMETERS
def plotting(dyw,input_data,l,fig_num,scale):  
    y_3=[]; y_6=[]; y_9=[]    # y_3 represent the value of y axis with decay rate 0.3 and in the same way ,  0.6, 0.9 etc.   
    bar_width = 0.15
    # l represent the set of decay rates. 
    for ix in range(len(input_data)):
        for lmi in range(len(l)):   # loop for the different decay rates 
            if lmi==0:
                y_3.append(Aging_Technique(l[lmi],input_data[ix]))
            if lmi==1:
                y_6.append(Aging_Technique(l[lmi],input_data[ix]))
            if lmi==2:
                y_9.append(Aging_Technique(l[lmi],input_data[ix]))

    y1=dyw     #dynamic weights
    fig, ax = plt.subplots()       
    ax.set_ylim(scale[0],scale[1])
    dyw=list(dyw)
    data_x_ax=dyw[:len(input_data)]    
    x_pos = np.arange(len(data_x_ax))    
    ax.bar(x_pos,y1,bar_width,color='r',label="Dynamic weights")   #The red bar graph  
    ax.bar(x_pos+bar_width, y_3, bar_width, color='darkgreen', label='Aged weight at \u03BB='+str(l[0]))    
    ax.bar(x_pos+2*bar_width, y_6, bar_width, color='green', label='Aged weight at \u03BB='+str(l[1]))
    ax.bar(x_pos+3*bar_width, y_9, bar_width, color='lightgreen', label='Aged weight at \u03BB='+str(l[2]))

    plt.xlabel("Set of previously distributed aged-weights")
    plt.ylabel("Aged weights ")     
# Add legend
    ax.legend()
# Add grid lines to the background
    ax.set_axisbelow(True)
# Show the plot
    plt.grid(True, linestyle='--')
    if l[0]==0.2:
        
        file_path = 'C:\\Users\\Administrator\\Dropbox\\Research_Lab\\AgingTech\\Bar_graph\\lambda246\\Fig'+str(fig_num)+'.svg'
    else:file_path = 'C:\\Users\\Administrator\\Dropbox\\Research_Lab\\AgingTech\\Bar_graph\\lambda369\\Fig'+str(fig_num)+'.svg'
    plt.savefig(file_path)
    if os.path.exists(file_path):
        print(file_path)        
    else:
        print(f"File not found: {file_path}") 
    
file=pd.read_csv('Dynamic_score.csv')
updateDF=pd.DataFrame(file)
static_weight=updateDF['Weight_Before_Review']

print("Checking start...")
dy_wt1,w1=Find_worker1()   
print("Worker and its incresing weight:",w1,dy_wt1)

dy_wt2,w2=Find_worker2()
print(w2,dy_wt2)
print("Worker and its decreasing weight:",w2,dy_wt2)
print(w2,dy_wt2) 

# dyw2=Decreasing_dynamic_weight_worker(wkr2)
st_wt1=Find_first_static_weight(w1)
st_wt2=Find_first_static_weight(w2)
input_list1=[]
input_list2=[]
print("Dynamic weight",dy_wt1)
print("Dynamic weight decresing",dy_wt2)
input_list1.append(st_wt1)    #Add the first static weight
input_list1.extend(dy_wt1)    #Append all the dynamic weight

input_list2.append(st_wt2)    #add the first static weight
input_list2.extend(dy_wt2) 
print("First static + all dynamic weight:",input_list1)
print("Dynamic list length(excluding static weight)",len(dy_wt1))

print("First static + all dynamic weight decreasing:",input_list2)
print("Dynamic list length decreasing ",len(dy_wt2))

if __name__=="__main__":
    scale1=[55,80]
    lambda_values=[0.2,0.4,0.6]
    lambda_values2=[0.3,0.6,0.9]    
    d=slice_data(input_list1)   # sliced data in the descrete form 
    d2=slice_data(input_list2)   #decreasing list
    plotting(dy_wt1,d,lambda_values,1,scale1)  # this will plot the bar graph at descrete lists of increasing value,
    # it considers the different decay rate, and ploted the resultant values.   
    print("check for first ",len(dy_wt1),dy_wt1,"check input list",d)
    ## For the the worker whose weight are decreasing    
    print("check for the second.....")  
    scale2=[35,60]
    print(dy_wt2)
    print(d2)
    plotting(dy_wt2,d2,lambda_values,2,scale2) 
    plotting(dy_wt1,d,lambda_values2,1,scale1) 
    plotting(dy_wt2,d2,lambda_values2,2,scale2) 
    
    



    
        
