n=5
for i in range(6):
    for j in range(6):
        print("*",end="")
    print()


n=5
for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()


n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

n=6
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()
    break


#practice
# 
n=6 
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()
        


    



