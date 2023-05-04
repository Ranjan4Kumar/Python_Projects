print("Your are using a basic calculator")
num1 = int(input('Enter Your 1st value'))
op = input('Enter your operator')
num2 = int(input("Enter your 2nd value"))

if op == '+':
    result = num1+num2
elif op =='-':
    if num1>num2:

        result = num1 - num2
    else:
        result = num2-num1
elif op == '*':
    result = num1*num2
elif op == '/':
    result = num1/num2
else:
    print('Number is not valid')

if op in ['+','-','*','/']:
    print(f'{num1} {op} {num2} = {result}')
else:
    print('----------')