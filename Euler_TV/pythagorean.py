from manim import *
import numpy as np
import introduction #import Intro

class Pythagorean(Scene):
    def construct(self):
        introduction.Intro()
        titleb=Text("Pythagorean Theorem").scale(1.6)
        titles=Text("Pythagorean Theorem").scale(1).move_to(UP*3.5)
        line00=Line([-6, 3, 0], [ 6, 3, 0])
        self.play(Write(titleb))
        self.wait(1)
        self.play(ReplacementTransform(titleb, titles))
        self.play(Create(line00))
        self.wait(1)

        triangle00=Triangle()
        self.play(Create(triangle00))
        self.wait(3)
