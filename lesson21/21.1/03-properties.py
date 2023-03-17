
#01-property.py

class Cat:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

cat = Cat('Tom')
# name = cat.name()
name = cat.name
print(name)

#02-student.py

class Student:
    def __init__(self, name, course):
        self._name = name
        self._course = course

    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return self._course

student = Student('John', 2)

student_name = student.name
student_course = student.course

#03-setter.py

class Student:
    def __init__(self, name, course):
        self._name = name
        self._course = course

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value


student = Student('Misha', 2)

student.name = "New name"
student.course = 3