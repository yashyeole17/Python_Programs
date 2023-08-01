# Normal division using function
def div(a,b):
    if a < b:
        a,b=b,a
    print("Normal Division: ",a // b)
div(11,55)

def divi(a,b):
    print(a // b)

def smart(a,b):
    def inner(func):
        if  a < b :
            a,b = b,a
        return func(a,b)
    return inner
divi(88,11)

