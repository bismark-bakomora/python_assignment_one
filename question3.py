employees = ["Kwame", "Akua", "Yaw", "Afia"]
salaries = [3200, 4000, 2800, 5000]

employee_salaries = {}

for i in range(len(employees)):
    employee_salaries[employees[i]] = salaries[i]

# adjust salaries based on salary amount
for name, old_salary in employee_salaries.items():

    # apply increase based on salary amount
    if old_salary < 3500:
        new_salary = old_salary * 1.07 # 7% increase
    else: 
        new_salary = old_salary * 1.04 # 4% increase

    # update the dictionary using update() method
    employee_salaries.update({name: new_salary})

# print updated salaries
for name, new_salary in employee_salaries.items():
    old_salary = salaries[employees.index(name)]
    print(f"{name}: | Old: {old_salary:.2f} | New: {new_salary:.2f}")