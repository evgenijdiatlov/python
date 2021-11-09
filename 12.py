class Point:
 
    def __init__(self, x, y, z=10):
        print('в конструкторе')
        self.choords = (x, y, z)
 
    def __repr__(self):
        return f'Point: {self.choords}'
 
    def __del__(self):
        del self.choords
        print('в деструкторе')
 
 
p = Point(1, 2, 3)
print(p)
del p
print('конец работы программы')