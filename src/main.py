from datetools import convert_weekday_to_string
from Task import Task

if __name__ == '__main__':

    # Testing Task class
    myTask = Task('clean room', 2018, 6, 6, 2018, 6, 12)
    print('The task called "{}" takes {} days'.format(myTask.name, myTask.get_duration()))