L=eval(input("Enter a list: "))
elm=eval(input("Enter the number to removed: "))
count=L.count(elm)
for i in range(count):
    L.remove(elm)
print(L)