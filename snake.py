from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setposition(position)
            self.segments.append(snake)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_grow(self):
        tail = Turtle("square")
        tail.penup()
        tail.color("white")
        tail_x = self.segments[-1].xcor()
        tail_y = self.segments[-1].ycor()
        self.segments.append(tail)
        tail.setposition(x=tail_x, y=tail_y)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
