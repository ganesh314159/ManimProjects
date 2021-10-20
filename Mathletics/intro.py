from manim import *
from manimpango import *
import numpy as np

class Introduction(Scene):
    def construct(self):
        title=MarkupText("Mathletics", gradient=(BLUE, RED))
        self.wait(1)
        self.play(Write(title), run_time=3)
        self.wait(3)