from random import randrange
import time
from datetime import datetime

#buble
my_list = [ randrange(0, 15) for i in range(10) ]
import sys

max_list = len( my_list )
class Graph(): 

i = 0
while i < max_list:
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    j = 0
    while j < max_list-i-1:
    def printMST(self, parent): 
        print ("Prima algoritm")
        print ("Edge \tWeight")
        for i in range(1, self.V): 
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ]) 

        if my_list[ j ] > my_list[ j + 1 ]:
    def minKey(self, key, mstSet): 
        min = sys.maxsize 
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
        return min_index 

            my_list[ j ], my_list[ j + 1] = my_list[ j + 1], my_list[ j ]
        j+=1
    i += 1
    def prima_Algoritm(self): 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V 
        parent[0] = -1 

print( my_list )
        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
            mstSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
        self.printMST(parent) 


g = Graph(8) 
g.graph = [ [0, 8, 0, 8, 7, 0, 0, 0], 
            [8, 0, 2, 0, 0, 1, 0, 0], 
            [0, 2, 0, 0, 0, 9, 0, 1], 
            [8, 0, 0, 0, 9, 0, 6, 0], 
            [7, 0, 0, 9, 0, 0, 7, 10],
            [0, 1, 9, 0, 0, 0, 0, 6],
            [0, 0, 0, 6, 7, 0, 0, 2],
            [0, 0, 1, 0, 10, 6, 2, 0]]

from datetime import datetime
start_time = datetime.now()
# do your work here
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) 
g.prima_Algoritm();


from collections import defaultdict 

class Graph: 

    def __init__(self,vertices): 
        self.V= vertices
        self.graph = []

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def Kruskal_Algorithm(self): 
        result =[]
        i = 0 
        e = 0 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parent = [] ; rank = [] 

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
        print ("Kruskal algoritm")
        for u,v,weight  in result: 
            print ("%d -- %d == %d" % (u,v,weight)) 

g = Graph(8) 
g.addEdge(0, 1, 8)
g.addEdge(0, 3, 8)
g.addEdge(0, 4, 7)
g.addEdge(1, 2, 2)
g.addEdge(1, 5, 1)
g.addEdge(2, 5, 9)
g.addEdge(2, 7, 1)
g.addEdge(3, 4, 9)
g.addEdge(3, 6, 6)
g.addEdge(4, 6, 7)
g.addEdge(4, 7, 10)
g.addEdge(5, 7, 6)
g.addEdge(6, 7, 2)

g.Kruskal_Algorithm () 
