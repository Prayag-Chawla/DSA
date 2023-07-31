import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
       
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
        
    def removeEdge(self, v1, v2):
        if self.containEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
        
    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
        
    def __str__(self):
        return str(self.adjMatrix)
    

    
    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
            
    def bfs(self):       # Using BFS for traversing all vertices of a graph
        q = queue.Queue()
        visited = [False for i in range(self.nVertices)]
        visited[0] = True
        q.put(0)
        while q.empty() is False:
          u = q.get()
          print(u, end = " ")
          for i in range(self.nVertices):
            if self.adjMatrix[u][i] > 0 and visited[i] is False:
              q.put(i)
              visited[i] = True
    
    
v, e = [int(x) for x in input().split()[:2]]    
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a,b)
g.bfs()