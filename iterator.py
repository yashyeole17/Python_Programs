class TopTen:
    def __init__(self,x):
        self.num = x

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = TopTen(1)
for i in values:
    print(i)

print("End")
