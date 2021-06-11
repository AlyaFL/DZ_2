import turtle as tk

def l_system(n, axiom, rules):
    start = axiom
    if n == 0:
        return axiom
    end = ""
    for i in range(n):
        end = "".join(rules[i] if i in rules else i for i in start)
        start = end
    return end 

def draw_curve(t, string, ang, step):
    for i in string:
        if i == "F":
            t.forward(step)
        elif i == "+":
            t.right(ang)
        elif i == "-":
            t.left(ang)

def main(t, iters, axiom, rules, ang, x = 0, y = 0):
    t.speed(0)
    t.pensize(3)
    t.color("green")
    t.penup()
    t.goto(x, y)
    t.pendown()
    st = l_system(iters, axiom, rules)
    step = 80 // iters 
    draw_curve(t, st, ang, step)
    t.hideturtle()

axiom = "L"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
ite = 5
angle = 90  
x = -70 * (ite - 1)
y = 70 * (ite - 1)

#axiom = "FX"
#rules = {"X":"X+YF+", "Y":"-FX-Y"}
#ite = 9 
#angle = 90
#x = 0
#y = 0

t = tk.Turtle()
main(t, ite, axiom, rules, angle, x, y)
tk.exitonclick()