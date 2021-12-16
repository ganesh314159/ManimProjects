from manim import *
import numpy as np
config.background_color="WHITE"
# print(np.linspace(-3, 1, 1))
class TestIntro(Scene):
    def construct(self):
        with register_font("assets/fonts/"):
            trustlogo=ImageMobject("Pictures/Trust.png").move_to(UP*3+RIGHT*5.75).scale(0.5)
            kjssclogo=ImageMobject("Pictures/kjssclogo.png").move_to(UP*3.2+LEFT*4).scale(0.75)
            logo=ImageMobject("Pictures/mathletics.png").move_to(UP*1).scale(0.75)
            a = Text("Mathletics", color="#b7202e", font="Marcellus").move_to(DOWN*1).scale(2)
            b = Text("Presents You", color="#545454", font="Marcellus").move_to(DOWN*2)
            rec1=Rectangle(height=3, width=0.6, color="#b7202e", fill_color="#b7202e", fill_opacity=1).move_to(DOWN*2+RIGHT*6.7975)
            rec2=Rectangle(height=0.45, width=11, color="#b7202e", fill_color="#b7202e", fill_opacity=1).move_to(DOWN*3.758+RIGHT*2.2)
            rec3=Rectangle(height=0.45, width=4, color="#ed1c24", fill_color="#ed1c24", fill_opacity=1).move_to(DOWN*3.758+LEFT*5.3)
            self.play(
                FadeIn(kjssclogo),
                FadeIn(trustlogo),
                DrawBorderThenFill(rec1),
                DrawBorderThenFill(rec2),
                DrawBorderThenFill(rec3),
                run_time=1
            )
            self.play(FadeIn(logo), run_time=1)
            self.play(Write(a), run_time=0.5)
            self.play(Write(b), run_time=0.5)
            self.wait(1)
            self.play(
                Unwrite(a),
                Unwrite(b),
                Uncreate(rec1),
                Uncreate(rec2),
                Uncreate(rec3),
                FadeOut(kjssclogo),
                FadeOut(trustlogo),
                FadeOut(logo),
                run_time=1
            )   



class Test3D(ThreeDScene):
    def construct(self):
        axes1=ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            z_length=7,
            axis_config={
                "stroke_color": BLACK
            }
        ).rotate(PI/6, RIGHT)
        axes2=ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            z_length=7,
            axis_config={
                "stroke_color": BLACK
            }
        ).rotate(PI/6, DOWN).rotate(PI/6, RIGHT)
        self.play(Create(axes1))
        self.play(ReplacementTransform(axes1, axes2), run_time=5)
        self.wait(5)



class TestAnimate(Scene):
    def construct(self):
        circle1 = Circle().move_to(LEFT)  # create a circle
        square1 = Square().move_to(LEFT)
        circle2 = Circle().move_to(RIGHT)
        circle3 = Circle().move_to(RIGHT).set_fill(PINK, opacity=0.5)
        square2 = Square().move_to(RIGHT)  # create a square
        square3 = Square().move_to(RIGHT).rotate(PI/4)
        self.play(Create(square1), Create(square2))  # show the shapes on screen
        self.play(
            square1.animate.rotate(PI / 4),
            ReplacementTransform(square2, square3)
        )  # rotate the square
        self.play(
            ReplacementTransform(square1, circle1),
            ReplacementTransform(square3, circle2)
        )  # transform the square into a circle
        self.play(
            circle1.animate.set_fill(PINK, opacity=0.5),
            ReplacementTransform(circle2, circle3)
        )  # color the circle on screen
