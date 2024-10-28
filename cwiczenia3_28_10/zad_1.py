class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50

student1 = Student("Jan", [60, 70, 80])
student2 = Student("Anna", [40, 45, 50])

print(student1.name, "passed:", student1.is_passed())
print(student2.name, "passed:", student2.is_passed())
