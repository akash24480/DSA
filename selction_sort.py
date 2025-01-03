def selection_sort(arr):
    for i in range (0, len(arr) - 1):
        mini = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]
    print(arr)


selection_sort([9,23,45,0,2,6,90])