#7
def h_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Пример использования
result1 = h_3([1, 3, 3])
result2 = h_3([1, 3, 1, 3])
result3 = h_3([3, 1, 3])

print(result1)
print(result2)
print(result3)
