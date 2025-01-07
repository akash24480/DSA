def insertion_sort(arr):
    for i in range(0, len(arr)):
        j=i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]

            j -= 1
        print(arr)

insertion_sort([1,5,9,3,6,0])


# Dry Run Example: 
# Input: [1, 5, 9, 3, 6, 0]

# Iteration 1 (i = 0):
# j = 0, no comparison (j > 0 is False)
# Array: [1, 5, 9, 3, 6, 0]

# Iteration 2 (i = 1):
# j = 1, compare arr[0] (1) with arr[1] (5): 1 < 5, no swap
# Array: [1, 5, 9, 3, 6, 0]

# Iteration 3 (i = 2):
# j = 2, compare arr[1] (5) with arr[2] (9): 5 < 9, no swap
# Array: [1, 5, 9, 3, 6, 0]

# Iteration 4 (i = 3):
# j = 3, compare arr[2] (9) with arr[3] (3): swap
# Array: [1, 5, 3, 9, 6, 0]
# j = 2, compare arr[1] (5) with arr[2] (3): swap
# Array: [1, 3, 5, 9, 6, 0]
# j = 1, compare arr[0] (1) with arr[1] (3): no swap
# Array: [1, 3, 5, 9, 6, 0]

# Iteration 5 (i = 4):
# j = 4, compare arr[3] (9) with arr[4] (6): swap
# Array: [1, 3, 5, 6, 9, 0]
# j = 3, compare arr[2] (5) with arr[3] (6): no swap
# Array: [1, 3, 5, 6, 9, 0]

# Iteration 6 (i = 5):
# j = 5, compare arr[4] (9) with arr[5] (0): swap
# Array: [1, 3, 5, 6, 0, 9]
# j = 4, compare arr[3] (6) with arr[4] (0): swap
# Array: [1, 3, 5, 0, 6, 9]
# j = 3, compare arr[2] (5) with arr[3] (0): swap
# Array: [1, 3, 0, 5, 6, 9]
# j = 2, compare arr[1] (3) with arr[2] (0): swap
# Array: [1, 0, 3, 5, 6, 9]
# j = 1, compare arr[0] (1) with arr[1] (0): swap
# Array: [0, 1, 3, 5, 6, 9]

# Final Output:
# [0, 1, 3, 5, 6, 9]