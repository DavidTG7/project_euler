'''If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
'''

# My solution:
result = 0
numbers = []

for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        numbers.append(num)

for num in numbers:
    result += num

print(result)

