from typing import List, Any

def binary_search(x: Any, vals: List[Any], low: int=0, high: int=None) -> int:
	if high is None:
		return binary_search(x=x, vals=vals, low=0, high=len(vals))
	elif low <= high:
		mid = int((low + high)/2)
		if x < vals[mid]:
			return binary_search(x=x, vals=vals, low=0, high=mid-1)
		elif x > vals[mid]:
			return binary_search(x=x, vals=vals, low=mid+1, high=high)
		else:
			return mid
	else:
		raise Exception(f"{x} not in {vals}")

if __name__ == "__main__":

	x = [1,2,3,4,5,6,7]
	print(binary_search(4,x))
