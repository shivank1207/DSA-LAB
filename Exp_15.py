# from typing_extensions import Concatenate


# def A(d,last_ind):
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     l_alpha = len(alpha)
#     l_d = len(d)
#     con = str(last_ind)+str(last_ind-1)
#     con = int(con)

#     b = A(d , last_ind-1)



# # Driver code
# digits = "1234"
# l = len(digits)
    # if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7')):

# print("Count is ", A(digits , l-1))





# def numDecodings(s: str) -> int:
#     if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
#         return 0
#     return numDecodingsHelper(s, len(s))

# def numDecodingsHelper(s: str, n: int) -> int:
#     if n == 0 or n == 1:
#         return 1
#     count = 0
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if s[n-1] > "0":
#         count = numDecodingsHelper(s, n-1)
#     b = str(s[n-2]) + str(s[n-1])
#     b = int(b)
#     if (b<27):
#         print(alpha[b])
#         count += numDecodingsHelper(s, n - 2)
#     return count

# # Driver code
# digits = "1234"
# print("Count is ", numDecodings(digits))


# def convert(d):
#     alpha = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     l = len(d)
#     for i in range(0,l):
#         print(alpha[d[i]],end="")
#     b = str(d[l-2]) + str(d[l-1])
#     b = int(b)
#     if (b<27):
#         print(alpha[b])
#         for i in range(0,l):
#             print(alpha[d[i]-1],end="")





# # Driver code
# d = [1,2,3,4]
# print(convert(d))












# Alpa = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Array = [1, 2, 5, 3] #  ADB, NB
# Pair = []

# for i in range(len(Array)-1):
#     num = int(str(Array[i])+str(Array[i+1]))  
#     Combo = []  
    
#     j=0
#     while j < len(Array):
#         if j != i and j != i+1:
#             Combo.append(Array[j])    
#             j += 1
#         else:
#             Combo.append(num)
#             j += 2
#         if Combo not in Pair:    
#             Pair.append(Combo)

# double = []
# i=0
# while i < len(Array)-1:
#     pairs = int(str(Array[i])+str(Array[i+1]))
#     double.append(pairs)
#     i += 2  

# def isValid(elem):
#     count = 0
#     for item in elem:
#         if item<26:
#             count += 1 
#     if count == len(elem):
#         return 1
#     return 0    

# def result(item):
    
#     AlpaList=''
#     for index in item:
#         AlpaList += str(Alpa[index])
    
#     print(AlpaList)  


# #printing result
# result(Array)

# for item in Pair:
#     if isValid(item):
#         result(item)

# if isValid(double):
#     if len(double)>1:
#         result(double)



# Function to find all possible combinations of words formed by replacing
# given positive numbers with the corresponding character of the English alphabet
def findCombinations(digits, i=0, s=''):
    if not digits:
        return
    if i == len(digits):
        # print the string
        print(s)
        return
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    # process the next two digits (i'th and (i+1)'th)
    for j in range(i, min(i + 1, len(digits) - 1) + 1):
        total = (total * 10) + digits[j]
        # if a valid character can be formed by taking one or both digits, append it to the output and recur for the remaining digits
        if 0 < total <= 26:
            findCombinations(digits, j + 1, s + alphabet[total - 1])
 
 
if __name__ == '__main__':
 
    digits = [1, 2, 2,4]
 
    findCombinations(digits)