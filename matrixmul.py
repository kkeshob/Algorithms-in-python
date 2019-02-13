def matinp():
    r=int(input("Enter the row size:"))
    c=int(input("Enter the column size:"))
    mat=[]
    for i in range(0,r):
        row=[]
        print(i,"row")
        for j in range(0,c):
            print("Enter column",j,"value:")
            row.append(int(input()))
        mat.append(row)
    return mat

def matshow(mat):
    for i in mat:
        print(i)

def matmul(m1,m2):
    mat=[]
    for i in range(len(m1)):
        row=[]
        for j in range(len(m2[0])):
            row.append(0)
        mat.append(row)

    for i in range(0,len(m1)):
        for j in range(0,len(m2[0])):
            for k in range(0,len(m2)):
                mat[i][j]=mat[i][j]+ m1[i][k]*m2[k][j]
    return mat
 
a=matinp()
b=matinp()
m=matmul(a,b)
matshow(m)
