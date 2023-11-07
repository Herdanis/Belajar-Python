class CountClass:
    def __init__(self, func) -> None:
        self.func = func
        self.num = 0

    def __call__(self, *args, **kwargs):
        self.num += 1
        print(f"print {self.num} times")
        return self.func(*args, **kwargs)


@CountClass
def sayhello():
    print("Hello")


sayhello()
sayhello()
sayhello()
