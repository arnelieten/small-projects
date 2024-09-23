import math

num = int(input('Enter your number:'))

def factorization(num):
    for i in range(2,num):
        if num % i == 0:
            print(i, 'times', num//i, 'equals', num)
            return
    print('No factorization possible! Your number is a prime number')

factorization(num)
