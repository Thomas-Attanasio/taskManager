taskList = []

def addNewTask(newTask):
    if newTask and newTask.strip():
        taskList.append(newTask)

def showTasks():
    return taskList