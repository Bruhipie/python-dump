string=str(input("Enter a sentence: "))
vowel=lower=upper=consonant=0
vow=['a','e','i','o','u','A','E','I','O','U']
for i in string:
    if i in vow:
        vowel+=1
    if i not in vow and (i>'A' and i<='z'):
        consonant+=1
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("There are", vowel, "vowels", consonant, "consonants", upper, "uppercase and", lower, "lowercase characters")
