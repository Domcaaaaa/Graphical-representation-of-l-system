import turtle

def iterate(axiom, num=0, rule='F'):
    for _ in range(num):
        axiom = ''.join(rule if c == 'F' else c for c in axiom)
    return axiom

def draw(axiom, angle=90, length=10):
    stack = []                     
    screen = turtle.Screen()
    zelva = turtle.Turtle()

    zelva.hideturtle()
    zelva.speed(0)
    zelva.left(90)

    actions = {
        'F': lambda: zelva.forward(length),
        'f': lambda: (zelva.penup(), zelva.forward(length), zelva.pendown()),
        '+': lambda: zelva.left(angle),
        '-': lambda: zelva.right(angle),
        '[': lambda: stack.append((zelva.heading(), zelva.pos())),
        ']': lambda: (zelva.penup(), zelva.goto(stack[-1][1]), zelva.setheading(stack[-1][0]), zelva.pendown(), stack.pop())
    }

    for c in axiom:
        action = actions.get(c)
        if action:
            action()

    screen.onkey(screen.bye, "q")
    screen.listen()
    turtle.mainloop() 

# Fractal patterns based on the table
fractals = {
    "Edge Rewrite": {"axiom": "F", "rule": "F+F--F+F", "angle": 60},
    "Quadratic Koch": {"axiom": "F-F-F-F", "rule": "F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F", "angle": 90},
    "Koch Curve a": {"axiom": "F-F-F-F", "rule": "FF-F-F-F-F-F+F", "angle": 90},
    "Branching (a)": {"axiom": "F", "rule": "F[+F]F[-F]F", "angle": 25},
    "Sympodial Tree": {"axiom": "A(1,10)", "rule": "F(l,w)[&(c)B(l*b,w*h)]/(m)A(l*b,w*h)", "angle": 28},
    "Monopodial Tree": {"axiom": "A(1,10)", "rule": "Custom rule depending on values", "angle": 45}, 
    "Sunflower": {"axiom": "A(0)", "rule": "Rule 1 and conditionals for seed arrangement", "angle": 137.5}
}

# Display available fractal patterns
print("Available fractals:")
for i, key in enumerate(fractals.keys(), 1):
    print(f"{i}. {key}")
print(f"{len(fractals) + 1}. Custom Fractal")

# Take user choice
choice = int(input("Choose a fractal pattern by number: ")) - 1

# If the user selects a predefined fractal
if choice < len(fractals):
    selected_fractal = list(fractals.keys())[choice]
    pattern = fractals[selected_fractal]

    # Take number of iterations from user
    iterations = int(input("Enter the number of iterations: "))
    length = int(input("Enter the line length (default 10): ") or 10)

    # Generate the final axiom and draw it
    final_axiom = iterate(pattern["axiom"], iterations, pattern["rule"])
    draw(final_axiom, pattern["angle"], length)


else:
    # Take user-defined axiom, rule, and other parameters
    user_axiom = input("Enter your custom axiom: ")
    user_rule = input("Enter your custom rule (F -> ...): ")
    angle = float(input("Enter the angle (default 90): ") or 90)
    iterations = int(input("Enter the number of iterations: "))
    length = int(input("Enter the line length (default 10): ") or 10)

    # Generate the final axiom and draw it
    final_axiom = iterate(user_axiom, iterations, user_rule)
    draw(final_axiom, angle, length)
