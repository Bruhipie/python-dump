students=()
for i in range(1,6):
    print("Enter marks of Student", i)
    m1,m2,m3=eval(input("Enter marks in subject 1,2,3: "))
    students+=((m1,m2,m3),)
    print("Total marks obtained by Student", i, "is:", m1+m2+m3)
    print("Average marks obtained by Student", i, "is:", (m1+m2+m3)/3, "\n")
print(students)
