#experiment no.: 9
import sys
INF=sys.maxsize

def findminmax(A,i,j,min,max):
    if i==j:
        if min>A[j]:
            min=A[j]
        if max<A[i]:
            max=A[i]
        return min,max
    if i==j-1:
        if A[i]<A[j]:
            if min > A[i]:
                min=A[i]
            if max<A[j]:
                max=A[j]
        else:
            if min>A[j]:
                min=A[j]
            if max<A[i]:
                max=A[i]
        return min,max
    mid=(i+j)//2
    min,max=findminmax(A,i,mid,min,max)
    min,max=findminmax(A,mid+1,j,min,max)
    return min, max

A=[7,2,9,3,1,6,7,8,4]
(min,max)=(INF,-INF)
(min,max)=findminmax(A, 0, len(A)-1, min, max)
print("minimum value:",min)
print("maximum value:",max)