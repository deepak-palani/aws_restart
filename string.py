mystring="this is a string msg"
print(mystring)
print(type(mystring))
print(mystring+" this is string type "+str(type(mystring)))

#string concatenation 
first="good"
second="morning"
third=first+" "+second
print(third)

#input string

name=input("what is your name :")
print(name)

#Formatting output strings
color=input("enter your favorite color ?")
animal=input("what is your favorite animal ?")
print("{},you like {} {} !!".format(name,color,animal))