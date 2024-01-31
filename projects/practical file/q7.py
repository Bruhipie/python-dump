string=str(input("Enter a string: "))
alt_caps=''
count=1
for i in string:
    if count%2==0:
        alt_caps+=i.upper()
    else:
        alt_caps+=i
    count+=1
print(alt_caps)