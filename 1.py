'''print("gjkjl")
print("vhcgfydtcfgvjbhnj")

def sqr(x):
    return x * x
print(sqr(5))

def Addition(*args):
   print(sum(args))
print(Addition(1, 2, 3, 4))

tup=(2,1,2,3,4,2,6)
print(tup.count(2))
print(tup.index(3))

# dictionary
std={
  "name":"ritul",
  "age":20,
  "roll":10
}
new_std=std.copy()
print(new_std)
print(std.get("name"))

print(std.keys())

print(std.items())
print(std.values())

print(std.update({"age":25}))

# oop
class car:
    def _init_(self,brand,colur):
     self.brand=brand
     self.colur=colur
     print("Intializer is Called")
def drive(self):
    print(self.brand)
    print("drive")

my_car=car("Toyoyta","Red")
my_car.drive()

# intro using dictionary
my_intro = {
    "Name": "Ritul",
    "Father's Name": "Vipin Kumar",
    "Class": "B.tech CSE",
    "Roll No": 10,
    "Belong": "Sirsa, Haryana, India"
}
print("Name:", my_intro["Name"])
print("Father's Name:", my_intro["Father's Name"])
print("Roll No:", my_intro["Roll No"])
print("Class:", my_intro["Class"])
print("Belong:", my_intro["Belong"])

# Star Pattern
for i in range(1,5):
  for j in range(1,5):
    print("*",end="") 
  print() ''' 

# star ptrn right side
for i in range(1,5):
  for j in range(1,5):
    if(j<i+1):
      print("*",end="") 
    else:
      print("",end="") 
  print()

# str ptrn dwn sde
for i in range(1,5):
  for j in range(1,5):
    if(j<=5-i):
      print("*",end="") #same output
    else:   
      print("",end="")    
  print() 

# st ptrn lft dwn sde
for i in range(1,5):
  for j in range(1,5):
    if(j>=i):
      print("*",end="") #have same output
    else:   
      print("",end="")
  print() 

# str pttn pyramide 
for i in range(1,6):
  for j in range(1,10):
    if(j>=6-i and j<=4+i):
      print("*",end="")
    else:   
      print(" ",end="")   
  print()

# str pttn pyramide dwn side
for i in range(5,0,-1):
  for j in range(1,10):
    if(j>=6-i and j<=4+i):
      print("*",end="")
    else:   
      print(" ",end="")   
  print() 

# common prgrm to call fxn thogh object
class parent:
    def first(self):
        print("Hii Ritul")
obj=parent()
obj.first()

  
