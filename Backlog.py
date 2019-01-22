from Habit import *

def isBacklogItem(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
    return (isImportant == False) and (isUrgent == False) and (isLessImportant == False) and (isLessUrgent == False)

def printTodo(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
    print("To-Do: " + todo["text"])
    print("\t" + todo["notes"])
    if todo["notes"] != "":
        print()

processToDos(isBacklogItem, printTodo)