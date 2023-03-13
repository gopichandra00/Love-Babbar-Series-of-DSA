class Solution:
    def KthMM(self, A, start, end):
        if start == end:
            return A
        else:
            mid = (start+end)//2
            max_1, min_1 = self.KthMM(A, start, mid)
            max_2, min_2 = self.KthMM(A,mid+1,end)
            A[start], A[end] = A[end], A[end]
