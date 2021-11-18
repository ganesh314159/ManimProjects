from manim import *
import numpy as np

class Heron(Scene):
    def construct(self):
        polygon01=Polygon(
            [-3,-3,0],
            [3,-3,0],
            [-1,2,0]
        ).scale(0.75)
        self.play(Create(polygon01))
        circle01=Circle().surround(polygon01, buffer_factor=0.5)
        self.play(Create(circle01))
        self.wait(3)