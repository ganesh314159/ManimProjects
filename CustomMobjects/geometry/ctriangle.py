from manim import * 
from numpy import *
import numpy as np

class CTriangle(VMobject):
    def __init__(self, a=None, b=None, c=None, color=BLUE, **kwargs):
        super().__init__(color=color, **kwargs)
        if a is None:
            a=60
        if b is None:
            b=60
        if c is None:
            c=60

        lside1=1
        lside2=np.sin(b)*lside1/sin(a)
        lside3=np.sin(c)*lside2/sin(b)
        height=np.sin(b)*lside3
        btoh=np.cos(b)*lside3
        side1=Line([0,0,0],[1,0,0])
        side2=Line().put_start_and_end_on([1,0,0], [btoh,height,0])
        side3=Line().put_start_and_end_on([btoh,height,0], [0,0,0])
        self.add(side1)
        self.add(side2)
        self.add(side3)


class TriangleScene(Scene):
    def construct(self):
        triangle=Triangle(a=30, b=90, c=60)
        self.wait()
        self.play(Create(triangle), run_time=5)
        self.wait(3)