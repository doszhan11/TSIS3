#12
def h(numbers):
    for num in numbers:
        print('*' * num)

numbers_p = [int(x) for x in input().split()]


h(numbers_p)
