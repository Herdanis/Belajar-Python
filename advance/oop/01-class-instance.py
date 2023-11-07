# class
class SoftwareEngineer:
    # class attributes
    alias = "keyboard wizard"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance
se1 = SoftwareEngineer("max", 12, "junior", 100)
print(f"{se1.name} - {se1.alias}")
