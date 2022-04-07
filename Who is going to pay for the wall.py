def who_is_paying(name):
    if len(name) > 2:
        a = [name , name[0:2]]
        return a
    else:
        return [name]