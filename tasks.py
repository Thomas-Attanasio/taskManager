taskList = []

def addNewTask(newTask):
    if newTask and newTask.strip():
        taskList.append(newTask)

def deleteTask(index):
    if 0 <= index < len(taskList):
        taskList.pop(index)

def showTasks():
    return taskList