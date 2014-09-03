#program that lists prime numbers under 100
#user input question for number to increment
question = input("Enter a number. ")

#create outer loop of numbers up to and including n
outer = range(2, question + 1)
#create test loop of prime numbers 2, 3, 5, 7
#future enhancement - to work when user input is less than 7
primes = [2, 3, 5, 7]
#create loop to print prime number after 2, 3, 5, 7
for i in outer:
#nested loop for prime test
    for j in primes:
#testing if number divisible by 2, 3, 5, 7
	if i % 2 == 0:
	    break
	elif i % 3 == 0:
	    break
	elif i % 5 == 0:
	    break
	elif i % 7 == 0:
	    break
#do not include prime numbers that are already in the primes list
	elif i in primes:
	    break	
	elif i % j == 0:
	    primes.remove(i)
	    break
	else: 
	    primes.append(i)
print(primes)

""" prime numbers up to 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
73, 79, 83, 89, 97
"""
