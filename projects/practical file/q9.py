L=["Hi",123,"How",234,"Are You?",901]
print("\nSelect what you want to do with the list:\n\
1. Insert Elements\n\
2. Remove Elements")
print("Current List: ", L, "\n")
choice=int(input("Enter your choice: "))

if choice==1:
    index=int(input("Enter the index where to add the element: "))
    element=eval(input("Enter the element: "))
    L.insert(index,element)
    print(L)

elif choice==2:
    print("How do you want to remove element:\n\
    1. By index\n\
    2. By element\n\
    3. By List Slice")
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        ind=int(input("Enter index to be removed: "))
        L.pop(ind)
    elif ch==2:
        elm=eval(input("Enter element to be removed: "))
        L.remove(elm)
    elif ch==3:
        start=int(input("Enter starting index: "))
        end=int(input("Enter last index (not included): "))
        del L[start:end]
    else:
        print("Enter a valid choice! Exiting..")
    print(L)

else:
    print("Enter a valid choice! Exiting..")