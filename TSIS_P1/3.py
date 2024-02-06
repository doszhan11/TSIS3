#3
def solve(num, numl):
    for num_c in range(num + 1):
        num_rabbits = num - num_c
        total = 2 * num_c + 4 * num_rabbits

        if total == numl:
            return num_c, num_rabbits

    return None, None

n = int(input())
na = int(input())

result_c, result_r = solve(n, na)

if result_c is not None and result_r is not None:
    print(result_c)
    print(result_r)
else:
    print("No solution found.")
