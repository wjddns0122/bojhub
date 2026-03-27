n = input()

digits_arr = []
for char in n:
    digits_arr.append(int(char))

digits_arr.sort(reverse=True)
for v in digits_arr:
    print(v, end="")