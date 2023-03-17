
#01-basic-class.py

# class CatFirst:
#     def __init__(self):
#         self.say = "meow"
#
#     def meow(self):
#         print(self.say)


#01-class-atribures.py

# class Cat:
#     color = "gray"
#     breed = "deafult"
#     name = "umcnown"
#     total_snacks = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_snack(self):
#         Cat.total_snacks += 1
#
#     def get_snack(self):
#         return Cat.total_snacks
#
#     @classmethod
#     def ger_deafult(cls):
#         return cls.name
#
# cat_1 = Cat("Tom")
# cat_1.add_snack()
#
# cat_2 = Cat("George")
#
# cat_2.add_snack()
#
# Cat.color = "red"
#
# print(Cat.color)
# print(Cat.breed)
# print(Cat.name)
#
# print(cat_1.color)
# print(cat_1.breed)
# print(cat_1.name)
#
# print(cat_1.get_snack())
# print(Cat.ger_deafult())

#05-class-scope-test.py

class Cat:
    name = "deafault"

    def __init__(self):
        self.name = "new_name"

    def get_name(self):
        return self.name

cat_1 = Cat()
print(cat_1.get_name())