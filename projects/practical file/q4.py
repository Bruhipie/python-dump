import math
x=float(input("Enter value of x: "))
n=int(input("Enter another number: "))
sum1=sum2=1
sum3=count=sum4=0

#First Series
for i in range(1,n+1):
    sum1+=x**i
print("Sum of first series is: ", sum1)

#Second Series 
for i in range(1,n+1):
    if count%2==0:
        sum2-=x**i
    else:
        sum2+=x**i
    count+=1
print("Sum of second series is: ", sum2)

#Third Series
for i in range(1,n+1):
    sum3+=(x**i)/i
print("Sum of third series is: ", sum3)

#Fourth Series
for i in range(1,n+1):
    sum4+=(x**i)/math.factorial(i)
print("Sum of fourth series is: ", sum4)