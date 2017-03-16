import datetime
from datetime import date

class test:
    """docstring for test"""
    def cTime():
        i = datetime.datetime.now()
        print("")
        cYear = i.year
        cMonth = i.month
        cDay = i.day

        """
        print("cYear = ", cYear)
        print("cMOnth = ", cMonth)
        print("cDay = ", cDay)
        """
        return 'The current date is - {}/{}/{}'.format(cDay, cMonth, cYear)

    def dateCalc():
        d0 = date(2008, 8, 18)
        d1 = date(2008, 8, 19)
        delta = d1 - d0
        print(delta.days)

    def tt():
        print(test.cTime())

print(test.cTime())
print(test.tt())

