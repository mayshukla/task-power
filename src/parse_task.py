from Task import Task

# TODO: error checking (missing parameters)

def parse_task(buf):
    # takes in string of raw data from .task file and returns Task object

    # initialize variables to store Task object properties
    task_name = ''
    units_name = ''
    units_count = 0
    starty = 0
    startm = 0
    startd = 0
    endy = 0
    endm = 0
    endd = 0

    # split newlines
    buf = buf.splitlines()

    # split at colon
    for i in range(0, len(buf)):
        buf[i] = buf[i].split(':')

    # remove leading and trailing whitespace
        for j in range(0, len(buf[i])): # there should only be two elements in buf[i]
            buf[i][j] = buf[i][j].strip()

    # read parameters
    # parameter names such as 'Task name' are not case sensitive
    for i in range(0, len(buf)):
        if buf[i][0].lower() == 'task name':
            task_name = buf[i][1]
        elif buf[i][0].lower() == 'units name':
            units_name = buf[i][1]
        elif buf[i][0].lower() == 'number of units':
            units_count = int(buf[i][1])
        elif buf[i][0].lower() == 'start date':
            # split date at periods
            start_date = buf[i][1].split('.')
            starty = int(start_date[0])
            startm = int(start_date[1])
            startd = int(start_date[2])
        elif buf[i][0].lower() == 'end date':
            # split date at periods
            end_date = buf[i][1].split('.')
            endy = int(end_date[0])
            endm = int(end_date[1])
            endd = int(end_date[2])

    return Task(task_name, units_name, units_count, starty, startm, startd, endy, endm, endd)
