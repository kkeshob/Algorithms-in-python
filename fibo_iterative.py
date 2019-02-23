#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:41:00 2019

@author: keshob
"""

def fibo(n):    
    fibseries = [0, 1]  
    while len(fibseries) < n:  
        fibseries.append(0)  
      
    if n <= 1:  
        return n  
    else:  
        for i in range(2,n):
            fibseries[i] = fibseries[i-2] + fibseries[i - 1]  
    return fibseries
n=int(input("How Many Fibonacci Number:"))
print(fibo(n))    