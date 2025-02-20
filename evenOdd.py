def isOdd (a):
   

    if a%2 == 0:
        return False
    else:
        return True
    
a = int(input("Enter the number: "))
ans = isOdd(a)
print("The Entered number isOdd: ", ans)