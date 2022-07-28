class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date

    @classmethod
    def MakeDigit(cls, param):
        par = param.split('-')
        global d, m, y
        d = int(par[0])
        m = int(par[1])
        y = int(par[2])
        #print(d, m, y)
        return Date(param)

    @staticmethod
    def DateCheck():
        if d > 0 and d <= 31 and m > 0 and m <= 12 and y > 0:
            pass
        else:
            print('Enter the correct date!')


dmy = Date.MakeDigit(input("Enter the date as date-month-year:"))
Date.DateCheck()

print(dmy.date)