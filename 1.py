print("gjkjl")
print("vhcgfydtcfgvjbhnj")

'''def sqr(x):
    return x * x
print(sqr(5))

def Addition(*args):
   print(sum(args))
print(Addition(1, 2, 3, 4))

tup=(2,1,2,3,4,2,6)
print(tup.count(2))
print(tup.index(3))'''

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
