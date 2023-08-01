
# magic opearations
class operations:
    def __init__(self, a):
        self.a=a

    def __lt__(self, uu):
        lt= self.a < uu.a
        return lt

    def __gt__(self, uu):
        gt = self.a > uu.a
        return gt

    def __le__(self, uu):
        le = self.a <= uu.a
        return le

    def __ge__(self, uu):
        ge = self.a >= uu.a
        return ge

    def __eq__(self, uu):
        return self.a >= uu.a

    def __ne__(self, uu):
        return self.a >= uu.a


a = operations(1)
b = operations(2)
print("Less than: ",a<b)
print("Greter Than: ",a>b)
print("Less Equal: ",a<=b)
print("Greter Equal: ",a>=b)
print("Equals: ",a==b)
print("Not Equlas: ",a!=b)

