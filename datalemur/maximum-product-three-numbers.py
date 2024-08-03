https://datalemur.com/questions/python-maximum-product-three-numbers

def max_three(input):
  input.sort()
  max_num = input[-1]
  min_num = input[0]
  
  if min_num < 0:
    if abs(min_num) <= max_num:
      return max(max_num * input[-2] * input[-3], 
                 max_num * input[0] * input[1]),
    else:
      return max(max_num * min_num * input[1], 
                 max_num * min_num * input[2])
  else:
      return max_num * input[-2] * input[-3]
