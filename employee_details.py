import sys
import gc
class company:
    def __init__(self, cname):
        self.cname = cname
        self.employees = []
    class employee:
        def __init__(self, emp_id, emp_name, company):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.company = company
        def display(self):
            print(f"ID: {self.emp_id}, Name: {self.emp_name}, Company: {self.company.cname}")
    def add_employee(self, emp_id, emp_name):
        e = self.employee(emp_id, emp_name, self)
        self.employees.append(e)
        print("Added:", emp_name, "Ref:", sys.getrefcount(e))
    def remove_employee(self, emp_id):
        for e in self.employees:
            if str(e.emp_id) == str(emp_id):  # Ensure ID types match for comparison
                print("Removing:", e.emp_name, "Ref:", sys.getrefcount(e))
                self.employees.remove(e)  # Actually remove from list
                del e
                gc.collect()
                print("Removed & GC Done")
                return
        print("Employee not found.")
    def display_all(self):
        for e in self.employees:
            e.display()
cname = input("Enter company name: ")
c = company(cname)
n = int(input("Enter no of employees: "))
for i in range(n):
    emp_id = input("Enter employee id: ")
    name = input("Enter employee name: ")
    c.add_employee(emp_id, name)
print("\n--- Current Employees ---")
c.display_all()
r = input("\nEnter id to remove: ")
c.remove_employee(r)
print("\n--- Final Employee List ---")
c.display_all()
