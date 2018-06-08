from datetools import convert_weekday_to_string
from Task import Task

if __name__ == '__main__':

    # Testing Task class
    myTask = Task('math worksheet', 'questions', 60, 2018, 6, 6, 2018, 6, 12)
    print('The task called "{}" takes {} days'.format(myTask.task_name, myTask.get_duration()))
    print('You need to complete {} {} per day'.format(myTask.get_required_rate(), myTask.units_name))
