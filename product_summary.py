import sys
class product:
    def __init__(self, name):
        self.name = name
    class specification:
        def __init__(self, weight):
            self.weight = weight
    def add_spec(self, weight):
        spec = self.specification(weight)
        print("spec Ref", sys.getrefcount(spec))
        return spec
class supplier:
    def __init__(self, name):
        self.name = name
n = int(input("Enter number of products: "))
product_list = []
for i in range(n):
    print(f"\n--- Product {i + 1} ---")
    pname = input("Enter product name: ")
    weight = input("Enter product weight: ")
    sname = input("Enter supplier name: ")
    p = product(pname)
    spec = p.add_spec(weight)
    s = supplier(sname)
    product_list.append((p, spec, s))
print("\n--- Summary of All Products ---")
for p, spec, s in product_list:
    print(f"Product: {p.name} | Supplier: {s.name} | Weight: {spec.weight}")

