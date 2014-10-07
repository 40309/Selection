#Tony K.
#06-10-2014
#Selection- D.E. Task 4

print("This programm tells you your Grade one you enter your score")

mark = int(input("Please enter your marks you got in the test: "))
if 0 <= mark <= 40:
    print("Grade U")
elif 41 <= mark <= 50:
    print("Grade E")
elif 51 <= mark <= 60:
    print("Grade D")
elif 61 <= mark <= 70:
    
    print("Grade C")
elif 71 <= mark <= 80:
    print("Grade B")
elif 81 <= mark <= 100:
    print("Grade A")
else:
    print("The value you entered is invalid, Please Try again")
