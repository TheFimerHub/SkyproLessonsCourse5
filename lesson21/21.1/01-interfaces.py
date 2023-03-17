
#01-user-class.py

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def change_password(self, old_password, new_password): # public
        self._is_password_correct(old_password)
        self._is_password_valid(new_password)
        self._was_password_used(new_password)

    def _is_password_correct(self, old_password): #protected - underscore
        pass

    def __is_password_valid(self, new_password): #private - dunder
        pass

    def was_password_used(self, new_password):
        pass

user = User('John', '123456')


#02-class-example.py

class SomeClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def print(self):
        print(self._concat())

    def _concat(self):
        return f"{self.var1} {self.var2}"

object_1 = SomeClass(var1="Hello", var2="World")

object_1.print()










