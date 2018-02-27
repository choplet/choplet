from datetime import datetime




class Course():
    def __init__(self, name, price):
        self.name = name
        self.teacher = None
        self.price = price

    def get_name(self):
        return self.name

    def add_teacher(self, teacher):
        self.teacher = teacher.get_name()

    def __str__(self):
        return ('Course: {}  \nPrice: {} \nTeacher: {}').format(self.name, self.price, self.teacher)


class Group():
    def __init__(self, name):
        self.name = name
        self.teacher = None
        self.course  = None
        self.students = []

    def get_name(self):
        return self.name

    def add_teacher(self, teacher):
        self.teacher = teacher.get_name()

    def add_course(self, course):
        self.course = course.get_name()

    def add_student(self, student):
        self.students.append (student.get_name())

    def __str__(self):
        return ('\nGroup: {} \nCourse: {} \nTeacher: {}   \nStudents: {} ').format(self.name, self.course, self.teacher, self.students)


class Teacher():
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def get_name(self):
        return self.name


class Student():
    def __init__(self, age, name, course):
        self.age = age
        self.name = name
        self.course = course

    def get_name(self):
        return self.name


student_bob = Student(20, "Bob", "Python")
student_rob = Student(21, "Rob", "Python")
student_dob = Student(21.5, "Dob", "Python")



teacher_linus = Teacher("Linus Torvalds", ["C++","Java"])
#print(teacher_linus.skills)


course_py = Course( "Python", "500$")
course_py.add_teacher(teacher_linus)
print(course_py)

group1 = Group("1")
group1.add_teacher(teacher_linus)
group1.add_course(course_py)
group1.add_student(student_bob)
group1.add_student(student_rob)

print(group1)
