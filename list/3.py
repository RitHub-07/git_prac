# ----------if else statement-----------
a=int(input("entr no: "))
b=int(input("entr no: "))
if(a>b):
  print("a is greater")
else:
  print("b is greater")

#----------if statement---------------
marks=int(input("Enter Marks: "))
if(marks>60):
  print("First divison")
if(marks>45):
  print("Second divison")
if(marks>30 or marks>45):
  print("Third divison")

# #------if elif else statement----
# a=int(input("entr no: "))
# b=int(input("entr no: "))
# c=int(input("enter no: "))
# if(a>b and a>c):
#   print("a is greater")
# elif(b>a and b>c):
#    print("b is greater")
# else:
#   print("c is greater")

#---------Nested-if-----------
income=int(input("Enter Your Income: "))
credit_score=int(input("Enter Your Credit Score: "))
emp_status="employed"
if(income>=40000):
  if(credit_score>=650):
    if(emp_status=="employed"):
     print("YOU ARE ELIGIBLE FOR LOAN!") 
    else:
     print("You Need to be Employed to get Loan")
  else:
   print("Your credit score is too low for Loan")
else:
 print("Your income is too low to qualify for the loan")

# #  --------odd even--------
# x=int(input("Enter No: "))
# if(x%2==0):
#  print("ITS EVEN")
# else:
#  print("Its ODD")

# # write a pogram to determine leap year using if else
# year=int(input("Enter Year: "))
# if(year%4==0 and year%100!=0 or year%400==0 ):
#  print("ITS A LEAP YEAR...")
# else:
#  print("Not A Leap YEAR")

# my_list=[1,33,44,5,6]
# for x in my_list:
#   print(x)

#conditional Statement
a=10
b=3
if(a>b):
  print("a is greater")
else:
  print("b is greater")

  #Write a program in if else using input function to check your eligibility for vote
age=int(input("Enter Your Age: "))
print("Age",age)
if(age>=18):
  print("You are eligible for VOTE")
else:
  print("You are not eligible for VOTE")