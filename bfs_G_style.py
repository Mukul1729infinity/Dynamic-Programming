from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def Bfs(self,s):
        vis=[]
        bfs=[]
        Q=[]
        Q.append(s)
        while Q:
            a=Q.pop(0)
            vis.append(a)
            bfs.append(a)
            for i in self.graph[a]:
                if i not in vis:
                    vis.append(i)
                    Q.append(i)
        print(bfs)
g=graph()
g.addedge(1,2)
g.addedge(2,3)
g.addedge(3,4)
g.addedge(2,7)
g.addedge(3,5)
g.addedge(7,5)
g.addedge(5,8)
g.addedge(5,6)
g.Bfs(1)
            
