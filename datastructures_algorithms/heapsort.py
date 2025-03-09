def leftChildIndex(index):
	return 2 * index + 1

def rightChildIndex(index):
	return 2 * index + 2

def swap(x, index1, index2):
	temp = x[index1]
	x[index1] = x[index2]
	x[index2] = temp

def heapifyDown(x, index, last_index):
	maxIndex = leftChildIndex(index)

	# Go all the way down to the root and heapify
	while(maxIndex <= last_index):

		# check the right child
		if(rightChildIndex(index) < last_index and x[maxIndex] < x[rightChildIndex(index)]):
			maxIndex = rightChildIndex(index)

		if(x[index] < x[maxIndex]):
			swap(x, index, maxIndex)
			index = maxIndex
			maxIndex = leftChildIndex(index)

		else:
			return

def heapsort(x):

	# set size = length - 1 to get the last possible parent
	size = len(x)-1
	lastPossibleParent = size / 2 

	# heapify inplace
	for i in range(lastPossibleParent, -1, -1):
		heapifyDown(x, i, size)

	# now move the max in the heap to the back
	# to first unsorted index by swapping and 
	# heapifying down if necessary to the i-1 th
	# element
	for i in range(size, -1 , -1):
		if x[0] > x[i]:
			swap(x, 0, i)

			# i-1 instead of i
			# otherwise would put it back at the top
			heapifyDown(x, 0, i - 1)



if __name__ == "__main__":

	x = [5, 7, 2, 9, 4, 15, 1, 3]

	print x

	heapsort(x)

	print x

