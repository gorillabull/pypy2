adj = []
visited = []

visited = [False for x in range(1000)]  
adj = [[0 for x in range(10)]for y in range(10)]    
adj2 = [[]] # [[0 for x in range(100)]for y in range(100)]

#this is how they are given as input 
adj[1][2]=1
adj[3][1]=1
adj[2][4]=1
adj[1][2]=1
adj[2][3]=1
adj[5][6]=1

#number of nodes in the array 
nodes = 6

#number of connected components in the entire graph 
conComp = 0 ;

#count of subtrees 
ct=0 


def dfs(s):
    visited[s]=True;
    for x in range(0,adj2[s].__len__(),1):
        if(visited[adj2[s][x]]==False):
            p=adj2[s][x]
            print(p)
            dfs(adj2[s][x])
            




def hr1(a,b,c,d):
    #append the nodes into the list 
    for x in range(0,d.__len__(),1):
        for y in range(0,d[x].__len__(),1):
            if d[x][y] ==1:
                adj2.append([]);
                adj2[x].append(y)

#append a bunch of extra nodes for missing elements 
for x in range(100  ):
    adj2.append([0])



#init the adjacency lists
hr1(1,1,1,adj)

for x in range(1,nodes + 1,  1 ):
    if visited[x] ==False:
        dfs(x);
        conComp = conComp+1; 

print("---------------")
print(conComp)


dfs(6)


#final calculation, if more than one subtree 
#subtree count * lib_cost (at least one library in each subtree is required) + (number of nodes - Subtree count )