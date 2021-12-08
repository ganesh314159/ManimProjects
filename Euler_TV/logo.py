from manim import *
import numpy as np
config.frame_size=(720,720)

class Logo(Scene):
    def construct(self):
        logos=Text("e").scale(3)
        logot=Text("Euler TV").scale(0.5).next_to(logos, DOWN, buff=0.2)
        logo=VGroup(logos, logot).scale(3.8).set_opacity(1).move_to(0.25*UP)
        self.add(logo)