class Person:
    def __init__(self, fn, ln):
        self._first = fn
        self._last = ln

    def get_name(self):
        return self._first +" "+ self._last

class Student(Person):
    def __init__(self, fn, ln, gpa):
        super().__init__(fn, ln)
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, fn, ln, numstu):
        super().__init__(fn, ln)
        self.numstu = numstu

class Admin(Person):
    def __init__(self, fn, ln, favword):
        super().__init__(fn, ln)
        self.favword = favword
