from datetime import date

from Task import Task

# TODO: error checking (missing parameters)

def parse_task(buf):
    # takes in string of raw data from .task file and returns Task object

    # initialize variables to store Task object properties
    task_name = ''
    units_name = ''
    units_count = 0
    work_periods = []       
 
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

        elif buf[i][0].lower() == 'work periods':
            # split at commas
            buf[i][1] = buf[i][1].split(',')
            
            for j in range(0, len(buf[i][1])):
                # remove leading and trailing whitespace
                buf[i][1][j] = buf[i][1][j].strip()

                # split start dates and end dates at dashes
                buf[i][1][j] = buf[i][1][j].split('-')
                
                for k in range(0, len(buf[i][1][j])):
                    buf[i][1][j][k] = buf[i][1][j][k].strip()
                    # split year/month/day at slash
                    buf[i][1][j][k] = buf[i][1][j][k].split('/')

                    for l in range(0, len(buf[i][1][j][k])):
                        buf[i][1][j][k][l] = buf[i][1][j][k][l].strip(
)
                starty = int(buf[i][1][j][0][0])
                startm = int(buf[i][1][j][0][1])
                startd = int(buf[i][1][j][0][2])

                endy   = int(buf[i][1][j][1][0])
                endm   = int(buf[i][1][j][1][1])
                endd   = int(buf[i][1][j][1][2])

                work_periods.append([date(starty, startm, startd), date(endy, endm, endd)]) 

    return Task(task_name, units_name, units_count, work_periods)
