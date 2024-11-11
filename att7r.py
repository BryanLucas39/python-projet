salary = int (input("Enter your salary: R$"))

if salary <= 280:
    increase = salary * 0.20
    f_salary = increase + salary
    print("Your salary was ",salary," and according with that info. you gonna receive a increase of 20%, in total ",increase," in your salary, and your final payment are", f_salary)

elif salary >= 280 or salary == 700:
    increase = salary * 0.15
    f_salary = increase + salary
    print("Your salary was ",salary," and according with that info. you gonna receive a increase of 15%, in total ",increase," in your salary, and your final payment are", f_salary)

elif salary >=700 or salary == 1500:
    increase = salary * 0.10
    f_salary = increase + salary
    print("Your salary was ",salary," and according with that info, you gonna receive a increase of 10%, in total ",increase," in your salary, and your final payment are", f_salary)

elif salary > 1500:
    increase = salary * 0.05
    f_salary = increase + salary
    print("Your salary was ",salary," and according with that info. you gonna receive a increase of 05%, in total ",increase," in your salary, and your final payment are", f_salary)


else:
    ("ERROR, something gone wrong filling from the info, please try again")