from manim import *
import numpy as np

config.frame_size=(1080,1080)
MATHLETIS_COLOR = "#7097e2"
SOMAIYA_COLOR = "#ed1c24"

class Riemann(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-10, 11, 1),
            y_range=(-1, 10, 1),
            x_length=12,
            y_length=7,
            color=MATHLETIS_COLOR
        )
        graph = FunctionGraph(lambda x: x**2, x_range=[-10, 10], color=SOMAIYA_COLOR)
        graph.add(number_plane)
        self.add(number_plane, graph)
        
        
        
        
        