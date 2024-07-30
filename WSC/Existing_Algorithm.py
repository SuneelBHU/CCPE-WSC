
import Graph as g
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

def Dijktra_App(graph,source,target):    
    print("Applying Dijktra Shortest Path Algorithm")
    v,ed=0,0    
    queue = []
    visited = {}
    distance = {}
    shortest_distance = {}
    parent = {}
    for node in range(1,len(graph)+1):
        distance[node] = None
        visited[node] = False            
        parent[node] = None
        shortest_distance[node] = float(9999)
        v=v+1
    queue.append(source)
    distance[source] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        visited[current] = True        
        if current == target:
            print()
            backtrace(parent, source, target)
            
        for neighbor in graph[current]:           
            if visited[neighbor] == False:              
              
                distance[neighbor] = distance[current] + current_weight(graph,current,neighbor)
                if current_weight!=None:
                 ed=ed+1                               
                if distance[neighbor] < shortest_distance[neighbor]:
                            shortest_distance[neighbor] = distance[neighbor]
                            parent[neighbor] = current                         
                            queue.append(neighbor)                
                                                     
    print("Shortest Distance D: ")
    print(str(shortest_distance[target]))   
    print("Number of Node traversed: "+str(v)) 
    print("Number of Edges traversed: "+str(ed))
    print("#Nodes: ",graph.number_of_nodes())
    print("#Edges: ",graph.number_of_edges())

    return v,ed
    
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
    global nd1
    nd1,edg1,time1=[],[],[]        
    print("...... started Taskgraph.......") 
    worker_list=[6,9,12,15,18,21,24,27,30,33,36,39,42,45,48]     
    no_worker=worker_list
    iter=len(worker_list) 
    for i in range(len(no_worker)):        
        print("Number of workers: ",no_worker[i])
        tg,_=g.create_Task_Graph(no_worker[i])
        n11,e11,t11,avg=0,0,0,3    
        for ii in range(avg):
          start=time.time()
          n1,e1=Dijktra_App(tg,0,g.n+1)
          end=time.time()
          t1=(end-start)*1000/3
          n11+=n1
          e11+=e1
          t11+=t1      
        nd1.append(math.ceil(n11/avg))
        edg1.append(math.ceil(e11/avg))
        time1.append(round(t11/3,2))

    return iter,no_worker,nd1,edg1,time1
def experiment2():
    no_node_list=[5,10,15,20,25,30,35,40,45,50,55]#,60]#,65,70,75]
    source=1 
    no_node=no_node_list
    iteration=len(no_node_list)
    nd2,ed2,time2=[],[],[]       
    for ix in range(iteration):
        print("Number of node: ",no_node[ix])
        R_graph=g.create_Random_Graph(no_node[ix])    
        print("Random Graph Result ")
        destination=no_node[ix]        
       
        n22=0
        e22=0
        t22=0
        avg=3
        for jj in range(avg):
            start=time.time()    
            n2,e2=Dijktra_App(R_graph,source,destination)
            end=time.time()
            t2=(end-start)*1000

            n22+=n2
            e22+=e2
            t22+=t2
        nd2.append(math.ceil(n22/avg))
        ed2.append(math.ceil(e22/avg))
        time2.append(t2/avg)
    return iteration,no_node_list,nd2,ed2,time2   

