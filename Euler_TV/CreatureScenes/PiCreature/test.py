from manim import *

class Creature(Scene):
    def construct(self):
        svg=SVGMobject("PiCreature.svg")
        self.play(Create(svg), run_time=5)
        self.wait(5)