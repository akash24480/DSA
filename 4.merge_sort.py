#Example array [2,8,4,6,0,3,4]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]  #Not including the midlevalue
    right_arr = arr[mid:] #Including the middle

    left_sort = merge_sort(left_arr)
    right_sort = merge_sort(right_arr)

    #Now we have to merge them 

    return merge(left_sort, right_sort)


def merge(left, right):
    result = []

    i = j = 0 #Pointers for the left and right arrays

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left)
            i += 1
        else:
            result.append(right)
            j+= 1
    #Now adding the remaining code
    result.extend(left[i:])
    result.extend(right[j:])

    return result