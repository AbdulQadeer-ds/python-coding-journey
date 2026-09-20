lst=[]
for i in range(4):
    lst.append(int(input("enter a namber:")))
    print(lst)
    s=0
    for i in lst:
        s+=i
        print("sum of the nambers is:",s)