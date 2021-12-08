from manim import *
import numpy as np
config.frame_size=(720,720)
class Intro(VGroup):
    def __init__(self, **kwargs):
        # super().__init__(color=color, **kwargs)
        text00 = Text("e")
        text00.scale(12)
        text00.move_to(UP*1.2)
        text01 = Text("e")
        text01.scale(3)
        text01.move_to(UP*3.25 + RIGHT*6.2)
        text10 = Text("Euler TV")
        text10.scale(2)
        text10.move_to(DOWN*1.8)
        text11 = Text("Euler TV")
        text11.scale(0.5)
        text11.move_to(DOWN*1.3 + UP*3.8 + RIGHT*6.2)
        # self.add(grid, text00, text10)
        # self.play(Write(text00), run_time=3)
        # self.play(Write(text10), run_time=3)
        # self.wait(1)
        # self.play(ReplacementTransform(text00, text01), ReplacementTransform(text10, text11))
        # self.wait(1)
        self.add(text00)
        self.add(text10)

class MathSeries1(Scene):
    def construct(self):
        
        title=Text("New series starting...")
        self.play(Write(title))
        self.wait()