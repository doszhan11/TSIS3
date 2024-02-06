#9
def sphere(radius):
    pi = 3.14159
    volume = (4/3) * pi * (radius ** 3)
    return volume

radius = float(input())
result = sphere(radius)
print(result)
