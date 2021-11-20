def findPair(nums, target):
    # sort the list in ascending order
    nums.sort()
    # maintain two indices pointing to endpoints of the list
    (low, high) = (0, len(nums) - 1) 
    # reduce the search space `nums[low…high]` at each iteration of the loop
    # loop till the search space is exhausted
    while low < high:
        if nums[low] + nums[high] == target:        # target found
            print('Pair found', (nums[low], nums[high]))
            return
        # increment `low` index if the total is less than the desired sum;
        # decrement `high` index if the total is more than the desired sum
        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
    # No pair with the given sum exists
    print('Pair not found')












# def getpairs(a,n,sum,p,q):
# 	count = k = 0
# 	for i in range(0,n):
# 		for j in range(i+1,n):
# 			if (a[i] + a[j] == sum) :
# 				p[k] = a[i]
# 				q[k] = a[j]
# 				k = k+1
# 				count = count+1
# 	return count

# if __name__=='__main__':
# 	a = [2, 5, 45, 6, 11, 9,15,1,14,2]
# 	p = q = []
# 	sum = 16
# 	count = getpairs(a,len(a),sum,p,q)
# 	print("Count of pairs is ", count)
# 	for i in range(0,count):
# 		print("Pair ",i+1," is (",p[i],",",q[i],")")