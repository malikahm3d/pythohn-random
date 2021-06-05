class Student:
    def __init__(self, name, major, GPA, is_on_probation):
        self.name = name
        self.major = major
        self.GPA = GPA
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.GPA >= 3.5 :
            return True
        else:
            return False
    