numbers= []
n1 = float (input("Enter the first  number  to compare: "))
n2 = float (input("Enter the second number  to compare: "))
n3 = float (input("Enter the third  number  to compare: "))
n4 = float (input("Enter the fourth number  to compare: "))
n5 = float (input("Enter the fifth  number  to compare: "))

# adicionar os numeros a lista
numbers.append(n1)
numbers.append(n2)
numbers.append(n3)
numbers.append(n4)
numbers.append(n5)

highest = numbers[0]
for n in numbers:
   if n > highest:
     highest = n
print("the highest number you inserted was: ",highest)