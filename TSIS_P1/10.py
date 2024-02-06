#10
def unique(ss):
    u = []
    for i in ss:
        if i not in u:
            u.append(i)
    return u

a = [1, 2, 2, 3, 4, 4, 5]
result = unique(a)
print(result)
