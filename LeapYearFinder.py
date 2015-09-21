"""
This is Leap year checker.... The user inputs a year and the program optputs the answer. If it is a leap year, it prints "It is a leap year"
else it prints "It is not a leap year".The program ends only of the user wants it to end.

"""

import sys 
import time
    
print "\n ----------------Welcome to the Leap Year Finder !!!!! ------------------"
rep=0
while(rep!=1):
    print "\n"
    tryuntil=0
    while(tryuntil!=1):
        try:
            inp=int(raw_input("Please enter a year :"))
            if (inp%4==0):
                if(inp%100==0):
                    if (inp%400==0):
                        print"\n This is a leap year"
                    else:
                        print"\n This is not a leap year"
                else:
                    print "\n This is a leap year"
            else:
                print"\n This is not a leap year"
            
            tryuntil=1
                
        except:
            print "\nPlease Enter a numeric integer value"
    
    print "\n"
    
    checkoption=0
    while(checkoption!=1):
        try:
            print"\n"
            ask=raw_input("Do you want to try it again ??? y or n")
            if (ask=='y' or ask=='Y'):
                checkoption=1
                continue
            elif (ask=='n' or ask=='N'):
                checkoption=1
                rep=1
                print"\n Thank you for using the leap year checker"
            else:
                raise NameError
        except:
            print"\n"
            print "Please enter a valid option. press 'y' for Yes and 'n' for No "