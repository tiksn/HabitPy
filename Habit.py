from habitipy import Habitipy, load_conf,DEFAULT_CONF
conf = load_conf(DEFAULT_CONF)
api = Habitipy(conf)

importantTagId = conf.get("Important")
urgentTagId = conf.get("Urgent")
lessImportantTagId = conf.get("LessImportant")
lessUrgentTagId = conf.get("LessUrgent")
