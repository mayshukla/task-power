# Reusable functions for dealing with dates
# Uses the following standard python modules: datetime
# Note: weekday() returns int, where Monday is 0, Sunday is 6

from datetime import date, timedelta

def convert_weekday_to_string(weekday_int):
    weekday_dict = {0 : 'monday',
                    1 : 'tuesday',
                    2 : 'wednesday',
                    3 : 'thursday',
                    4 : 'friday',
                    5 : 'saturday',
                    6 : 'sunday'}

    return weekday_dict[weekday_int]

if __name__ == '__main__':

    # Testing convert_weekday_to_string
    for i in range(0,7):
        print(convert_weekday_to_string(i))

    # Testing date and timedelta objects
    mydate = date(2018, 6, 6)
    print('Date 1:')
    print('y:{} m:{} d:{} weekday:{}'.format(mydate.year, mydate.month, mydate.day, convert_weekday_to_string(mydate.weekday() )))
    
    date2 = date(2018, 6, 12)
    print('Date 2:')
    print('y:{} m:{} d:{} weekday:{}'.format(date2.year, date2.month, date2.day, convert_weekday_to_string(date2.weekday() )))
    mytimedelta = date2 - mydate # creates a timedelta object
    print('That\'s a difference of {} days.'.format(mytimedelta.days))
