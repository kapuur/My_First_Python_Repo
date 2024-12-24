def multiplication(**var):
    result=1
    for i in var:
        result*=var[i]
    return result
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))

print(multiplication(a=num1, b=num2, c=num3))