# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# My solution (Takes to long but it works):
my_number = True
num_range = 20

while my_number:
  num_list = []

  for num in range(1, 21):
    if num_range % num != 0:
      break
    else:
      module_num = num_range % num
      num_list.append(module_num)
    
  if len(num_list) == 20:
    result = num_range
    my_number = False
 
  num_range += 2

print(result)