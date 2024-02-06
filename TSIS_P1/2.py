#2
def f(fahrenheit):
    c = (5 / 9) * (fahrenheit - 32)
    return c

_input = float(input())

result = f(_input)

print(result)
