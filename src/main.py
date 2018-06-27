# standard python modules
from datetime import date, timedelta

# my modules
from init_taskfiles_directory import init_taskfiles_directory
from datetools import convert_weekday_to_string
from Task import Task
from read_taskfiles import read_taskfiles

if __name__ == '__main__':

    # Initialize taskfiles directory and store in variable to pass when saving stuff to .task files
    taskfiles_path = init_taskfiles_directory()

    Task_list = read_taskfiles(taskfiles_path)
    for task in Task_list:
        print(task.task_name)

    # Testing Task class with user input
    task_name = input('Enter task name: ')
    units_name = input('Enter name of units (plural): ')
    units_count = input('Enter total number of units to complete: ')

    work_periods_count = int(input('Enter number of work periods: '))

    # create nested list of date objects
    # see Task class
    work_periods = []
    for i in range(0, work_periods_count):
        print('---New work period---')

        starty = int(input('Enter start year: '))
        startm = int(input('Enter start month: '))
        startd = int(input('Enter start day: '))

        endy = int(input('Enter end year: '))
        endm = int(input('Enter end month: '))
        endd = int(input('Enter end day: '))

        work_periods.append([date(starty, startm, startd), date(endy, endm, endd)])
    
    my_task = Task( task_name,
                    units_name,
                    units_count,
                    work_periods)

    my_task.save_to_file(taskfiles_path)
