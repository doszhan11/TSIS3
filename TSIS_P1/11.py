#11
def is_p(word):
    c = word.lower().replace(" ", "")
    return c == c[::-1]


inp = input()
if is_p(inp):
    print("palindrome")
else:
    print("not palindrome")
