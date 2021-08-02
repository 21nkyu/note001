arr =[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        print(arr[i], arr[j-1])
        if arr[j] < arr[j-1]:
            print(arr[j-1], arr[j], arr[j], arr[j-1])
            arr[j-1], arr[j] = arr[j], arr[j-1]
            print(arr)
        else:
            break
print(arr)
