print("select option")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


operation = input()
if operation == "1":
    num1= input("enter first number:")
    num2= input("enter second number:")
    print("the sum is:" + str(int(num1) + int(num2)))
if operation == "2":
    num1 = input("enter first number:")
    num2 = input("enter second number:")
    print("the subtraction is:" + str(int(num1) - int(num2)))
if operation == "3":   
    num1= input("enter first number:")
    num2= input("enter second number:")
    print("the multiplication is:" + str(int(num1) * int(num2)))
if operation == "4":
    num1= input("enter first number")
    num2= input("enter second number")
    print("the division is:" + str(int(num1) * int(num2)))
    
    


