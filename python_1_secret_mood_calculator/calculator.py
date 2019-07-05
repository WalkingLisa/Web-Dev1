number1=int(input("Please enter your first number: "))
number2=int(input("Please enter your second number: "))
operation=str(input("Please choose an operation (+, -, * or /): "))



if operation == "+":
    print(number1,"+",number2,"=",number1+number2)
elif operation == "-":
    print(number1,"-",number2,"=",number1-number2)
elif operation == "*":
    print(number1,"*",number2,"=",number1*number2)
elif operation == "/" and number2 != 0:
    print(number1,"/",number2,"=",int(number1/number2))
elif operation == "/" and number2 == 0:
    print("Don't divide by zero")
else:
    print("The operation input is invalid")