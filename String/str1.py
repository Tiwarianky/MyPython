str="String is a data type that stores a sequence of charecters.\n And we can perform several operation on it"
a="Ankit "
b="Tiwari"
print(a+b) #concatenation of Strings---
print(len(a)) #to check length of string
print(a[3])  #to access charecters by index

#Slicing: accessing part  of string
print(a[0:len(a)])
print(a[0:2]) 
print(a[0:])  #consider till last index of string itself
print(a[:5])  #cosider from starting index itself

#Negative indexing(Python have also negativeor backword indexing)------
print(a[-3:])