from manim import *
import fourier
from fourier import *

class Test(Scene):
    def construct(self):
        tex=Tex("\\tau")   # <----- it needs $$
        self.play(Write(tex), run_time=5)
        self.wait(5)
        set()

class ValueTrackerExample(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        label = Dot(radius=3).add_updater(lambda x : x.set_x(tracker.get_value()))
        self.add(label)
        self.wait(2)
        self.add(tracker)
        self.wait(2)
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(2)

class FourierTest(AbstractFourierOfTexSymbol):
    def __init__(self):
        super().__init__()
        self.start_drawn=True
        self.tex_class=Tex
        self.tex="M"
        # self.tex_class.set(font="Marcellus")
        self.tex_config={
            "fill_opacity": 0,
            "stroke_width": 1,
            "stroke_color": WHITE,
            # "font": "Marcellus"
        }
        self.drawn_path_color=RED
        self.interpolate_config=[0,1]
        self.n_vectors=100
        self.big_radius=1
        self.drawn_path_stroke_width=1
        self.center_point=ORIGIN
        self.slow_factor=0.01
        self.n_cycles=2
        self.run_time=60
        self.circle_config={
            "stroke_width": 1,
        }
        self.vector_config={
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.25,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 2,
            "stroke_width": 1
        }
        self.base_frequency=1
        self.parametric_function_step_size=0.001
