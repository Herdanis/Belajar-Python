def decorator_one(func):
    def wrapper_one(*args, **kwargs):
        print("Decorator one is being called")
        return func(*args, **kwargs)

    return wrapper_one


def decorator_two(func):
    def wrapper_two(*args, **kwargs):
        print("Decorator two is being applied")
        return func(*args, **kwargs)

    return wrapper_two


@decorator_one
@decorator_two
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
