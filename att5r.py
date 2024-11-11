num1 = int (input("Enter a number to compare: "))
num2 = int (input("Enter a another number to compare: "))
num3 = int (input("Enter the last number to compare: "))

if num1 > num2  and num1 > num3:
    print("The first number was the highest number you inserted, the number is:",num1)

elif num2 > num1  and num2 > num3:
    print("The second number was the highest number you inserted, the number is",num2)


elif num3 > num2 and num3 > num1:
    print("The third number was the highest number you inserted, the number is",num3) 

elif num1 == num2 and num2 == num3 and num3 == num1:
    print("The numbers was inserted are they same")