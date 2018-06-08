# Task class
# relies on standard datetime module
from datetime import date, timedelta

class Task:

    def __init__(self, name, starty, startm, startd, endy, endm, endd):

        self.name = name
        self.startdate = date(starty, startm, startd) # convert to a datetime.date object
        self.enddate = date(endy, endm, endd)

    def get_duration(self):
        # returns duration in days
        duration_delta = self.enddate - self.startdate # datetime.delta object
        return duration_delta.days
