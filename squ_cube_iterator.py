class square_cube:
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= 20:
            squr = self.val ** 2
            cube = self.val ** 3
            
            self.val += 1
            return squr , cube
        else:
            raise StopIteration

values = square_cube(1)
num = 1
for square , cube in values:
    print(f"{num}: Square: {square} , Cube: {cube}")
    num += 1
  
    
