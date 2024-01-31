L1=eval(input("Enter a list: "))
L2=eval(input("Enter a list of similar size: "))
for i in range(len(L1)):
    if L1[i]==L2[i]:
        continue
    else:
        print("The lists differ at the index number", i)
        break