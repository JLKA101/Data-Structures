#student mark record
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    #getter and setter method

    def get_marks(self):
        return self.marks

    def set_marks(self, new_marks):
        self.marks = new_marks

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

student1 = Student(name, marks)

print("Current marks: ", student1.get_marks())

new_marks = int(input("Enter updated marks: "))
student1.set_marks(new_marks)

print("Updated marks: ", student1.get_marks())

