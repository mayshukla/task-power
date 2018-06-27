from pathlib import Path

from Task import Task
from parse_task import parse_task

def read_taskfiles(taskfiles_path):
    # return a list of Task objects based on all the .task files in the taskfile directory
    # taskfiles_path should be path object returned by init_taskfiles_directory()
    
    taskfiles_list = taskfiles_path.glob('*.task')    
    
    Task_list = []    

    for taskfile in taskfiles_list:
        buf = taskfile.read_text()
        Task_list.append(parse_task(buf))

    return Task_list
