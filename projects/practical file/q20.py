L=eval(input("Enter a list of 2-element-tuples: "))
n=len(L)
for i in range(1,n):
    j=i
    while j>0 and L[j][1] < L[j-1][1]:
        L[j],L[j-1]=L[j-1],L[j]
        j=j-1
print("Sorted List:", L)