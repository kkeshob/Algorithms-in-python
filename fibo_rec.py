#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:20:52 2019

@author: keshob
"""
def fibo(n): 
    if n<0: 
        print("Wrong Input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fibo(n-1)+fibo(n-2) 
n=int(input("How Many Fibonacci Number:"))
for i in range(0,n):
    print(fibo(i),end=",")