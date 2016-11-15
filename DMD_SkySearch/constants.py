token = "290131664:AAF2slLW_MdetguEo9Y9zNW6tvQuKwBUvHM"

class User:
    id = -1
    status = ""
    city = ""
    from_city = ""
    to_city = ""
    feedback = ""
    def __init__(self, id, status):
        self.id = id
        self.status = status