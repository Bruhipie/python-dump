num=int(input("Enter a number to be checked: "))

##Palindrome
wnum=num
rev=0
while wnum>0:
    dig=wnum%10
    rev=rev*10+dig
    wnum=wnum//10
if num==rev:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")    

##Perfect Number
sum=0  
for i in range(1,num):  
    if num%i==0:  
        sum+=i  
if sum==num:  
    print("The number is a Perfect Number")  
else:  
    print("The number is not a Perfect Number")
sum=0

##Armstrong Number
n=len(str(num))
for i in str(num):
    sum+=int(i)**n
if sum==num:
    print("The number is an Armstrong Number")  
else:
    print("The number is not an Armstrong Number")
