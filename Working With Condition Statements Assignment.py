1
employee_information = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 , 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

2
employee_numbers = [1121, 22.22, 1122, 1127, 1132, 1137, 1138, 1152, 1157]

employee_names = ["Jackie Grainger", "Jignesh Thrakkar", "Dion Green", "Jacob Gerber", "Brandon Heck", "David Toma", "Charles King"]

salary_information = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]

4
salary_information = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]

total_hourly_rate = []
for generic_value in salary_information:
    total_hourly_rate.append(generic_value * 1.3)
if(max(total_hourly_rate)>37.30):
    print("someone's salary may be a budget concern")
else:
    print(total_hourly_rate)

5
salary_information = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]

underpaid_salaries= []

for salary_rate in salary_information:
   if(salary_rate>=28.15 and salary_rate<=30.65):
       underpaid_salaries.append(salary_rate)

print(underpaid_salaries)

6
salary_information = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]

company_raises = []

for salary in salary_information:
    if (salary > 22 and salary < 24):
        raises = 0.05 * salary
        company_raises.append(salary + raises)
    elif (salary > 24 and salary < 26):
        raises = 0.04 * salary
        company_raises.append(salary + raises)
    elif (salary > 26 and salary < 28):
        raises = 0.03 * salary
        company_raises.append(salary + raises)
    else:
        raises = 0.02 * salary
        company_raises.append(salary + raises)
7
# An employee(s) can login to the sever with the below credentials and perform work.

login1 = "nick"
login2 = "rick"
login3 = "bill"
login4 = "jill"
credentials1 = "1234"
credentials2 = "12345"
credentials3 = "123"
credentials4 = "12"
if (login1 == "nick" and credentials1 == "1234") or (login2 == "rick" and credentials2 == "12345") or (login3 == "bill" and credentials3 == "123") or (login4 == "jill" and credentials3 == "12"):
    print("Welcome to the server")
