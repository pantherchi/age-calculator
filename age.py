#https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
import datetime
from datetime import date

class calc:

    def impVal():
        print("in ImpVal method")
        inp = input("Enter your date of birth (dd/mm/yyyy): ")
        inp_list = inp.split('/')
        numbers = [int(x.strip()) for x in inp_list]
        birthYear = numbers[2]
        birthMonth = numbers[1]
        birthDay = numbers[0]

        i = datetime.datetime.now()
        currentYear = i.year
        currentMonth = i.month
        currentDay = i.day

        if(birthYear <= currentYear):
            if(calc.isLeap(birthYear) == True and birthMonth == 2):
                if (29 >= birthDay):
                    print("Leap Feb")
                    return calc.justCalc(birthYear,birthMonth,birthDay,currentDay,currentMonth,currentYear)
                else:
                    print ("Please check your date input!")
            elif(calc.isLeap(birthYear) == False and birthMonth == 2):
                print("Non-Leap Feb")
                if (28 >= birthDay):
                    return calc.justCalc(birthYear,birthMonth,birthDay,currentDay,currentMonth,currentYear)
                else:
                    print ("Please check your date input!")
            else:
                print("Not Feb")
                return calc.justCalc(birthYear,birthMonth,birthDay,currentDay,currentMonth,currentYear)
        else:
            return "You have not born yet? Your birthday is in future!"

    def daysTill():

        inp = input("Enter your date of birth (dd/mm/yyyy): ")
        inp_list = inp.split('/')
        numbers = [int(x.strip()) for x in inp_list]
        #print(numbers[2])
        birthYear = numbers[2]
        birthMonth = numbers[1]
        birthDay = numbers[0]

        i = datetime.datetime.now()
        currentYear = i.year
        currentMonth = i.month
        currentDay = i.day

        #condtion when the currentMonth is smaller than birthMonth
        if (currentMonth <  birthMonth and birthMonth <= 12):
            cD = date(currentYear, currentMonth, currentDay)
            bD = date(currentYear, birthMonth, birthDay)
            dayCalc = bD - cD
            return '{} days.'.format(dayCalc.days)
            #print(delta.days)

        #condtion when the currentMonth is same as the moth entered
        elif (currentMonth == birthMonth):
            if (currentDay == birthDay):
                return "HAPPY BIRTHDAY"

            elif (currentDay < birthDay):
                cD = date(currentYear, currentMonth, currentDay)
                bD = date(currentYear, birthMonth, birthDay)
                dayCalc = bD - cD
                return '{} days.'.format(dayCalc.days)

            elif(currentDay > birthDay):
                nextYear = currentYear + 1
                cD = date(currentYear, currentMonth, currentDay)
                bD = date(nextYear, birthMonth, birthDay)
                dayCalc = bD - cD
                return '{} days.'.format(dayCalc.days)

            else:
                print("Sorry, something went wrong!")

        elif (currentMonth > birthMonth):
            nextYear = currentYear + 1
            cD = date(currentYear, currentMonth, currentDay)
            bD = date(nextYear, birthMonth, birthDay)
            dayCalc = bD - cD
            return '{} days.'.format(dayCalc.days)

        else:
            print("Sorry, something went wrong!")

    def justCalc(birthYear,birthMonth,birthDay,currentDay,currentMonth,currentYear):
        if (currentMonth <  birthMonth and birthMonth <= 12):
            cD = date(currentYear, currentMonth, currentDay)
            bD = date(currentYear, birthMonth, birthDay)
            dayCalc = bD - cD
            return '{} days.'.format(dayCalc.days)
            #print(delta.days)

        #condtion when the currentMonth is same as the moth entered
        elif (currentMonth == birthMonth):
            if (currentDay == birthDay):
                return "HAPPY BIRTHDAY"

            elif (currentDay < birthDay):
                cD = date(currentYear, currentMonth, currentDay)
                bD = date(currentYear, birthMonth, birthDay)
                dayCalc = bD - cD
                return '{} days.'.format(dayCalc.days)

            elif(currentDay > birthDay):
                nextYear = currentYear + 1
                cD = date(currentYear, currentMonth, currentDay)
                bD = date(nextYear, birthMonth, birthDay)
                dayCalc = bD - cD
                return '{} days.'.format(dayCalc.days)

            else:
                print("Sorry, something went wrong!")

        elif (currentMonth > birthMonth):
            nextYear = currentYear + 1
            cD = date(currentYear, currentMonth, currentDay)
            bD = date(nextYear, birthMonth, birthDay)
            dayCalc = bD - cD
            return '{} days.'.format(dayCalc.days)

        else:
            print("Sorry, something went wrong!")

    #this function will help decide if the year is a leap year or not
    def isLeap(year):
        if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return True
        else:
            return False

print(calc.impVal())
#print(calc.isLeap(2017))
"""
year = 2016
if(calc.isLeap(year) == True):
    print("366")
else:
    print("365")
"""
