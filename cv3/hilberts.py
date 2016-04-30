from Turtle import Turtle

turtl = Turtle('c_hilbert')


def step(angle = 90, dist = 10, level = 5):
    if level == 0:
        return

    turtl.right(angle)
    step(-angle, dist, level - 1)
    turtl.forward(dist)
    turtl.left(angle)
    step(angle, dist, level - 1)
    turtl.forward(dist)
    step(angle, dist, level - 1)
    turtl.left(angle)
    turtl.forward(dist)
    step(-angle, dist, level - 1)
    turtl.right(angle)

step(90,15, 5)

turtl.save()
