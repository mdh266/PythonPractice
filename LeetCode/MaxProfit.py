from typing import List

def max_profit(values: List[float]) -> float:
	min_val = values[0]
	max_profit = 0
	for val in values:
		if val < min_val:
			min_val = val
		if val - min_val > max_profit:
			max_profit = val - min_val
			
	return max_profit


if __name__ == "__main__":
	values = [1,3,4,5,8,2,8,7,20,4]
	profit = max_profit(values)

	print(f"{profit}")
