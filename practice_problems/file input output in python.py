#read a file
'''f=open("problem11.py","r")
data=f.read()
print(data)
f.close()

#append a file
f=open("problem11.py","a")
f.write("I am learning in Alghazali University")
f.close()'''

#
f=open("first.py","r+")
f.write("my name is abdul qadeer")
f.close()

#open i/o 
f=open("first.py","+r")
f.write("abc")
print(f.write)
f.close()


