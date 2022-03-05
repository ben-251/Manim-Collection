from manim import *
import random 
import typing
from functools import wraps
from math import sqrt

import numpy as np


class dots(Scene):
    def construct(self):
        a = 0
        b = 0 
        c = 0 
        d = 0
        letters = (a,b,c,d)
        def gen_random4():
            for i in letters:
                i = random.randint(1, 10)
            
            if a > b or b > c or c > d:
                gen_random4()
            return letters

        a,b,c,d = gen_random4()
        b = 13
        vertices = [a, b, c, d]
        edges = [(a, b), (b, c), (c, d), (d, a)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()

class label(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=rate_functions.ease_in_sine))

class Rate(Scene):
    def construct(self):
        line = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(GOLD)
        circle = Circle(radius=2,stroke_color=GOLD_B,stroke_width=2)

        dot = Dot().move_to(line.get_left())

        Square1 = Square(side_length=0.4,fill_color=GOLD,fill_opacity=0.8).next_to(line, RIGHT)
        Square2 = Square(side_length=0.4,fill_color=GOLD,fill_opacity=0.8).next_to(circle, RIGHT)
        self.play(
            FadeIn(VGroup(line, Square2,Square1,circle)),
        )

        self.play(
            MoveAlongPath(Square1, line, rate_func=rate_functions.my_sine),
            MoveAlongPath(Square2,circle, rate_func=rate_functions.my_sine),
            run_time=12
        )

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)