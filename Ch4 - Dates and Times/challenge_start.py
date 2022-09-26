# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

def main():

    while True:
        userinput = prompt_for_weekday();
        if str(userinput).lower() == 'exit':
            break
        else:
            try:
                day = int(userinput)
            except ValueError as e:
                print(e)
                print("Sorry, that's not valid input")
                continue

        year = prompt_for_year()
        month = prompt_for_month()

        cal = calendar.monthcalendar(int(year), int(month))
        # print(type(cal))
        numofday = len(cal)
        if cal[0][day] == 0:
            numofday -= 1;
        if cal[-1][day] == 0:
            numofday -= 1;
        print("There are %d of those days in the month and year specified" % numofday)



def prompt_for_weekday():
    print("Which day of the week do you want to count?")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i,d in enumerate(weekdays):
        print(str(i)+":", d)
    return input("Or 'exit' to quit\n")

def prompt_for_year():
    return input("Enter year: ")

def prompt_for_month():
    return input("Enter month: ")


if __name__ == '__main__':
    main()

