class Graph:
    def __init__(self,nVertices):
        self.nVertices= nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
    def __dfsHelper(self,sv,visited):
        print(sv,end=" ")
        visited[sv]=True
        for i in range(self.nVertices):
            if (self.adjMatrix[sv][i]>0 and visited[i] is False):
                self.__dfsHelper(i,visited)
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0,visited)
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return 
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    def __str__(self):
        return str(self.adjMatrix)


def main():
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(2,3)
    g.addEdge(0,2)
    g.dfs()



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()