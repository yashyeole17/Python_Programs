
# .Write a program which will accept age as an input from the user and check whether the user is
# eligible for permanent driving license or not. If age < 18 and 'NOT' having learning license , it
# should raise the exception as ‘Not eligible ’.
class NotEligible(Exception):
    pass

age = int(input("Enter Age:"))
if(age>=18):
    print("Eligible for permanat driving license")
else:
    raise NotEligible("Not Eligible")