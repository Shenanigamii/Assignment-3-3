# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

import calendar

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

#dictionary of months
months = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December"]

#user input
print("This program checks if a date is valid or not.")
year = input("Enter a year: ")
monthInput = input("Enter a Month, 1-12 or its name: ")
day = input("Enter a valid day, 1-31: ")

# Check to be sure date is valid

#validate the year. checks to ensure user input digits, 
#and checks it against MIN_YEAR for compliance
if not year.isdigit() or int(year) < MIN_YEAR:
    validDate = False

#validate the month
if monthInput.isdigit():
    month = int(monthInput)
    if month < MIN_MONTH or month > MAX_MONTH:
        validDate = False
else:
  #changes month number to name if user input name instead of number
    monthName = monthInput.capitalize()
    if monthName not in months:
        validDate = False
    else:
        month = months.index(monthName) + 1

#validate the day
#checks to ensure user input information properly, 
#and checks it against MIN_DAY and MAX_DAY for validity for that month
if not day.isdigit() or int(day) < MIN_DAY or int(day) > MAX_DAY.get(month, 0):
    validDate = False

#check if it's a leap year
if validDate:
    year_int = int(year)
    if month == 2 and int(day) == 29:
        if (year_int % 4 != 0) or (year_int % 100 == 0 and year_int % 400 != 0):
            validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
#uses f-string to format the desired output of the given date
if validDate:
    if monthInput.isdigit():
        print(f"{month}/{day}/{year} is a valid date.")
    else:
        print(f"{monthName}/{day}/{year} is a valid date.")
else:
    print(f"{monthInput}/{day}/{year} is an invalid date.")