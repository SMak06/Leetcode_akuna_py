class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1
        
        #creating an adjacency list out of the given list  
        graph = defaultdict(set)
        for u,v in (connections):
            graph[u].add(v)
            graph[v].add(u)
            
        numberOfConnections = 0 #this keeps track of the separate components
        visitedNodes = set() #this keeps track of the vertex that have been visited
        
        
        #Depth First Search Function
        def dfs(node):
            if node in visitedNodes:
                return 0
            visitedNodes.add(node)
            for i in (graph[node]): #traversing each neighbor vertex of the root in one go and add them to visited
                dfs(i)
            return 1
        
        # loop to check the no. of vertex which can be visited from each i
        for i in range (n): 
            numberOfConnections += dfs(i) #every un-visited vertex will be a new separate component
        
        return numberOfConnections - 1 #we need n-1 cables to connect n separate components