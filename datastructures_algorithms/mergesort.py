from typing import List

def mergesort(x: List[int], start: int=0, end: int=None) -> None:
	if end is None:
		end = len(x) - 1

	mid = int((start + end)/2)

	if start < end:
		mergesort(x=x, start=start, end=mid)
		mergesort(x=x, start=mid+1, end=end)

		temp = [None] * (end - start + 1)
		k = 0
		i = start
		j = mid + 1

		print(f"{start}, {end}, {mid}")

		while i <= mid and j <= end:
			if x[i] < x[j]:
				temp[k] = x[i]
				k += 1
				i += 1
			else:
				temp[k] = x[j]
				k += 1
				j += 1

			while i <= mid:
				temp[k] = x[i]
				k += 1
				i += 1

			while j <= end:
				temp[k] = x[j]
				k += 1
				j += 1

			print(f"temp = {temp}")

		for z in range(k):
			x[start+z] = temp[z]

		print(f"x = {x}")


if __name__ == "__main__":
	x = [4, 8, 28, 1, 3, 9, 13, 2, 7]

	print(f"unsorted: {x}")
	mergesort(x)
	print(f"sorted: {x}")