from typing import List

def quicksort(x : List[int], start: int=0, end: int=None) -> None:
	if end is None:
		end = len(x)-1

	mid = int((start + end)/2)
	i = start
	j = end

	while i <= j:
		while x[i] < x[mid]:
			i += 1
		while x[j] > x[mid]:
			j -= 1
		if i <= j:
			temp = x[i]
			x[i] = x[j]
			x[j] = temp
			i += 1
			j -= 1

	if i < end:
		quicksort(x=x, start=i, end=end)
	if j > start:
		quicksort(x=x, start=start, end=j)

if __name__ == "__main__":
	x = [4, 8, 28, 1, 3, 9, 13, 2, 7]

	print(f"unsorted: {x}")
	quicksort(x)
	print(f"sorted: {x}")