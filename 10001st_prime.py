# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# My solution:
prime_index = 2
new_range = 3
last_prime = 3

while prime_index <= 10001:

  is_prime = False
  
  for num in range (2, int(new_range / 2) + 2):
    if new_range % num == 0:
      is_prime = False
      break
    else:
      is_prime = True
  
  if is_prime:
    last_prime = new_range
    prime_index += 1
  
  new_range += 2
  
print(last_prime)

