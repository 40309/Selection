# Tony K.
# 10/10/2014
# spot Check

print("This programm check pupils attendance")

attendance = float(input("Please enter your attendance: "))

if attendance >= 85 and attendance < 100:
    print("Your attendance is {0}%. Keep up the good attendance.".format(attendance)) 
elif attendance < 85 and attendance > 0:
    print("Your attendance is {0}%. You must improve your attendance.".format(attendance))
else:
    print("The value you entered is invalid.")

print("Thank you for using this program.")
