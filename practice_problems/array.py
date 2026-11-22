#practice array's list
import array as arr
a=arr.array('i',[])
s=0
for i in range(7):
    num=int(input("enter a number to store in the array:"))
    a.append(num)
    s+=num
    m=0
    if num>m:
        m=num
print("Maximum element in the array is:", m)
print("Sum of the array elements is:", s)

#practice
