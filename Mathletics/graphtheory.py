from manim import *
from manim_presentation import Slide


class Dots(Slide):
    def construct(self):
        p1 = np.array([-3, -1, 0])
        p1b = p1 + [0, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [0, 2, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.play(Create(l1))
        self.play(Create(d1))
        self.play(Create(l2))
        self.play(Create(d2))
        self.play(Create(bezier))
        self.pause()
        shapes = VGroup(l1, d1, l2, d2, bezier)
        self.play(Uncreate(shapes))
        self.wait()