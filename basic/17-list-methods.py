number = [1, 2, 3, 4, 5, 6]
number.append(7)

print(number)

number.insert(2, 4)
print(number)

number.remove(4)
print(number)

number.pop()
print(number)

print(number.index(3))
print(30 in number)

number.reverse()
print(number)

number2 = number.copy()

number.clear()
print(number)
