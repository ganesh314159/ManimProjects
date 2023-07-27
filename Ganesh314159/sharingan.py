from manim import *
import numpy as np
config.background_color = WHITE


class MadaraMS(Scene):
    def construct(self):
        ms0=ImageMobject("Pictures/MadaraMS.png").scale(4).move_to(ORIGIN)
        self.wait(1)
        p0=np.array([0.6,1.44,0])
        p0b=p0 + [0.6,0.1,0]
        d0=Dot(point=p0).scale(0.5)
        l0=Line(p0, p0b)
        p1=np.array([1.95,-0.16,0])
        p1b=p1 + [0.1,1,0]
        d1=Dot(point=p1).scale(0.5)
        l1=Line(p1, p1b)
        b0=CubicBezier(p0,p0b+0.15*UP, p1b+0.3*UP+0.09*LEFT, p1, stroke_width=0.5)
        p2=np.array([0.42,2.52,0])
        p2b=p2+[]
        d2=Dot(point=p2).scale(0.2)
        l
        p3=np.array([2.23,-0.44,0])
        d3=Dot(point=p3).scale(0.2)
        self.add(ms0, d3, b0)
        self.wait(5)





