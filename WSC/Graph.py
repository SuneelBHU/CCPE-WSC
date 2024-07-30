
import networkx as nx
import matplotlib.pyplot as plt
import random
random.seed(1445)

def create_Random_Graph(n):
    RG=nx.MultiDiGraph()
    
    node_list=[]
    for i in range(1,n+1):        
        node_list.append(i)
    RG.add_nodes_from(node_list)
    for i in range(1,n+1):        
        for j in range(i+1,n+1):            
            RG.add_edge(i,j,weight=random.randint(1,10))

    return RG #,avoid3,avoid3and4,avoid3or4
def create_Task_Graph(no_workers):
    print("Task Graph is being created .......")
    
    Theta=5 #Theta is the threshold for the number of subtasks divided by the worker
            #The workers who divides the tasks into smaller number of subtasks will be avoided to participate in the solution of the task. 
    m=[0]*no_workers
    global n
    n=0
    anc1=[] #Avoid node collection  
    # code for workers who divides the task into random number of subtasks  
    for i in range(no_workers):
        if(i<no_workers/3):
            m[i]=random.randint(2,4)
            # m[i]=3
        elif(no_workers/3<=i<2*no_workers/3):
            m[i]=random.randint(4,5)
            # m[i]=5
        else:
            m[i]=random.randint(5,6)    
            # m[i]=6
    # for i in range(no_workers):
    #     print("Worker",i+1,"divides task into ",m[i]," subtasks")
        n+=m[i]+1
    print("Destination Node Index "+str(n+1))  #Adding target node index
    #Workers  
    TG=nx.MultiDiGraph()
    #BEGIN...........Creation of graph by adding the nodes with associated cost..........................
    indexing=1
    for wk in range(no_workers):
        TG.add_edge(0,indexing,weight=0)
        for i in range(1,m[wk]+1):
            if(wk<no_workers/3):
                TG.add_edge(indexing,indexing+1,weight=random.randint(7,9))
                if m[wk]<Theta:
                    anc1.append(indexing)
            elif(no_workers/3<=wk<2*no_workers/3):
                TG.add_edge(indexing,indexing+1,weight=random.randint(4,6))
                if m[wk]<Theta:
                    anc1.append(indexing)
            else:
                TG.add_edge(indexing,indexing+1,weight=random.randint(1,2))
            indexing+=1                    
        TG.add_edge(indexing,n+1,weight=0)
        indexing+=1
    #END...................................creation graph.................................................

    return TG,anc1




    


    
