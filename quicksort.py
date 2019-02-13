#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:24:28 2019

@author: keshob
"""

def partition(arr,low,heigh):
    pivot=arr[low]
    i=low+1
    j=heigh
    while i<=j:
        while arr[i]<pivot:
            i=i+1
        while arr[j]>pivot:
            j=j-1
        if i<j:
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t
    t=arr[j]
    arr[j]=arr[low]
    arr[low]=t
    return j   
def qsort(arr,low,heigh):
    if low <heigh:
        pos=partition(arr,low,heigh)
        qsort(arr,low,pos-1)
        qsort(arr,pos+1,heigh)
def inp():
    a=int(input("Enter How Many Items:"))
    i=0
    arr=[]
    while i<a:
        arr.append(int(input("Enter Number:")))
        i=i+1
    return arr
arr=inp()
print("Before Merge Sort\n",arr)
qsort(arr,0,len(arr)-1)
print("After Merge Sort\n",arr) 