from Habit import *
import str2bool as s2b

def isBacklogItem(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
    return (isImportant == False) and (isUrgent == False) and (isLessImportant == False) and (isLessUrgent == False)

def prioritizeTodo(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
    printTodo(todo, isImportant, isUrgent, isLessImportant, isLessUrgent)
    markAsImportant = s2b.str2bool_exc(input("Is this to-do important? "))
    markAsUrgent = s2b.str2bool_exc(input("Is this to-do urgent? "))

    tagsToRemove = []
    tagsToAdd = []

    if isImportant and (not markAsImportant):
        tagsToRemove.append(importantTagId)
    if isLessImportant and markAsImportant:
        tagsToRemove.append(lessImportantTagId)
    if isUrgent and (not markAsUrgent):
        tagsToRemove.append(urgentTagId)
    if isLessUrgent and markAsUrgent:
        tagsToRemove.append(lessUrgentTagId)
    
    if markAsImportant and (not isImportant):
        tagsToAdd.append(importantTagId)
    if (not markAsImportant) and (not isLessImportant):
        tagsToAdd.append(lessImportantTagId)
    if markAsUrgent and (not isUrgent):
        tagsToAdd.append(urgentTagId)
    if (not markAsUrgent) and (not isLessUrgent):
        tagsToAdd.append(lessUrgentTagId)
    
    print(tagsToRemove)
    print(tagsToAdd)
processToDos(isBacklogItem, prioritizeTodo)