from pathlib import Path

from read_taskfiles import read_taskfiles

def hud(taskfiles_path, current_date):
    # generate text to use as a heads up display
    # taskfiles_path should be Path object

    hud_text = ''
    active_tasks = []
    inactive_tasks = []

    all_tasks = read_taskfiles(taskfiles_path)

    # check if today is in a work period for each task and sort accordingly
    for task in all_tasks:
        if task.is_active(current_date):
            active_tasks.append(task)
        else:
            inactive_tasks.append(task)

    # add stuff to hud
    hud_text += 'Active tasks:\n'

    for active_task in active_tasks:
        hud_text += active_task.task_name + '\n'

    hud_text += '\n'    

    hud_text += 'Inactive tasks:\n'

    for inactive_task in inactive_tasks:
        hud_text += inactive_task.task_name + '\n'

    return hud_text
