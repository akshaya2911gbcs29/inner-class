import gc
class employee:
    class address:
        def __init__(self, city, state):
            self.city = city
            self.state = state
        def display(self):
            print(self.city, self.state)
    def __init__(self, emp_id, name, city, state):
        self.emp_id = emp_id
        self.name = name
        self.address = self.address(city, state)
    def display(self):
        print(self.emp_id, self.name)
        self.address.display()
n = int(input("Enter no of employee: "))
emp_list = []
for i in range(n):
    emp_id = int(input("Enter employee id: "))
    name = input("Enter name: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    e = employee(emp_id, name, city, state)
    emp_list.append(e)
print("\n----Before deletion----")
for e in emp_list:
    e.display()
search_id = int(input("\nEnter employee id to remove: "))
found = False
for e in emp_list:
    if e.emp_id == search_id:
        print(f"Removing Employee ID: {e.emp_id}")
        emp_list.remove(e)
        del e
        found = True
        break
if not found:
    print("Employee ID not found.")
gc.collect()
print("\n----After deletion----")
if not emp_list:
    print("No employees left.")
else:
    for e in emp_list:
        e.display()

