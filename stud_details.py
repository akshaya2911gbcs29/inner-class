import sys
import gc
class university:
    def __init__(self,university_name):
        self.university_name=university_name
        self.students=[]
    def add_student(self,rollno,name):
        s=student(rollno,name,self)
        self.students.append(s)
        print(f"Added {name},Ref count:",sys.getrefcount(s))
    def remove_student(self,rollno):
        for s in self.students:
            if s.rollno==rollno:
                print("Removing:",s.name,"Ref count:",sys.getrefcount(s))
                self.students.remove(s)
                del s
                gc.collect()
                print("Removed & GC Done")
                return
    def display_all(self):
        for s in self.students:
            s.display_details()
class student:
    def __init__(self,rollno,name,university):
        self.rollno=rollno
        self.name=name
        self.university=university
    def display_details(self):
        print(f"Roll no:{self.rollno},Name:{self.name},University:{self.university.university_name}")
uname=input("Enter University Name: ")
U=university(uname)
n=int(input("Enter number of students:"))
for i in range(n):
    roll=int(input("Enter rollno:"))
    name=input("Enter name:")
    U.add_student(roll,name)
U.display_all()
r=int(input("Enter rollno to remove: "))
U.remove_student(r)
U.display_all()
