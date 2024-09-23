operation = input('Enter operation (addition, subtraction, multiplication and division): ')
num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

if operation == 'addition':
    result = num1 + num2

elif operation == 'substraction':
    result = num1 - num2

elif operation == 'multiplication':
    result = num1 * num2

else:
    result = num1//num2

print('result =',result)