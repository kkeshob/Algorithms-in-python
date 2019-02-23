#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 06:33:16 2019

@author: keshob
"""
def knapsac(pr,wg,sac):
    pdw=[]
    n=len(pr)
    item=[]
    i=0
    while i<n:
        pdw.append(pr[i]/wg[i])
        item.append(0)
        i=i+1
    temp=pdw.copy()
    while sac>0:
        itemno=temp.index(max(temp))        
        if wg[itemno]<=sac:
            item[itemno]=1
            sac=sac-wg[itemno]
        else:
            item[itemno]=sac/wg[itemno]
            sac=sac-item[itemno]*wg[itemno]
        temp[itemno]=0
    mp=0
    for i in range(0,n):
        mp=mp+pr[i]*item[i]    
    print("Weight    Profit    Pi/Wi        Xi")
    print("____________________________________")
    for i in range(0,n):
        print("  ",wg[i],"      ",pr[i],"      ",round(pdw[i],2),"      ",round(item[i],2))
    print("Hence Maximum Profit=",mp)

print("Enter How many Items:", end="")
n=int(input())
profit=[]
weight=[]
for i in range(0,n):
    print("Enter the Weight of item no-",i,":", end="")
    weight.append(int(input()))
    print("Enter the Profit of item no-",i,":", end="")
    profit.append(int(input()))
print("Enter the height Sac Size:", end="")
s=int(input())
knapsac(profit,weight,s)

























