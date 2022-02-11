'''The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143 ?
'''

my_num = 600851475143
largest_prime = 0
prime = 3


while my_num % 2 == 0:
    my_num /= 2
    largest_prime = 2

while my_num != 1:
    while my_num % prime == 0:
        my_num /= prime
        largest_prime = prime
    prime += 2

print(largest_prime)
