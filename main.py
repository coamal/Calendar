#!/usr/bin/env python
# accept year and month from user and display that month's calendar
import datetime as dt


def get_year():
    '''
    input --> none
    output --> year
    accept year from user and if it is valid
    returns the year
    '''
    while True:
        try:
            year = int(input("Enter the year(1995 - 2090): "))
            if year <= 2090 and year >= 1995:
                return year
            else:
                print("Invalid year!")
                continue
        except ValueError:
            print("Not a number!")
            continue

def get_month(year):
    '''
    input --> year
    output --> month
    accept month from user and if it is valid, returns the month
    '''
    while True:
        try:
            month = int(input("Enter the month(1- 12): "))
            if month <= 12 and month >= 1:
                return month
            else:
                print("Invalid month!")
                continue
        except ValueError:
            print("Not a number!")
            continue

def get_start_day(year, month):
    '''
    input --> year and month
    output --> a list of blank spaces according to the start day offset
    '''
    week_day = int(f'{dt.date(year=year, month=month, day=1):%w}')
    if  week_day == 0:
        start = 0
    elif week_day == 1:
        start = 1
    elif week_day == 2:
        start = 2
    elif week_day == 3:
        start = 3
    elif week_day == 4:
        start = 4
    elif week_day == 5:
        start = 5
    elif week_day == 6:
        start = 6
        
    return [" " for i in range(start)]


def is_leap_year(year):
    '''
    input --> year
    output --> boolean value
    return True or False according to whether year is leap or not
    '''
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        return True
    else:
        return False


def return_month(year, month):
    '''
    input --> year and month
    output --> corresponding calendar of the given month
    '''
    not_leap = {1: list(range(1, 32)), 2: list(range(1, 29)), 3: list(range(1, 32)),
                4: list(range(1, 31)), 5: list(range(1, 32)), 6: list(range(1, 31)),
                7: list(range(1, 32)), 8: list(range(1, 32)), 9: list(range(1, 31)),
                10: list(range(1, 32)), 11: list(range(1, 31)), 12: list(range(1, 32))}
    leap = {2: list(range(1, 30))}

    if is_leap_year(year) and month == 2:
        return leap[month]
    else:
        return not_leap[month]


def display_month(month_list, year, month, start_day):
    '''
    input --> list of days in a month
    output --> calendar of the month
    display calendar with good formating
    '''
    months = {1: 'January', 2: "February", 3: "March",
              4: 'April', 5: 'May', 6: 'June', 7: 'July',
              8: 'August', 9: 'September', 10: 'October',
              11: 'November', 12: 'December'}
    print(months[month], year)
    print('Sun Mon Tue Wed Thu Fri Sat')
    
    count = 0
    for i in start_day + month_list:
        
        print(f"{i:^4}", end="")
        count += 1
        if count == 7:
            count = 0
            print()
            continue
    print()


def main():
    '''
    driver function
    '''
    print(f"Welcome! Today is {dt.date.today()}")
    print("Enter the year and month and you will get a calendar of the given month!")
    while True:
        choice = input("Do you want to continue?(Yes or No): ")
        if choice == "":
            print("Invalid choice!")
            continue
        elif choice[0] == 'Y' or choice[0] == 'y':
            year = get_year()
            month = get_month(year)
            start = get_start_day(year, month)
            month_list = return_month(year, month)
            print()
            display_month(month_list, year, month, start)
            print()
            continue
        elif choice[0] == 'N' or choice[0] == 'n':
            print('Exiting...')
            break
        else:
            print('Invalid choice!')
            continue
    
    print()
    print("Have a nice day! Come back again!")


main()
