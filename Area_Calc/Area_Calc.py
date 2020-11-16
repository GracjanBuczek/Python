import math
from enum import IntEnum


 
Menu = IntEnum("Menu", ("Rectangle, Square, Triangle, Circle, Trapeze, Exit"))

 
def rectangle(a, b):
    return a * b
 
 
def square(a):
    return a * a
 
 
def triangle(a, h):
    return (a * h) / 2
 
 
def circle(r):
    return math.pi * r ** 2
 
 
def trapeze(a, b, h):
    return ((a + b) * h) / 2
 
 

 
 
def start():
 back = True
 while(back):
    print(
        """
This simple program allows to calculate areas of mathematical figures.
Choose number:
1. Rectangle
2. Square
3. Triangle
4. Circle
5. Trapeze
0. Exit
"""
    )
 
    wyb = int(input())
 
    if (wyb == Menu.Rectangle):
        print("Figure: Rectangle. Enter lengths of sides.")
        a = int(input("A: "))
        b = int(input("B: "))
        if a <= 0 or b <= 0:
            print("Areas or sides lengths cannot be negative. Try it again.")
            #back = False
        else:
            print("Area of this figure is", rectangle(a, b))
    elif (wyb == Menu.Square):
        print("Figure: Square. Enter length of side.")
        a = int(input("A:"))
        if a <= 0:
            print("Areas or sides lengths cannot be negative. Try it again.")
            #back = False
        else:
            print("Area of this figure is", square(a))
    elif (wyb == Menu.Triangle):
        print("Figure: Triangle. Enter length of side and height.")
        a = int(input("A:"))
        h = int(input("H:"))
        if a <= 0 or h <= 0:
            print("Areas, sides lengths or height cannot be negative. Try it again.")
            #back = False
        else:
            print("Area of this figure is", triangle(a, h))
    elif (wyb == Menu.Circle):
        print("Figure: Circle. Enter radius.")
        r = int(input("r:"))
        if r <= 0:
            print("Areas or radius cannot be negative. Try it again.")
            #back = False
        else:
            print("Area of this figure is", circle(r))
    elif (wyb == Menu.Trapeze):
        print("Figure: Trapeze. Enter length of sides and heigth.")
        a = int(input("A: "))
        b = int(input("B: "))
        h = int(input("h: "))
        if a <= 0 or h <= 0:
            print("Areas, sides lengths or height cannot be negative. Try it again.")
        else:
            print("Area of this figure is", trapeze(a, b, h))
    elif (wyb >= 7):
        print(
            """
    This operation is not avaliable in your version of program.
    Update your program to the newest version
    to calculate area of choosen figure.
    """
        )
    elif (wyb == Menu.Exit):
       back = False
       print("KONIEC")

 
start()
