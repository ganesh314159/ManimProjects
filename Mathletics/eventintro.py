from manim import *
import numpy as np

config.background_color = BLACK


class Intro(Scene):
    def construct(self):
        title=Text("Mathletics", color="#b7202e", font="Marcellus")
        rec=Rectangle()
        self.play(Write(title), DrawBorderThenFill(rec), run_time=5)
        self.wait(5)