class Shape:

    area = 0

    def __lt__(self, other):
        return self.area < other.area


a = Shape()
a.area = 20
b = Shape()
b.area = 10

print(a > b)
print(a < b)
print(a == b)
print(a != b)