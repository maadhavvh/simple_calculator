num1 = float(input('Enter Number 1:'))
num2 = float(input('Enter Number 2:'))
operator = input('Enter the operator (+ - * / :)')

if operator == '+':
    print(num1+num2)

elif operator == '-':
    if num1>num2 or num1==num2:
        print(num1-num2)
    else:
        print(num2-num1)

elif operator == '*':
    print(num1*num2)

else:
    print(num1/num2)