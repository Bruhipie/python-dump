## Sub-Part (a)
print("Printing Letter Pattern:\n")
for i in range(5):
    for j in range(i+1):
        print(chr(69-j), end=' ')
    print()

## Sub-Part (b)
print("\nPrinting Star Pattern:\n")
n=3
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (i + 1))
