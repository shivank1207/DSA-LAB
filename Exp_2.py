#experiment:2
def maxproduct(arr, n):
    if (n < 2):
        print("no pair")
        return
    a = arr[0]; b = arr[1]
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] * arr[j] > a * b):
                a = arr[i]; b = arr[j]
                print("Max product pair is {", a, ",", b,"}", sep = "")
	
arr = [11, 14, 8, 7, 12, 2]
n = len(arr)
maxproduct(arr, n)