class Max_Min:
    def DACMM(self,A, start, end):
        if start == end:
            max = A[start]
            min = A[start]
        else:
            mid = (start+end)//2
            max_1, min_1 = self.DACMM(A, start, mid)
            max_2, min_2 = self.DACMM(A, mid +1, end)

            if max_1 > max_2:
                max = max_1
            else:
                max = max_2
            if min_1 < min_2:
                min = min_1
            else:
                min = min_2
        return max , min

A = [1,32,46,5,71,7,34]
obj = Max_Min()
maximum , miniumum = obj.DACMM(A, 0, len(A)-1)
print("Maximum is: ", maximum)
print("Minimum is:", miniumum)
