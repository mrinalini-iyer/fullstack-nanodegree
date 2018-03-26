import turtle

def draw_square(some_turtle):

    index = 0
    while index < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        index+=1
        
def draw_shapes():

    window =  turtle.Screen()
    window.bgcolor("red")
    ziggy = turtle.Turtle()

    # ziggy attributes
    ziggy.shape("turtle")
    ziggy.color("yellow")
    ziggy.speed(2)

    # draw square
    #36 times since 10 * 36 = 360 
    for i in range(1,37):
        draw_square(ziggy)
        ziggy.right(10)

   window.exitonclick()


draw_shapes()
