def knapsac(pr,wg,sac):
    n=len(wg)
    k=[]
    for i in range(0,n):
        r=[]
        for j in range(0,sac+1):
            r.append(0)
        k.append(r)
    for i in range(0,n):
        for w in range(0,sac+1):
            if i==0 and w==0:
                k[i][w]=0
            elif wg[i]<=w:
                k[i][w]=max(pr[i]+k[i-1][w-wg[i]],k[i-1][w])
            else:
                k[i][w]=k[i-1][w]
    return k

print("Enter How many Items:", end="")
n=int(input())
profit=[]
weight=[]
for i in range(0,n+1):
    if i==0:
        weight.append(0)
        profit.append(0)
    else:
        print("Enter the Weight of item no-",i,":", end="")
        weight.append(int(input()))
        print("Enter the Profit of item no-",i,":", end="")
        profit.append(int(input()))
print("Enter the height Sack Size:", end="")
s=int(input())
m=knapsac(profit,weight,s)
for i in m:
    print(i)
print("Hence Maximum Profit Is:",m[4][8])
























