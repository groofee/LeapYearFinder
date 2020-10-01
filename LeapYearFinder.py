"""
This is Leap year checker.... The user inputs a year and the program optputs the answer. If it is a leap year, it prints "It is a leap year"
else it prints "It is not a leap year".The program ends only of the user wants it to end.

"""

# --- Leap Year Finder --- #
while True:
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("Sorry, that is not a valid year. Please try again.")
        continue
    else:
        break
    
if (year < 1582):
    print("Sorry, {} pre-dates the Gregorian calendar.".format(year))

# --- The Triangle of Doom --- #  
else:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{} is a leap year!".format(year))
            else:
                print("{} is a common year!".format(year))
        else:
            print("{} is a leap year!".format(year))
    else:
        print("{} is a common year!".format(year))
