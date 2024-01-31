L=[(1,"Google",999999),(2,"Levi's",0),(3,"Hilfiger",300000),(4,"Tommy",10000),(5,"Sam",9999999999)]
for i in range(len(L)):
    for j in range(0,len(L)-i-1):
        if L[j][2] < L[j+1][2]:
            L[j],L[j+1]=L[j+1],L[j]

## using for loop otherwise output would be small in size
for i in L:
    print(i)
