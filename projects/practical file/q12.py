num_list=eval(input("Enter a list of numbers: "))
print(num_list)
avg=sum(num_list)/len(num_list)
elm=int(input("Enter number to be searched: "))
if elm in num_list:
    index=num_list.index(elm)
    print("The element exists at index", index)
else:
    print("Element not found!")
print("The average of these numbers is: ", avg)