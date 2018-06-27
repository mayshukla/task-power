# Reusable functions for dealing with dates

from datetime import date, timedelta

def convert_weekday_to_string(weekday_int):
    # Note: date.weekday() returns int, where Monday is 0, Sunday is 6
    weekday_dict = {0 : 'monday',
                    1 : 'tuesday',
                    2 : 'wednesday',
                    3 : 'thursday',
                    4 : 'friday',
                    5 : 'saturday',
                    6 : 'sunday'}

    return weekday_dict[weekday_int]

def is_in_range(date, range_start, range_end):
    # checks if date is on or between range_start and range_date
    # all arguments should be date objects

    if (date - range_start).days >= 0 and (range_end - date).days >= 0:
        return True
    else:
        return False
