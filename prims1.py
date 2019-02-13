#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:18:07 2019

@author: keshob
"""
import random
class graph:
    def __init__(self):
        self.vertex=[]
        self.edges=set()
    def addedge(self,w,s,d):
        self.edges.add((w,s,d))        
    def printgraph(self):
        print("Vertices:",self.vertex)
        print("Edeges:",self.edges)
def stedge(edeges,v,nv):
    edg=[]
    for node in v: 
        for eg in edeges:
            if eg[1]==node and eg[2] in nv or eg[2]==node and eg[1] in nv:
                edg.append(eg)
    if edg==[]:
        return ()
    else:
        edg.sort()
        return edg[0]
def prim(gr):
        visited=[]
        notvisited=gr.vertex
        msteg=[]
        egs=list(gr.edges)
        rv=random.choice(gr.vertex)
        visited.append(rv)
        notvisited.remove(rv)
        while notvisited !=[]:
            edge=stedge(egs,visited,notvisited)
            if edge not in egs:
                break
            msteg.append(edge)
            
            egs.remove(edge)
            if edge[2] in visited:
                visited.append(edge[1])
                notvisited.remove(edge[1])
            else:
                visited.append(edge[2])
                notvisited.remove(edge[2])
        mst=graph()
        mst.vertex=visited
        mst.edges=msteg
        return mst
a=graph()
a.vertex=["A","B","C","D","E","F","G"]
a.addedge(7,"A","B")
a.addedge(5,"A","D")
a.addedge(8,"B","C")
a.addedge(7,"B","E")
a.addedge(9,"B","D")
a.addedge(5,"C","E")
a.addedge(15,"D","E")
a.addedge(6,"D","F")
a.addedge(8,"E","F")
a.addedge(9,"E","G")
a.addedge(11,"F","G")
print("Entered Graph");
a.printgraph()
mst=prim(a)
print("Using Prims Algorithm The Minimum Spanning tree:")
mst.printgraph()
