import datetime
import re
class Date:
    def __init__(self,datestring):
        if len(re.findall(r'\d{2}-\d{2}-\d{4}',datestring)) == 0:
            print('Неверная строка даты, пожалуйста введите в формате дд-мм-гггг')
            raise ValueError
        self.datestring = datestring

    @staticmethod
    def check_date(day,month,year):
        try:
            datetime.date(year, month, day)
        except ValueError as err:
            print(err)
        else:
            print('все хорошо')
    @classmethod
    def extract_numbers(cls, datestring):
        if len(re.findall(r'\d{2}-\d{2}-\d{4}',datestring)) == 0:
            print('Неверная строка даты, пожалуйста введите в формате дд-мм-гггг')
            return None
        __array=datestring.split('-')
        return list(map(lambda x:int(x),__array))

mydate = Date('09-09-2020')
Date.check_date(20,1,2020)
Date.check_date(30,2,2020)
Date.check_date(23,13,2020)
Date.check_date(23,12,-2020)
print(Date.extract_numbers('20-02-2000'))