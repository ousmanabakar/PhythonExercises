# Check a number if a Positive, Negative or 0

print("******************************")

print("type 'exit' to end the program\n")

while True:
    number = (input("En a number:"))

    if number.lower() == "exit":
        print("The program is turned off")
        break

    elif float(number) > 0:

        print(f"{number} is a positive number")

    elif float(number) < 0:

        print(f"{float(number)} is a negative number")

    else:
        print("The number you entered is :", number)


