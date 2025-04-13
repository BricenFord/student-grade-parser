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

# Open and parse input.txt
with open("input.txt", "r") as file:
    input_data = file.read()
    text = input_data.split()
    studentIDIndexes = []
    for i, word in enumerate(text):
        if word.isdigit() and len(word) == 9:
            studentIDIndexes.append(i)

    # Create student objects for all indexes except the last
    for i in range(len(studentIDIndexes) - 1):
        counter = 0
        ID = fName = lName = score = participation = city = state = None
        for j in range(studentIDIndexes[i], studentIDIndexes[i+1]):
            match counter:
                case 0:
                    ID = text[j]
                case 1:
                    fName = text[j]
                case 2:
                    lName = text[j]
                case 3:
                    score = text[j]
                case 4:
                    participation = text[j]
                case 5:
                    city = text[j]
                case 6:
                    state = text[j]
            counter += 1
        students.append(Student(ID, fName, lName, score, participation, city, state))

    # Handle last record (not covered in the loop)
    if studentIDIndexes:
        last_index = studentIDIndexes[-1]
        counter = 0
        ID = fName = lName = score = participation = city = state = None
        for j in range(studentIDIndexes[-1], len(text)):
            match counter:
                case 0:
                    ID = text[j]
                case 1:
                    fName = text[j]
                case 2:
                    lName = text[j]
                case 3:
                    score = text[j]
                case 4:
                    participation = text[j]
                case 5:
                    city = text[j]
                case 6:
                    state = text[j]
            counter += 1
        students.append(Student(ID, fName, lName, score, participation, city, state))

# Sort students by score descending, then participation (E > L)
students.sort(key=lambda s: (-int(s.score), s.participation != 'E'))

# Assign grades based on ranking
n = len(students)
third = n // 3
tenth = -(-n // 10)  # ceil(n/10) without math module

for idx, student in enumerate(students):
    if idx < third:
        student.letterGrade = "A"
    elif idx < 2 * third:
        student.letterGrade = "B"
    elif idx >= n - tenth:
        student.letterGrade = "F"
    else:
        student.letterGrade = "C" if student.participation == 'E' else "D"

# Final sort by last name, first name, then ID
students.sort(key=lambda s: (s.lName, s.fName, s.ID))