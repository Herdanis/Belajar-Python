class User:
    total = 0
    
    def __init__(self, name, role):
        self.name = name
        # private variable
        self.__role = role
        
        User.total += 1
        
    def info(self):
        return f"{self.name} - name - {self.__role}"
    
    def update_user(self, new_role):
        if self.__role != "user":
            self.__role = new_role

qwe = User("poi", "user")
print(qwe.name)
print(qwe.info())
qwe.update_user("admin")
# qwe.__role = "admin"
print(User.total)
print(qwe.info())

asd = User("lkj", "admin")
print(asd.info())
asd.update_user("super_user")
print(User.total)
print(asd.info())