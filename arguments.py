
#default arguments
print("Default arguments")
def person(name,age=24):
    print("Name: ",name)
    print("Age: ",age)
person('navin')
print()

#keyword arguments
print("keyword arguments")
def person(name,age):
    print("Name: ",name)
    print("Age: ",age)
person(age=55, name="Yash")