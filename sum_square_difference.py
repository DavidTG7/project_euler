# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# My solution:
num_square = 0
total_sum = 0
result_sum_sqr = 0

for num in range(1, 101):
  num_square = num * num
  result_sum_sqr += num_square

for num in range(1, 101):
  total_sum += num

sqr_sum = total_sum * total_sum

dif_sum_sqr = sqr_sum - result_sum_sqr

print(dif_sum_sqr)
