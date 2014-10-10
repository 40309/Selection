#Tony K.
#06-10-2014
#Selection- D.E. Task 3

print("This programm works out your gross pay.")

numbers_of_hours = float(input("Please enter the hours you have worked: "))
hourly_rate = float(input("Please enter the hourly rate of pay: "))

if 40 < numbers_of_hours <= 60:
    gross_pay = (1.5 * hourly_rate) * numbers_of_hours
    print("Your gross pay is £{0}".format(gross_pay))
elif 0 < numbers_of_hours <= 40:
    gross_pay = hourly_rate * numbers_of_hours
    print("Your gross pay is £{0}".format(gross_pay))
elif numbers_of_hours <= 0:
    print("Start working")
else:
    print("You worked 60+ hours, catch a break")
