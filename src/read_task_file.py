from parse_task import parse_task
from Task import Task

def read_task_file(task_name):
    # Reads properties from file <task_name.task> and returns Task object

    try:
        with open('{}.task'.format(task_name), 'r') as f:
            buf = f.read()
            return parse_task(buf)
    except FileNotFoundError:
        print('Could not find file called {}.task'.format(task_name))
