#6
def reverse_w(sentence):
    w = sentence.split()
    r_ = ' '.join(reversed(w))
    return r_

# Пример использования
_input = input()
result = reverse_w(_input)

print(result)
