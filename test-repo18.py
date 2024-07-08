# calculate the hour worked 
# calculate the hourly rate
# calculate the bonus 
# calculate the total salary

hour_worked = int(input("Enter how many hours: "))
hourly_rate = int(input("Enter how much rate: "))

salary = hour_worked * hourly_rate

if hour_worked >= 45:
    bonus = 100

if hour_worked <= 40:
    bonus = 50

if hour_worked <= 35:
    bonus = 25

total_salary = bonus + salary

print("The salary is; ", str(salary))
print("\nThe bonus is: ", str(bonus))
print("\nThe total salary: ", (total_salary))