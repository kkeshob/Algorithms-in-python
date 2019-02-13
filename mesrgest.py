def merge(a1,a2):
    a3=[]
    m=len(a1)
    n=len(a2)
    i=0
    j=0
    while i<m and j<n :
        if a1[i]<a2[j]:
            a3.append(a1[i])
            i=i+1
        else:
            a3.append(a2[j])
            j=j+1
    while i<m:
        a3.append(a1[i])
        i=i+1
    while j<n:
        a3.append(a2[j])
        j=j+1
    return a3
def split(arr):
    if len(arr)>1:
        mid=len(arr)//2
        a1=split(arr[:mid])
        a2=split(arr[mid:])
        arr=merge(a1,a2)
    return arr

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
arr=split(arr)
print("After Merge Sort\n",arr)
