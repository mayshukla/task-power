from datetools import convert_weekday_to_string
from Task import Task

if __name__ == '__main__':

    # Testing Task class
    #my_task = Task('math worksheet', 'questions', 60, 2018, 6, 6, 2018, 6, 12)
    #print('The task called "{}" takes {} days'.format(my_task.task_name, my_task.get_duration()))
    #print('You need to complete {} {} per day'.format(my_task.get_required_rate(), my_task.units_name))

    # Testing Task class with user input
    input_task_name = input('Enter task name: ')
    input_units_name = input('Enter name of units (plural): ')
    input_units_count = int(input('Enter number of units: '))

    input_starty = int(input('Enter start year: '))
    input_startm = int(input('Enter start month: '))
    input_startd = int(input('Enter start day: '))

    input_endy = int(input('Enter end year: '))
    input_endm = int(input('Enter end month: '))
    input_endd = int(input('Enter end day: '))

    my_task = Task( input_task_name,
                    input_units_name,
                    input_units_count,
                    input_starty,
                    input_startm,
                    input_startd,
                    input_endy,
                    input_endm,
                    input_endd,)
    print('The task called "{}" takes {} days'.format(my_task.task_name, my_task.get_duration()))
    print('You need to complete {} {} per day'.format(my_task.get_required_rate(), my_task.units_name))

    my_task.save_to_file()
