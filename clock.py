import turtle
import time

wn = turtle.Screen()
wn.bgcolor('#000')
wn.title('Clock')
wn.setup(width=600, height=600)
wn.tracer(0)


# classes
class ClockOutline(turtle.Turtle):
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


class ClockHands(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.pensize(5)
        self.penup()
        self.hideturtle()

    def draw_hour_hand(self, h):
        self.penup()
        self.setposition(0, 0)
        self.color('#fff')
        self.setheading(90)
        angle = (h / 12) * 360
        self.rt(angle)
        self.pendown()
        self.fd(100)

    def draw_minute_hand(self, m):
        self.penup()
        self.setposition(0, 0)
        self.color('#006666')
        self.setheading(90)
        angle = (m / 60) * 360
        self.rt(angle)
        self.pendown()
        self.fd(175)

    def draw_seconds_hand(self, s):
        self.penup()
        self.setposition(0, 0)
        self.color('#006633')
        self.setheading(90)
        angle = (s / 60) * 360
        self.rt(angle)
        self.pendown()
        self.fd(125)



class Time:
    def __init__(self):
        self.hour = time.localtime().tm_hour
        self.minute = time.localtime().tm_min
        self.second = time.localtime().tm_sec

    def print_time(self):
        print(self.hour)


# class instances
clock_outline = ClockOutline()
clock_hands = ClockHands()

# draw clock outline
clock_outline.draw_clock()
clock_outline.draw_hours()

# main loop
while True:
    # class instances
    currentTime = Time()
    # draw clock hands
    clock_hands.draw_hour_hand(currentTime.hour)
    clock_hands.draw_minute_hand(currentTime.minute)
    clock_hands.draw_seconds_hand(currentTime.second)
    wn.update()
    time.sleep(1)
    clock_hands.clear()
