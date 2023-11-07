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

    # instance method
    def code(self):
        print(f"{self.name} writing code")

    def code_lang(self, lang):
        print(f"{self.name} write code in {lang}")

    # dunder method
    def __str__(self):
        information = f"{self.name} - {self.age}"
        return information

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

    # decorator
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 2000
        if age < 30:
            return 3000
        return 4000


# instance
se1 = SoftwareEngineer("alice", 10, "junior", 100)
se2 = SoftwareEngineer("bob", 12, "senior", 200)
se1.code()
se1.code_lang("python")

print(f"{se1}")

print(se1 == se2)

print(se1.entry_salary(200))

print(SoftwareEngineer.entry_salary(3000))
