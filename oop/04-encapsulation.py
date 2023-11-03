class SoftwareEngineer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        # Private : hanya bisa di gungakan dalam class
        self.__salary = None
        # Protected : bisa di gunakan di luar class
        # tapi menandakan tidak boleh di akses dari luar class
        self._num_bugs_solve = 0

    def code(self):
        self._num_bugs_solve += 1

    # getter
    def get_salary(self):
        return self.__salary

    # setter
    def set_salary(self, base_value):
        self.__salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solve < 10:
            return base_value
        if self._num_bugs_solve < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("alice", 23)

for i in range(9):
    se.code()

se.set_salary(1000)

print(se.get_salary())
