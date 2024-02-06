#8
def spy_game(nums):
    code = [0, 0, 7]
    index = 0

    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True

    return False

result1 = spy_game([1, 2, 4, 0, 0, 7, 5])
result2 = spy_game([1, 0, 2, 4, 0, 5, 7])
result3 = spy_game([1, 7, 2, 0, 4, 5, 0])

print(result1)
print(result2)
print(result3)
