from pathlib import Path
from datetime import date, timedelta

from Task import Task

def task_creation_wizard(taskfiles_path):
    # prompts user for input and creates .task file in taskfiles directory
    # taskfiles_path should be Path object returned by init_taskfiles_directory()

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
