from Habit import *

def isBacklogItem(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
    return (isImportant == False) and (isUrgent == False) and (isLessImportant == False) and (isLessUrgent == False)


processToDos(isBacklogItem, printTodo)