# inherits, kita bisa extend, override
class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} working...")


class SoftwareEngineer(Employee):
    def __init__(self, name, age, level, salary) -> None:
        super().__init__(name, age, salary)
        self.level = level

    # extend method
    def debug(self):
        print(f"{self.name} is debugging")

    # override method
    def work(self):
        print(f"{self.name} is coding...")


class Designer(Employee):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age, salary)

    def draw(self):
        print(f"{self.name} is drawing")

    def work(self):
        print(f"{self.name} is designing...")


se = SoftwareEngineer("alice", 20, "junior", 2000)
de = Designer("bob", 23, 3000)
print(se.name)
print(de.name)

se.work()

se.debug()
de.draw()

print(f"--------------------------polymorphism--------------------------")

# polymorphism

employee = [
    SoftwareEngineer("charle", 20, "junior", 2000),
    SoftwareEngineer("rob", 20, "senior", 3000),
    Designer("angel", 20, 2000),
]


def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employee)
