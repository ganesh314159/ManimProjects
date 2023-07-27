from manim import *
import numpy as np

class Logo(Scene):
    def construct(self):
        tri0=Triangle(stroke_color="#FFD700").move_to(UP*0.25)
        tri1=Triangle(stroke_color="#FFD700").rotate(angle=PI).move_to(DOWN*0.25)
        tri=VGroup(tri0, tri1)
        cir0=Circle(stroke_color="#FFD700").surround(tri).scale(0.65)
        logo=VGroup(tri, cir0)
        self.add(logo)