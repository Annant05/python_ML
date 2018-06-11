# calc salary for a month
rate_hour = int(input("Enter Rate of Salary in Rate/Hour  : "))
hour_worked_in_week = int(input("Enter No Of Hours Worked : "))
no_week_in_month = 3
additional = 1
if hour_worked_in_week > 20:
    additional = (hour_worked_in_week - 20) * 1.5 * rate_hour
total_salary = rate_hour * hour_worked_in_week * no_week_in_month + additional
print(total_salary)
