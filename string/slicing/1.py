'''#--------------string--------------------------------
str1="hello"
str2="world"
print(str1+" "+str2)

txt="hi"
print(txt*3)

#-------slicing----------------------------------------
AB="Python"
print(AB[3])
str="Python"
print(str[0:3])
print(str[0:5])
print(str[3:5])
print(str[0:])
print(str[:3])
print(str[:])
print(len(str))

#-------------Gap Slicing-----------------------------
A="PythonProgramming"
print(A[0::2]) 
print(A[1::4])     
print(A[::])     
print(A[::-1])     
print(A[:-1]) 
print(A[:-6]) 
print(A[0:5:1])
print(A[::-1])
print(A[0:13:2])'''

# 3 parametr gap slicing
A="PythonProgramming"
print(A[0:5:1])
print(A[::-1])
print(A[0:13:2])     
print(A[0:16:2])
print(A[::-1])
print(A[0::4])