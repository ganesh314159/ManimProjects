from manim import *
import numpy as np
config.background_color = WHITE
class MadaraMS(Scene):
    def construct(self):
        ms0=SVGMobject("Pictures/3TomoeS.svg")
        self.wait(1)
        self.play(Create(ms0), run_time=10)
        self.wait(5)





