a = input()

result = 0

for i in range(len(a)):
    if a[i] == "A" or a[i] == "B" or a[i] == "C":
        result += 2
    elif a[i] == "D" or a[i] == "E" or a[i] == "F":
        result += 3
    elif a[i] == "G" or a[i] == "H" or a[i] == "I":
        result += 4
    elif a[i] == "J" or a[i] == "K" or a[i] == "L":
        result += 5
    elif a[i] == "M" or a[i] == "N" or a[i] == "O": 
        result += 6
    elif a[i] == "P" or a[i] == "Q" or a[i] == "R" or a[i] == "S":
        result += 7
    elif a[i] == "T" or a[i] == "U" or a[i] == "V": 
        result += 8
    elif a[i] == "W" or a[i] == "X" or a[i] == "Y" or a[i] == "Z":
        result += 9

    result += 1

print(result)