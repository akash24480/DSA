
class MergeSort:
    def merge_sort(self,arr,l,r):
        if l < r:
            mid = (l + r) // 2
            self.merge_sort(arr, l, mid)
            self.merge_sort(arr, mid + 1, r)

            #merge the two halves
            self.merge(arr,l,mid,r)
    def merge(self, arr, l, mid, r):
        left_arr  = arr[l:mid + 1]
        right_arr = arr[mid+1:r+1]

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        #copy the remaining elements from the left arr

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        #copy the remaining elements from the right arr

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1




# Test the implementation
arr = [2, 8, 4, 6, 0, 3, 4]
merge_sort_obj = MergeSort()
merge_sort_obj.merge_sort(arr, 0, len(arr) - 1)
print(arr)
