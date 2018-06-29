# standard python modules
from datetime import date, timedelta

# my modules
from init_taskfiles_directory import init_taskfiles_directory
from datetools import convert_weekday_to_string
from Task import Task
from read_taskfiles import read_taskfiles
from hud import hud
from task_creation_wizard import task_creation_wizard

if __name__ == '__main__':

    # Initialize taskfiles directory and store in variable to pass when saving stuff to .task files
    taskfiles_path = init_taskfiles_directory()

    # Generate text for heads up display
    hud_text = hud(taskfiles_path, date.today())
    print(hud_text)
    
    user_selection = input('Would you like to create a new task? (y/n) ')
    if user_selection.lower() == 'y':
        # Prompt user for input and create .task file in taskfiles directory
        task_creation_wizard(taskfiles_path)
