import turtle

wn = turtle.Screen()
wn.bgcolor('#000')
wn.title('Clock')
wn.setup(width=600, height=600)


# classes
class Clock(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('#003366')
        self.pensize(5)

    # draw outline for clock face
    def draw_clock(self):
        self.penup()
        self.setposition(0, 210)
        self.pendown()
        self.setheading(180)
        self.circle(210)

    # draw indent lines for hours
    def draw_hours(self):
        self.penup()
        self.setposition(0, 0)
        self.setheading(90)

        for _ in range(12):
            self.fd(190)
            self.pendown()
            self.fd(20)
            self.penup()
            self.setposition(0, 0)
            self.rt(30)


# class instances

# draw clock
clock = Clock()
clock.draw_clock()
clock.draw_hours()
# main loop
wn.mainloop()