from habitipy import Habitipy, load_conf,DEFAULT_CONF
conf = load_conf(DEFAULT_CONF)
api = Habitipy(conf)

for tag in api.tags.get():
    print(tag)