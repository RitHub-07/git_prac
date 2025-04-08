'''# ------------------------- dict-----------------------
Student={"name":"uv","roll":10,"email":"uv@gmail.com"}
print(Student)

#----------------------boolean------------------------
is_py_esy=True
print(is_py_esy)

#---------------------None-----------------------------
nothing=None
print(nothing)

#---------------------Set-----------------------------
uni_no={1,2,3,4,4}
print(uni_no)

#-----------------frozenset----------------------------
frozen_no=frozenset({1,2,3})
print(frozen_no)

#-----------------floor divison------------------------
a=22
b=3
print(a//b)

#----------------Exponential----------------------------
a=10
b=2
print(a**2,a**b)

#-----------input()_func---------------------------------
f_name=input("enter name: ")
l_name=input("enter name: ")
age=input("enter age: ")
print("Your Full Name Is: Your Age: ",f_name,l_name,age)

#--------indentation-------------------------------------
def first_func():
  print("This is Your first_function")
first_func()

#--------Relational Operators----------------------------
a=7
b=5
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)

#--------Bitwise Opr---------------------------------------
a=10
b=3
print(a&b)
print(a|b)

#---------logical-------------------------------------------
x=True
y=False
print()



#---------------Xor--------------------------------------
a=10
b=3
print(a^b)

#---------------bit not opr--------------------------
a=10
b=3
print(~a)
print(~b)

#----------------left shift-----------------------------
a=10
b=3
print(a<<2)
print(a>>2)

#----------------assignment opr--------------------------
a=10 
print("a=",a)
a+=5
print("a+=5->",a)
a-=3
print("a-=3",a)
a*=2
print("a*=2",a)
a/=2
print("a/=2",a)
a%=2
print("a%=4",a)
a=20
a//=3
print("a//2",a)

#---------------identity opr ---------------
a=10
b=10
c=[1,2,3]
d=[1,2,3]
print(a is b)
print(c is d)
print(c is not d)

#--------------membrship opr-----------------------------
a=(1,2,3,4)
print("3 in a",3 in a)
print("6 in a",6 in a)
print("6 not in a",6 not in a)

str= "this is the book"
a=2'''