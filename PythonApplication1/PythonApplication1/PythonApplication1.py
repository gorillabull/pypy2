
def main():
    q = int(input())

    #get the input stuff
    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        shiiet(n,c_lib, c_road, cities)


def shiiet(n, c_lib, c_road, d):
    adj2 = [[]] # [[0 for x in range(100)]for y in range(100)]
    #keep track of the visited nodes 
    visited = []


    def dfs(s):
        visited[s] = True
        for x in range(0,adj2[s].__len__(),1):
            if(visited[adj2[s][x]] == False):
                #p = adj2[s][x]
                #print(p)
                dfs(adj2[s][x])
        #number of nodes in the array

    nodes = 6

    #number of connected components in the entire graph
    conComp = 0

    #count of subtrees
    ct = 0 

    #return value
    result = 0

    #append a bunch of extra nodes for missing elements
    for x in range(10**6):
        adj2.append([0])

    visited = [False for x in range(10**6)]  

    nodes = n
 
    #init adjacency lists
    for x in range(0,d.__len__(),1):
        adj2.append([])
        adj2[d[x][0]].append(d[x][1])

    #print("---------------")
    #print(conComp)

    result = 0
    cheapest = 0

    if c_road >= c_lib:
        result =  n *c_lib
    else:
        ct=0
        for x in range(1,nodes + 1,  1):
            ct = ct + 1 
            if visited[x] == False:
                dfs(x)
                conComp = conComp + 1
                result =(ct-1) * c_road + c_lib
                ct=0 

    #result = result + (n - conComp) * cheapest 

    print(result)

    return result
    
    


main()

s = 5 

