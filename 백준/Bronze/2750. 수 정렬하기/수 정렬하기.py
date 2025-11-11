n = int(input())
array = []

for i in range(n):
    data = int(input())
    array.append(data)
    
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
bubble_sort(array)

for num in array:
    print(num)