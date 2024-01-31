string=str(input("Enter a string with digits: "))
sum=0
for i in string:
    if i.isdigit():
        sum+=int(i)
print("The sum of digits in the string is: ", sum)