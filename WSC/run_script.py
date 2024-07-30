
import WSC_Algorithm as pal
import Existing_Algorithm as al
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
import random
random.seed(1445)


def Ploting_graph(x_ax,y_ax1,y_ax2,x_lb,y_lb,fig_num):
       
       fn=str(fig_num)
       plt.title("Algorithm's performance graph")     
       plt.plot(x_ax, y_ax1,linestyle = 'dashed',color='r',label="Existing algorithm",marker = 'o')
       plt.plot(x_ax, y_ax2,linestyle = 'dashed',color='g',label="WSC algorithm",marker = '^')       
       plt.xlabel(x_lb)
       plt.ylabel(y_lb)
       plt.legend()
       store_path="C:/Users/Administrator/Dropbox/Research_Lab/CrowdGit24/"
       if fig_num==0:               
            plt.savefig(store_path+'Garbage/Performance_graph'+fn+'.svg')            
       elif fig_num<=3:
            plt.savefig(store_path+'Task_graph_performance/Performance_graph'+fn+'.svg')
       else:
            plt.savefig(store_path+'Random_graph_performance/Performance_graph'+fn+'.svg')     
        
       plt.show()
def Plot_multi_graph(x_ax,y_axe,y_axp1,ax_3nad4,ax_3or4,x_lb,y_lb,fn):
     fn=str(fn)
     plt.title("Algorithm's performance graph")
     plt.plot(x_ax, y_axe,linestyle = 'dashed',color='r',label="Existing algorithm",marker = 'o')
     plt.plot(x_ax, y_axp1,linestyle = 'dashed',color='g',label="Modified algorithm: nk%3",marker = '^') 
     plt.plot(x_ax, ax_3nad4,linestyle = 'dashed',color='b',label="Modified algorithm: nk%3 AND nk%4) ",marker = '*')  
     plt.plot(x_ax, ax_3or4,linestyle = 'dashed',color='y',label="Modified algorithm: nk%3 OR nk%4)",marker = '+')   

     plt.xlabel(x_lb)
     plt.ylabel(y_lb)
     plt.legend()
    
     plt.savefig('C:/Users/acer/Dropbox/Research_Lab/CrowdGit24/Performance_graph'+fn+'.jpeg')
     plt.show()       
       

if(__name__ =="__main__"):
       fig_count=2 
       #........Task Graph................
       inx1,w1,n1,e1,t1=al.experiment1()
       inx2,w2,n2,e2,t2=pal.experiment1()
     
     #   inx1,w1,n1,e1,t1,n2,e2,t2=ex1.experiment1()
     #   inx2=inx1; w2=w1
     #   x_axis = w2
       y_axis1,y_axis2,y_axis3,y_axis4,y_axis5,y_axis6=[],[],[],[],[],[]
       print(inx1, len(w1), len(n1),len(e1),len(t1),len(n2),len(e2),len(t2))
       for l in range(inx2):
           y_axis1.append(n1[l])
           y_axis2.append(n2[l])
           y_axis3.append(e1[l])
           y_axis4.append(e2[l])
           y_axis5.append(t1[l])
           y_axis6.append(t2[l])

       print("Numerical analysis..")
       for k1 in range(inx1):
            print(k1, "  ",n1[k1], "  ",e1[k1], "  ",t1[k1],  "          ",n2[k1],"  ",e2[k1],"  ",t2[k1])
       ##..................Random Graph...........................##
       modulas=[3,4]

       ind21,no_node21,n21,eg21,t21=al.experiment2()
       ind22,no_node22,n22,eg22,t22=pal.experiment2()
       x_ax=no_node21
       y_axis21,y_axis22,y_axis23,y_axis24,y_axis25,y_axis26=[],[],[],[],[],[]
       for li in range(ind21):
           y_axis21.append(n21[li])
           y_axis22.append(n22[li])
           y_axis23.append(eg21[li])
           y_axis24.append(eg22[li])
           y_axis25.append(t21[li])
           y_axis26.append(t22[li])
       print(" Random Graph Numerical analysis.........")
       print("indexing  No.of nodes   v1,  e1  time1    v2     e2   t2")
       for k1 in range(ind22):
            print(k1,"   ",x_ax[k1],"    ",n21[k1],"   ",eg21[k1]," initial time:",t21[k1],"    ", n22[k1], "  ",  eg22[k1],  " final time:",t22[k1])
       
       #plotting for taskgraph
       print("1===>>We are going to plot........")
       print("Experiment 1 : Task Graph sets performance ......")
       Ploting_graph(x_axis,y_axis1,y_axis2,"No. of workers","No. of traversed vertices ",1)      
       Ploting_graph(x_axis,y_axis3,y_axis4,"No. of workers","No. of traversed edges ",2)
       Ploting_graph(x_axis,y_axis5,y_axis6,"No. of workers","Execution time (milisecond) ",3)       
       #plotting for the random graph   
       
       print("2===>>We are going to plot........")
       print("Experiment 2: Random graph  performance ......")      
       Ploting_graph(x_ax,y_axis21,y_axis22,"No. of vertices ","No. of traversed vertices ",4)
       Ploting_graph(x_ax,y_axis23,y_axis24,"No. of vertices ","No. traversed edges ",5)
       Ploting_graph(x_ax,y_axis25,y_axis26,"No. of vertices ","Execution time (milisecond) ",6)
 
       print("stopped plotting")
       



           
        





















 

