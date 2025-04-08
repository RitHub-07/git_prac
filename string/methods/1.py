text="Python"
print(text.upper())

language=len("Python")
print(language)

text="PYTHON"
print(text.lower())

text="it is a python programming"
print(text.title())

text="Hello World"
print(text.replace("World","Ritul"))

text="Python programming is very interesting"
print(text.split())

#strip() Method
text="          Python Programming  "
print(text)
print(text.strip())
print(text.lstrip())
print(text.rstrip())

text="     This is a pen      "
print(text)
print(text.upper())
print(text.lower())
print(text.replace("pen","book"))
print(text.strip())
print(text)

#find() Method
text="Pythonotyt"
print(text.find("t")) 
print(text.find("z"))

str="hello"
str[2]="m"
print(str)

text="banana apple banana apple"
count_banana=text.count("banana")
print(count_banana)

text="Hello, India!"
print(text.startswith("Hello"))

text="Hello and Welcome"
print(text.endswith("Welcome"))
