
#01-attributes.py

class Player:
    def __init__(self):
        self._hits = 0

    def add_hit(self):
        self._hits += 1


#02-setter.py

class User:
    def __init__(self, name):
        self._name = name

    def set_name(self, new_name):
        self._name = new_name

user_1= User("John")
# user_1.name - "Artur"
user_1.set_name("Artur")


#03-getter.py

class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

user_1= User("John")
user_1.get_name()


#04-getset.py

class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

user_1 = User("John")
user_1.get_name()

user_1 = User("Artur")
user_1.set_name()