
from math import inf
import Graph as g
import random
import networkx as nx
import time
import math

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path
def current_weight(graph,current,nbd):
    
    for (u,v,w) in graph.edges(data=True):
        if u==current and v==nbd:
            wt=w["weight"]
           
    return wt

def Dijktra_App(graph,source,target,avnd):
    avn=avnd
    # print(" Dijktra Algorithm")
    v=0
    ed=0 
    queue = []
    visited = {}
    distance = {}
    shortest_distance = {}
    parent = {}
    for node in range(1,len(graph)+1):
        distance[node] = None
        visited[node] = False
        if node in avn:
            visited[node]=True
            v=v+1
        parent[node] = None
        shortest_distance[node] = float(9999)
    queue.append(source)
    distance[source] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        visited[current] = True        
        if current == target:
            # print("SHORTEST PATH PRINTING")
            # print("Shortest Path")
            # print()
            backtrace(parent, source, target)
            #break
        for neighbor in graph[current]:           
            if visited[neighbor] == False:              
                #print("(",current,neighbor,")") 
                distance[neighbor] = distance[current] + current_weight(graph,current,neighbor)
                if current_weight!=None:
                    ed=ed+1                
                if distance[neighbor] < shortest_distance[neighbor]:
                            shortest_distance[neighbor] = distance[neighbor]
                            parent[neighbor] = current                         
                            queue.append(neighbor)                     
    # print(graph.edges())                                                  
    print("Shortest Distance D: ")
    print(str(shortest_distance[target]))    
    # print("Dijktra Shortest Path:")
    # print(nx.shortest_path(graph, source, target, weight="weight", method='dijkstra'))
    # print("Path cost: ",nx.dijkstra_path_length(graph,source,target,weight="weight"))
    tn=graph.number_of_nodes()-v
    print("Number of Node traversed: "+str(tn)) 
    print("Number of Edges traversed: "+str(ed))
    # print("#Nodes: ",graph.number_of_nodes())
    # print("#Edges: ",graph.number_of_edges())
    return tn,ed
def Finding_all_path(R_g,s,t,cut):
    print("..........All possible path from Source to Destination ..........")
    counter=0
    for path in nx.all_simple_paths(R_g, source=s, target=t,cutoff=cut):
        print("Path : "+str(path), end=" ")         
        path_cost(R_g,path)             
        counter+=1     
    print()    
    print("....Total number of paths : ",counter)    
    e=R_g.number_of_edges()
    print("....Number of edges in the graph : ",e)

def path_cost(graph,path):
    cost=0
    for i in range(len(path)-1):        
        for (u,v,w) in graph.edges(data=True):
            if u==path[i] and v==path[i+1]:                
                cost+=w['weight']
    print(", Path Cost: "+str(cost)) 

def experiment1():
    nd2=[]
    edg2=[]
    time2=[]    

    print("...... started Taskgraph.......") 
    worker_list2=[6,9,12,15,18,21,24,27,30,33,36,39,42,45,48]   
    no_worker2=worker_list2 
    iter2=len(worker_list2)
    for i in range(len(no_worker2)):
        
        print("Number of workers: ",no_worker2[i])      
        tg,avoid_nodes=g.create_Task_Graph(no_worker2[i])
        # print("Avoiding nodes......")  
        # print(avoid_nodes)  
        # Finding_all_path(tg,0,g.n+1,None)
        n22=0
        e22=0
        t22=0
        avg=3
        for jj in range(avg):
          start=time.time()
          n2,e2=Dijktra_App(tg,0,g.n+1,avoid_nodes)
          end=time.time()
          t2=(end-start)*1000
          n22+=n2
          e22+=e2
          t22+=t2

        nd2.append(math.ceil(n22/avg))
        edg2.append(math.ceil(e22/avg))
        time2.append(round(t2/avg,2))
        print("Time in execution: ",end="")
        print(t2)
        # print("#Workers  #Nodes  #Edges  Execution Time(ms)")
    # for k in range(iter2):
    #     print("   ",no_worker2[k],"  ",math.ceil(nd2[k]),"     ",math.ceil(edg2[k]),"   ",round(time2[k],2))
    return iter2,no_worker2,nd2,edg2,time2 
def experiment2():
    no_node_list=[5,10,15,20,25,30,35,40,45,50,55]#,60]#,65,70,75]
    
    source=1 
    no_node=no_node_list
    iteration=len(no_node_list)
    nd2,ed2,time2=[],[],[]

    # nd3and4,ed3and4,time3and4=[],[],[] 
    # nd3or4,ed3or4,time3or4=[],[],[]      
       
    for ix in range(iteration):
        print("Number of node: ",no_node[ix])
        R_graph=g.create_Random_Graph(no_node[ix])     #,avd_node3,avd_node3and4,avd_node3or4
        print("Random Graph Result")
        destination=no_node[ix] 
        avd=avoid_calculation(iteration,source,destination) 

        #Finding_all_path(R_graph,1,no_node,None)
        n22=0
        e22=0
        t22=0
        avg=3
        for jj in range(avg):
            start=time.time()    
            n2,e2=Dijktra_App(R_graph,source,destination,avd)
            end=time.time()
            t2=(end-start)*1000
            n22+=n2
            e22+=e2
            t22+=t2
        nd2.append(math.ceil(n22/avg))
        ed2.append(math.ceil(e22/avg))
        time2.append(t2/avg)

        # start3and4=time.time()    
        # n2,e2=Dijktra_App(R_graph,source,destination,avd_node3and4)
        # end3and4=time.time()
        # t2=(end3and4-start3and4)*1000
        # nd3and4.append(n2)
        # ed3and4.append(e2)
        # time3and4.append(t2) 
        
        # start3or4=time.time()    
        # n2,e2=Dijktra_App(R_graph,source,destination,avd_node3or4)
        # end3or4=time.time()
        # t2=(end3or4-start3or4)*1000
        # nd3or4.append(n2)
        # ed3or4.append(e2)
        # time3or4.append(t2)    
        # collect=[nd3and4,ed3and4,time3and4,nd3or4,ed3or4,time3or4]
    return iteration,no_node_list,nd2,ed2,time2#,collect

def avoid_calculation(n,source,destination):
     avoid_node=[]
     modulus_operands=1
     while(source%modulus_operands==0 or destination%modulus_operands==0):
         modulus_operands=random.randint(2,5)              
     for av in range(1,n+1):
         if(av%modulus_operands==0):
             avoid_node.append(av)
     return avoid_node

if(__name__ =="__main__"):

    print("Proposed Experiment 2")
    # experiment1()
    # avd=avoid_calculation(35,1,29)
    # for i in range(len(avd)):
    #     print(avd[i])
    # print("modulus:",11111)    
    # print()

   
   
   
                
  
    
