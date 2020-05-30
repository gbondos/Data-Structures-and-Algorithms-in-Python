from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def dfsHelper(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for i in self.graph[node]:
            if i not in visited:
                self.dfsHelper(i, visited)

    def dfs(self):
        visited = set()
        self.dfsHelper(5, visited)

def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(4, 3)
    # adding below edge gives a disconnected graph
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(6, 8)
    g.addEdge(6, 7)
    g.addEdge(6, 5)
    g.addEdge(7, 5)
    g.addEdge(8, 6)
    g.addEdge(7, 6)

    g.dfs()

main()
