"""

f = lambda a:a**a
result = f(5)
print(result)



nums = [3,2,5,7,6,8,9,1]
evens = list(filter(lambda n: n % 2 == 0, nums))
du = list(map(lambda n: n, evens))
print(evens)
print(du)


def div(a,b):
    if b>a:
        a,b = b,a
        print(a//b)
    else:
        print(a // b)
div(2,5)



def div(a,b):
    print(a//b)
def smart_div(fun):
    def inner(a,b):
        if a < b:
            a, b= b, a
        return fun(a,b)
    return inner
v=smart_div(div)
v(2 ,8)





import re
pattern =r'^a..s$'
test="ass"
result = re.match(pattern, test)
if result:
    print("Yes")
else:
    print("NO")


import re
one = "i am a boy for m np"
match = re.findall(r"..", one)
print(match)
"""

import re
pattern = r"(\d{4})-(\d{2})-(\d{2})"
test = "4444-04-44"
match = re.search(pattern,test)
if match:
    print( "year" , match.group(1))
    print("month", match.group(2))
    print( "date",  match.group(3))
else:
    print("N")


