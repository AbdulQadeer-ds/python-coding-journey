import array as arr


'''scoure=arr.array('i',[54,4,43,54])
scoure.append(54)
scoure.insert(1,543)
scoure.pop(0)
scoure.reverse()
scoure.index(4)
possition=scoure.index(54)
scoure[3]=900
new_scoure=arr.array('i',[54,65,54,54666,444,])
scoure.extend(new_scoure)
slice_array=scoure[0:5]

print(scoure)
print(possition)
print(slice_array)
element_size=scoure.itemsize
print(element_size)

coure=arr.array('i',[54,4,43,54])
slice_array=coure[0:3]
print(slice_array)



nums=arr.array('i',[3,34,55,43,6,54,56,65,76,5435])
element_size=nums.itemsize
print(nums)#'''

nums=arr.array('i',[4,54,64,35,64,64,43,6,777,55,])
nums.append(666)
nums.insert(1,6555)
my_lst=nums.tolist()
print(my_lst)

# get 5 number from the user
# store in the array and display 
# find their sum 

'''import array as arr

a = arr.array('i',[])
s = 0
for i in range(5):#0 to 4 
    a.append(int(input("Enter a number to store in the array")))
for j in range(5):#0 to 4 
    print(a[j])
    s += a[j] # 2,3,4,5,6,7
print("Sum of the number is = "+str(s))'''


#array import
import array as arr
a=arr.array('i',[])
s=0
for i in range(5):
    num=(int(input("Enter a namber to store in the array:")))
    a.append(num)
    s+=num
print(s)

#practice
import array as arr
a=arr.array('i',[])
s=0
for i in range(4):
    num=(int(input("Enter a namber")))
    a.append(num)
    s+=num
print(s)

#practice
import array as arr






