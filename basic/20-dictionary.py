user = {
    "name": "qwe",
    "age": 0,
    "is_verified": True,
}

name = user.get("name")

print(name)

print(user.get("id", "01"))
