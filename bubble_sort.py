def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        didSwap = 0
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = 1
                print("Run")
        if didSwap == 0:
            break
    print(arr)    


bubble_sort([0,1,2,3,4,5,6,7])