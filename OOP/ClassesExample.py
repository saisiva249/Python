# here we will have the students and courses
# for courses we will add students only when students are less than acceptable

# Defining class Students
class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100
    
    def get_Grade(self):
        return self.grade

class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_Student(self, student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_AverageGrade(self):
        total_Grade = 0
        for student in self.students:
            total_Grade += student.get_Grade()
        return total_Grade/len(self.students)

student1 = Student("Venkata", 28, 90)
student2 = Student("Sai", 29, 93)

course1 = Course("Science", 3)
course1.add_Student(student1)
course1.add_Student(student2)
print("Average %s"%course1.get_AverageGrade())
        
    
        