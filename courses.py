import sys
class student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    class course:
        def __init__(self, cname):
            self.cname = cname
    def add_course(self, cname):
        c = self.course(cname)
        self.courses.append(c)
        print("Added:", cname, "Ref:", sys.getrefcount(c))
    def display(self):
        print("Student:", self.name)
        for c in self.courses:
            print("Course:", c.cname)
num_students = int(input("Enter no. of students: "))
student_list = []
for j in range(num_students):
    name = input(f"\nEnter name for student {j + 1}: ")
    s = student(name)
    n = int(input(f"Enter no. of courses for {name}: "))
    for i in range(n):
        cname = input("Enter course name: ")
        s.add_course(cname)
    student_list.append(s)
print("\n--- All Students Data ---")
for s in student_list:
    s.display()

