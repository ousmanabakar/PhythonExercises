print("type 'exit' to end the program.")

while True:

    year = (input("Enter a year :"))
    if(year == "exit"):
        print("The program is turned off.")

    elif (int(year) % 4) == 0:

        if (int(year) % 100) == 0:

            if (int(year) % 400) == 0:
                print(f"{int(year)} is leap year")
            else:
                print(f"{int(year)} is not leap year")
        else:
            print(f"{int(year)} is a leap  year")

    else:
        print(f"{int(year)} is not leap year")