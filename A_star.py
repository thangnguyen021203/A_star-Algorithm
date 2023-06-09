class Graph():
    
    def __init__(self, veritices):
        self.V = veritices
        self.adjacent = [[0 for columns in range (self.V)] for rows in range (self.V)]
        self.h = [0 for i in range (self.V)]
    
    #function heristic evalute a node follow to: destination - node_index
    def heuristic(self, destination, h):
        for i in range (self.V):
            h[i] = (destination - i) if destination > i else i-destination

    #Choose a node in open_list with the least f(x) = g(x) + h(x) to expand
    def Pick_to_Move(self, g, h, open_list, close_list, path):
        if len(open_list) == 0:
            print("Fault!")
            return
        min = h[open_list[0]] + g[open_list[0]]
        min_vertice = 0
        for i in open_list:
            if min > h[i] + g[i]:
                min = h[i] + g[i]
                min_vertice = i
        open_list.remove(min_vertice)
        close_list.append(min_vertice)
        path.append(min_vertice)
        return min_vertice
        
    def print(self, source, destination, path):
        print("Path from " + str(source) + " to " + str(destination) + ":")
        for i in range (path):
            print("Step " + str(i) + ": " + str(path[i]))
    
    def A_Star(self, source, destination):
        
        self.heuristic(destination, self.h)
        open_list = [source]
        path = [source]
        close_list = []
        g = [0] * self.V
        
        u = self.Pick_to_Move(g, self.h, open_list, close_list, path)
        
        for  i in range (self.V):
            if self.adjacent[u][i] > 0 and open_list.count(i) == 0 and close_list.count(i) == 0:
                if g[i] > g[u] + self.adjacent[u][i]:
                    g[i] = g[u] + self.adjacent[u][i]
                open_list.append(i)
                if i == destination:
                    path.append(i)
                    open_list.clear
                    close_list.clear
                    return
        print(source, destination, path)

g = Graph(6)
g.adjacent = [[0,4,0,2,0,0],
              [4,0,5,0,0,0],
              [0,5,0,3,1,3],
              [2,0,3,0,0,8],
              [0,0,1,0,0,3],
              [0,0,3,8,3,0]]
g.A_Star(0,5)        
        