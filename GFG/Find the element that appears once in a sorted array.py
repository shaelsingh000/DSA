def search(nums):
	# A Binary Search based method to find the element
	# that appears only once
	start = 0;
	end = len(nums)-1;
	mid = 0;

	# For Edge Cases
	if (len(nums) == 1): # If only one element is in the array
		return nums[0];

	if (nums[start] != nums[start + 1]): # If the first element
										# is the element that
										# appears only once
		return nums[start];

	if (nums[end] != nums[end - 1]): # If Last element is the element
									# that appears only once
		return nums[end];

	# Binary Search
	while (start <= end):
		mid = start + (end - start) // 2;
		
		# CASE 1
		if (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
		
			return nums[mid];
		# CASE 2 and CASE 3
		elif((nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 != 0)):
			start = mid + 1;
			
		# CASE 4 and CASE 5
		else:
			end = mid - 1;
	
	# If no such element found
	return -1;

# Driver code
if __name__ == '__main__':
	arr = [ 1, 1, 2, 4, 4, 5, 5, 6, 6 ];

	element = search(arr);

	if (element != -1):
		print("The required element is " , element);
	else:
		print("There is no such element");

# This code is contributed by umadevi9616
