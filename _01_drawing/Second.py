import turtle


jeremy = turtle.Turtle()

jeremy.shape('turtle')

jeremy.color('green')

for i in range(5):
    jeremy.right(90)
    
jeremy.left(90)

jeremy.penup()
jeremy.goto (200,200)



if jeremy.xcor() < 100:
    jeremy.forward(100)
    
for i in range(4):
    jeremy.forward(100)
    jeremy.left(90)

    




turtle.done()