import sys,threading
import networkx as nx
input=sys.stdin.readline
def solve():
    n=int(input())
    pts=[tuple(map(int,input().split())) for _ in range(n)]
    G=nx.Graph()
    G.add_nodes_from(range(1,n+1))
    for i in range(n):
        x1,y1=pts[i]
        for j in range(i+1,n):
            x2,y2=pts[j]
            G.add_edge(i+1,j+1,weight=abs(x1-x2)+abs(y1-y2))
    m=nx.max_weight_matching(G,maxcardinality=True)
    for a,b in m:print(a,b)
def main():
    t=int(input())
    for _ in range(t):solve()
threading.Thread(target=main).start()

