string=str(input("Enter a sentence: "))
reverse=string[::-1]
if string==reverse:
    print("The sentence is a Palindrome")
else:
    print("The string is not a Palindrome")