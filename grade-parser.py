# Classes
class Student:
    def __init__(self, ID, fName, lName, score, participation, city=None, state=None):
        self.ID = ID
        self.fName = fName
        self.lName = lName
        self.score = score
        self.participation = participation
        self.city = city
        self.state = state
        self.letterGrade = None

# Variable for storing student objects
students = []