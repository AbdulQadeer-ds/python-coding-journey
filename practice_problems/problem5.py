lst=[]
for i in range(7):
    lst.append(int(input("enter a namber")))
tple=tuple(lst)
print(tple)

#practice 1
lst=[]
for i in range(6):
    lst.append(int(input("enter a number")))
tple=tuple(lst)
print("This is the sum of the tuple:",str(tple))
s=0
for i in tple:
    s+=i
print("This is the sum of the tuple:",str(s))
