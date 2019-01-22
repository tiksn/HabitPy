from habitipy import Habitipy, load_conf,DEFAULT_CONF
conf = load_conf(DEFAULT_CONF)
api = Habitipy(conf)

importantTagId = conf.get("Important")
urgentTagId = conf.get("Urgent")
lessImportantTagId = conf.get("LessImportant")
lessUrgentTagId = conf.get("LessUrgent")

def processToDos(selector, processor):
    todos = api.tasks.user.get(type = "todos")
    for todo in todos:
        tags = todo["tags"]
        isImportant = True if importantTagId in tags else False
        isUrgent = True if urgentTagId in tags else False
        isLessImportant = True if lessImportantTagId in tags else False
        isLessUrgent = True if lessUrgentTagId in tags else False
        if selector(todo, isImportant, isUrgent, isLessImportant, isLessUrgent):
            processor(todo, isImportant, isUrgent, isLessImportant, isLessUrgent)