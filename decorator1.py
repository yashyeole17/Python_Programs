def topTen():
    n = 1
    while n <= 10:
        square = n ** 2
        yield square
        n += 1
    
values =  topTen()
for i in values:
    print(i)
