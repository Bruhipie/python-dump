num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

print("\nSelect what you want to do with the numbers:\n\
1. Add\n\
2. Subtract (num1-num2)\n\
3. Divide (num1/num2)\n\
4. Multiply\n\
")

choice=int(input("Enter your choice: "))

if choice==1:
    a=num1+num2
elif choice==2:
    a=num1-num2
elif choice==3:
    a=num1/num2
elif choice==4:
    a=num1*num2
print(a)
