class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name  =name


    def say_hi(self):
        print("Hi")

    def __str__(self):
        return "Animal"


class Cat(Animal):
    # cat inherits name age and say_hi
    def __init__(self, name, age, sound):
        #Animal.__init__(name, age)
        super().__init__(name, age)
        self.sound = sound

    def say_sound(self):
        print(self.sound)

    def __str__(self):
        return "Cat:" + self.name


cat = Cat("Cool (beans)", 67, "Fuck off")
cat.say_hi()
cat.say_sound()
print(cat)
