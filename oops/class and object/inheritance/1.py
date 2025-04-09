# oop type single inheritance
class parent:
    def first(self):
        print("This Is First")
class child(parent):
    def second(self):
        print("This Is Second")
obj=child() 
obj.first()
obj.second()        

# oop type multiple inheritance
class parent1:
    def first(self):
        print("This Is First")
class parent2:
    def second(self):
        print("This Is Second")
class child(parent1,parent2):
    x = 10
obj=child()
print(obj.x) 
obj.first()
obj.second()

# oop type multilevel inheritance
class Grandfather:
    def first(self):
        print("This Is First")
class father(Grandfather):
    def second(self):
        print("This Is Second")
class son(father):
    x=10
    y=20
obj=son()
obj.first()
print(obj.x)
obj.second()
print(obj.y)

# oop type hierarchical inheritance
class father:
    def first(self):
        print("This Is First")
class son1(father):
    def second(self):
        print("This Is Second")
class son2(father):
    x=19
    y=20
obj1=son1()
obj1.first()
obj1.second()

obj2=son2()
obj2.first()
print(obj2.x)
