from manim import *
import numpy as np

config.frame_size=(1080,1920)

class Solution(Scene):
    def construct(self):
        title0 = Tex("Linear Algebra").move_to(UP*2.2).scale(2)
        title1 = Tex("Part 1").move_to(UP).scale(2)
        title2 = Tex("Linear Equation").move_to(DOWN).scale(2)
        title3 = Tex("in 2 variables").move_to(DOWN*2.2).scale(2)
        title = VGroup(title0, title1, title2, title3).scale(1.8)
        self.play(Write(title))
        axes = Axes(
            x_range=[-10, 10, 1],  # step size determines num_decimal_places.
            y_range=[-10, 10, 1],
            x_length=12,
            y_length=12,
            axis_config={
                "numbers_to_include": np.arange(-10, 10, 1),
                "font_size": 24,
            },
            tips=False,
        )
        self.wait(0.5)
        # self.play(Create(axes))
        self.wait(2)