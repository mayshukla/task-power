from datetime import date, timedelta

from Task import Task

task_name = 'sweep'
units_name = 'tiles'
units_count = 21
work_periods = [ [date(2018, 1, 1), date(2018, 1, 4)], \
                 [date(2018, 2, 1), date(2018, 2, 3)]]

my_task = Task(task_name, units_name, units_count, work_periods)

print(my_task.get_required_rate())

my_task.save_to_file()
