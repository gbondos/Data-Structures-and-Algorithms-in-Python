from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, v):
        q = []
        visited = set()
        q.append(v)
        visited.add(v)
        
        while q:
            current = q.pop(0)
            print(current, end=" ")
            for i in self.graph[current]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
    
    
def main():
    g = Graph()
    g.addEdge(10, 1)
    g.addEdge(10, 4)
    g.addEdge(1, 10)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 10)
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
    # g.addEdge(10, 5)

    g.bfs(10)
    print()

main()
