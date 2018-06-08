# Reusable functions for dealing with dates

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
