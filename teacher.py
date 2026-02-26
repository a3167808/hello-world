from person import Person

class Teacher(Person):
    def __init__(self, name, gender, staffId):
        super().__init__(name, gender)
        self.staffId = staffId

    