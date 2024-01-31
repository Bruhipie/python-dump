string=str(input("Enter a string with digits and alphabets: "))
d={}
for i in string:
	if i.isalnum()!=True:
		continue
	elif i not in d:
		d[i]=string.count(i)
	else:
		continue
print(d)