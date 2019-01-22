from Habit import *
import str2bool as s2b

def isBacklogItem(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
    return (isImportant == False) and (isUrgent == False) and (isLessImportant == False) and (isLessUrgent == False)

def prioritizeTodo(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
    printTodo(todo, isImportant, isUrgent, isLessImportant, isLessUrgent)
    markAsImportant = s2b.str2bool_exc(input("Is this to-do important? "))
    markAsUrgent = s2b.str2bool_exc(input("Is this to-do urgent? "))

    importancyTagId = importantTagId if markAsImportant else lessImportantTagId
    urgencyTagId = urgentTagId if markAsUrgent else lessUrgentTagId

    print(dir(todo["tags"]))
processToDos(isBacklogItem, prioritizeTodo)