phone_dict=eval(input("Enter name-phone number dictionary: "))

#Sub-Part (a)
print(phone_dict, '\n')

#Sub-Part (b)
name=str(input("Enter the name of a new person: "))
num=int(input("Enter their phone number: "))
phone_dict[name]=num
print("Modified Dictionary:", phone_dict, '\n')

#Sub-Part (c)
name=str(input("Enter name to be removed: "))
phone_dict.pop(name, "Person not found!\n")
print(phone_dict, '\n')

#Sub-Part (d)
name=str(input("Enter name whose number is to be modified: "))
num=int(input("Enter new phone number: "))
phone_dict[name]=num

#Sub-Part (e)
name=str(input("Enter name to be searched: "))
if name in phone_dict:
    print("Name found! Their number is: ", phone_dict[name], '\n')
else:
    print("Name not found!\n")

#Sub-Part (f)
tup=list(phone_dict.items())
n=len(tup)
for i in range(n):
    for j in range(0,n-i-1):
        if tup[j][0] > tup[j+1][0]:
            tup[j],tup[j+1]=tup[j+1],tup[j]
phone_dict.clear()
for i in tup:
    phone_dict[i[0]]=i[1]
print("Sorted Dictionary: ", phone_dict)

