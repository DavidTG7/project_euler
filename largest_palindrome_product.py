# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def palChecker():
  
  result = 0
  for num in range(800, 1000):
    for num2 in range(800, 1000):
      product = num * num2
      palnum = str(product)
      if palnum == palnum[::-1]:
        result = product
  return result

print(palChecker())
    