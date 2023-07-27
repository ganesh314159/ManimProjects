from manim import *
import numpy as np
config.background_color=BLACK
config.frame_size=(1080,1920)
class Blaze(Scene):
    def construct(self):
        title0 = Text("ProjectBlaze", color=BLACK, fill_color="#c4d6f9").move_to(DOWN*6).scale(2)
        cir0 = Circle(radius=0.4, fill_color="#c4d6f9", fill_opacity=1).set_color("#c4d6f9").move_to(RIGHT*1.74+UP*2.2)
        polar=PolarPlane()
        n=1
        # cir1=polar.plot(lambda x : 2.3+0.13*np.sin(12*x), x_range=[0, 2*PI], color=BLACK)
        cir1=ParametricFunction(
            lambda t: np.array([
            2.3*np.cos(t)+0.13*np.cos(t)*np.sin(12*t),
            2.3*np.sin(t)+0.13*np.sin(t)*np.sin(12*t),
            0
            ]), t_range=np.array([0, 2*PI, 0.01]), fill_color="#c4d6f9", fill_opacity=1
        ).set_color("#c4d6f9")
        cir2=Circle(radius= 3.5, fill_color="#3d52b3", fill_opacity=1).set_color("#3d52b3")
        top=ArcPolygonFromArcs(
            ArcBetweenPoints([-2, 0.5, 0], [-2, 2, 0], radius=0),
            ArcBetweenPoints([-2, 2, 0], [])
        )
        
        
        
        self.play(Write(title0), DrawBorderThenFill(cir2))
        self.play(SpinInFromNothing(cir1, angle=PI), run_time=2)
        self.play(DrawBorderThenFill(cir0))