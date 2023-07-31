class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
       
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def __dfsHelper(self, sv, visited, list):
        
        #print(sv, end = " ")
        list.append(sv)
        visited[sv] = True 
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited, list)
            
        return list
    
    def dfs(self):         
        visited = [False for i in range(self.nVertices)]
        final_list = []
        for i in range(self.nVertices):
            if not visited[i]:
                cc = self.__dfsHelper(i, visited, [])
                final_list.append(cc)

        #self.__dfsHelper(0, visited)
        return final_list
    
g = Graph(8)
g.addEdge(0, 7)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(3, 5)
g.addEdge(3, 6)

list = g.dfs()

for i in list:
    i.sort()
    for j in i:
        print(j, end = " ")
    print()