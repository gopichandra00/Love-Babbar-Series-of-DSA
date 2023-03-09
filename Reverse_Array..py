class Reverse:
    def Reverse_array(self, A, start, End):
        while start < End:
            A[start], A[End] = A[End], A[start]
            start += 1
            End -= 1
        return A


A = [12,4,64,54,6,49]
print("This is Array",A)
obj = Reverse()
x = obj.Reverse_array(A,0,len(A)-1)
print("This is reversed array",x)

