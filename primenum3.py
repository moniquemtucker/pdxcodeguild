__author__ = 'monique'
#program that lists prime numbers based on user input
#asking user for number to determine prime increment
question = input("Enter a number. ")

#create outer loop of numbers up to and including n
outer = range(2, question + 1)

#create empty list for prime numbers to be appended to
primes = []

#outer loop to test if each number from 2 to n is prime or not
for i in outer:
#nested inner loop for prime test of numbers i
    for j in range(2, i):
#if number is divisible, do not include it in the primes list
#if number is not divisible, continue the loop
	if i % j == 0:
        break
#once inner loop completes, add prime numbers to primes list
else:
    primes.append(i)
print(primes)

""" list of prime numbers up to 100:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97
"""