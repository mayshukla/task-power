# Task class
# relies on standard datetime module
from datetime import date, timedelta

class Task:

    def __init__(self, task_name, units_name, units_count, starty, startm, startd, endy, endm, endd):

        self.task_name = task_name
        self.units_name = units_name
        self.units_count = units_count
        self.startdate = date(starty, startm, startd) # convert to a datetime.date object
        self.enddate = date(endy, endm, endd)

    def get_duration(self):
        # returns duration in days
        duration_delta = self.enddate - self.startdate # datetime.delta object
        return duration_delta.days

    def get_required_rate(self):
        # returns a number respresenting units per day
        return self.units_count / self.get_duration()
