# Tony K.
# 10/10/2014
# spot Check v2

first_name = input("Please enter your first name: ")
last_name = input("Please enter our last name: ")
gender = input("Please enter your gender: ")
if gender == male:
    print("Mr.{0} {1}".format(first_name,last_name))
elif gender == female:
    print("Ms.{0} {1}".format(first_name,last_name))
else:
    print("Please enter appropriate gender.")
