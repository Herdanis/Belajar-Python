class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
point1.draw()

point2 = Point()
point2.x = 10
point2.y = 20
point2.draw()

print(point2.x)
