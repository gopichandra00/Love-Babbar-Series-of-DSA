class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        i, j = 0, 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged

    def kth_max_min(self, arr, k):
        arr = self.merge_sort(arr)
        if k <= len(arr):
            kth_min = arr[k-1]
            kth_max = arr[-k]
            return kth_min, kth_max
        else:
            return None


arr = [3, 32, 14, 34, 31, 44, 11, 41, 4]
obj = Solution()
array_ = obj.merge_sort(arr)
print(array_)
k = int(input("Enter the kth value in range of array:\t"))
result = obj.kth_max_min(arr, k)
if result:
    kth_min, kth_max = result
    print("Kth minimum element: ", kth_min)
    print("Kth maximum element: ", kth_max)
else:
    print("Kth number you entered is out of range ")







