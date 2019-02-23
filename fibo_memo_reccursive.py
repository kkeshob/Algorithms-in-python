#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:41:00 2019

@author: keshob
"""

def fibo(n):    
    fibseries = [0, 1]  
    while len(fibseries) < n + 1:  
        fibseries.append(0)  
      
    if n <= 1:  
        return n  
    else:  
        if fibseries[n - 1] == 0:  
            fibseries[n - 1] = fibo(n - 1)  
  
        if fibseries[n - 2] == 0:  
            fibseries[n - 2] = fibo(n - 2)  
              
    fibseries[n] = fibseries[n - 2] + fibseries[n - 1]  
    return fibseries[n]
n=int(input("How Many Fibonacci Number:"))
for i in range(0,n):
    print(fibo(i),end=",")  
      