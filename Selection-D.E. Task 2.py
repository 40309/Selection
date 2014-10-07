#Tony K.
#06-10-2014
#Development Exercise 2

print("This programm tells you what state the water in the container is.")

temperature = float(input("Please enter the tempearure(in centigrade) of the water in the container: "))
if temperature <= 0:
    print("The state of water is frozen.")
elif 0 < temperature <  99.98:
    print("The state of the water is not frozen nor boiling.")
else:
    print("The state of water is boiling.")
