from pathlib import Path

def init_taskfiles_directory():
# creates taskfiles directory if none exists
# returns Path object for taskfiles directory

    taskfiles_path = Path('../taskfiles')
    if taskfiles_path.exists():
        print('taskfiles directory exists')
    else:
        print('No taskfiles directory found. Creating new one.')
        taskfiles_path.mkdir()

    return taskfiles_path
