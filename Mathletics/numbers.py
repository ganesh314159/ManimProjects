
# %%manim -qm -v WARNING Mathletics
from manim import *
from manim.mobject import number_line
import numpy as np
# config.media_width="100%"
config.background_color="WHITE"
class Numbers(Scene):
    def construct(self):
        with register_font("assets/fonts/"):
            # Intro starts
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
            # Intro ends
            title1=MarkupText("Numbers", gradient=(RED, BLUE), font="Marcellus").scale(3)
            title2=MarkupText("Numbers", gradient=(RED, BLUE), font="Marcellus").scale(1)
            title2.move_to(UP*3.5)
            line00=Line([-6, 3, 0], [ 6, 3, 0])
            line01=Line([-6,-2, 0], [ 6,-2, 0])
            # logos

            text00=Text("The numbers, we use to count.", color=BLACK, font="Fira Sans").move_to(2.6*DOWN).scale(0.85)
            text01=Text("There are different types of numbers.", color=BLACK, font="Fira Sans").move_to(3.4*DOWN).scale(0.85)
            number=Text("1 2 3 4 5 6 7 8 9 ...", color=BLACK, font="Fira Sans").scale(1).move_to(0.5*UP)
            text02=Text("But, Do you know numbers too have families?", color=BLACK, font="Fira Sans")

            self.play(Write(title1), run_time=1)
            self.wait(0.5)
            self.play(ReplacementTransform(title1, title2))
            # self.play(Create(line00))
            # self.play(Create(line01, run_time=1))
            self.play(Write(text00, run_time=1))
            self.wait(0.5)
            self.play(Write(number), run_time=1)
            self.wait(0.5)
            self.play(Write(text01), run_time=1)
            self.wait(1)
            self.play(Unwrite(text00), Unwrite(text01), Unwrite(number))

            
            naturals=MathTex(r"\mathbb{N}", color=BLACK).move_to(2.5*UP+LEFT*5).scale(1.5)
            naturaln=MathTex(r"= 1,2,3,4,5,...", color=BLACK).scale(1.5)
            wholes=MathTex(r"\mathbb{W}", color=BLACK).move_to(2.5*UP+LEFT*3).scale(1.5)
            wholen=MathTex(r"= 0",",1,2,3,4,...", color=BLACK)
            integers=MathTex(r"\mathbb{Z}", color=BLACK).move_to(2.5*UP+LEFT*1).scale(1.5)
            integern=MathTex(r"= ...,-3,-2,-1,0,1,2,3,...", color=BLACK)
            rationals=MathTex(r"\mathbb{Q}", color=BLACK).move_to(2.5*UP+RIGHT*1).scale(1.5)
            rationaln=MathTex(r"= \frac{p}{q},","\; Where","\; p,q \in \mathbb{Z}", color=BLACK)
            reals=MathTex(r"\mathbb{R}", color=BLACK).move_to(2.5*UP+RIGHT*3).scale(1.5)
            realn=MathTex(r"= ...,-2,-1,0,1,","\sqrt{2}",",","\phi",",","\sqrt{3}",",2,","\pi",",...", color=BLACK)
            imaginarys=MathTex(r"\mathbb{C}", color=BLACK).move_to(2.5*UP+RIGHT*5).scale(1.5)
            imaginaryn=MathTex(r"= ","a","+","i","b",",\; Where\; a,b \in \mathbb{R}, i=\sqrt{-1}", color=BLACK)
            
            naturalsb=MathTex(r"\mathbb{N}", color=BLACK).scale(4)
            self.play(Write(naturalsb), run_time=0.5)
            text10=Text("Natural numbers", color=BLACK, font="Fira Sans").move_to(1.5*DOWN)
            self.play(Write(text10), run_time=0.5)
            self.wait(1)
            naturalss=MathTex(r"\mathbb{N}", color=BLACK).move_to(4*LEFT+1.5*UP).scale(1.5)
            self.play(ReplacementTransform(naturalsb, naturalss), ReplacementTransform(text10, naturaln.next_to(naturalss)))
            self.wait(0.5)
            numbarn=NumberLine(
                x_range=[1, 5, 1],
                length=4,
                color=BLACK,
                include_numbers=True,
                label_direction=UP,
            ).move_to(DOWN*3)
            numbarn.numbers.set_color(BLACK)
            self.play(ReplacementTransform(naturaln.copy(), numbarn))
            self.wait(1)
            self.play(ReplacementTransform(naturalss, naturals), ReplacementTransform(naturaln, naturals))
            wholesb=MathTex(r"\mathbb{W}", color=BLACK).scale(4)
            text11=Text("Whole Numbers", color=BLACK, font="Fira Sans").move_to(1.5*DOWN)
            self.play(Write(wholesb), run_time=0.5) 
            self.play(Write(text11), run_time=0.5)
            self.wait(1)
            wholess=MathTex(r"\mathbb{W}", color=BLACK).move_to(4*LEFT+1.5*UP).scale(1.5)
            self.play(ReplacementTransform(wholesb, wholess), ReplacementTransform(text11, wholen.next_to(wholess)))
            self.wait(0.5)
            numbarw=NumberLine(
                x_range=[0, 4, 1],
                length=5,
                color=BLACK,
                include_numbers=True,
                label_direction=UP,
            ).move_to(DOWN*3)
            numbarw.numbers.set_color(BLACK)
            self.play(ReplacementTransform(wholen.copy(), numbarw),ReplacementTransform(numbarn, numbarw))
            self.wait(1)
            self.play(ReplacementTransform(wholess, wholes), ReplacementTransform(wholen, wholes))
            integersb=MathTex(r"\mathbb{Z}", color=BLACK).scale(4)
            text12=Text("Intergers", color=BLACK, font="Fira Sans").move_to(1.5*DOWN)
            self.play(Write(integersb), run_time=0.5)
            self.play(Write(text12), run_time=0.5)
            self.wait(1)
            integerss=MathTex(r"\mathbb{Z}", color=BLACK).scale(1.5).move_to(4*LEFT+1.5*UP)
            self.play(ReplacementTransform(integersb, integerss), ReplacementTransform(text12, integern.next_to(integerss)))
            self.wait(0.5)
            numbari=NumberLine(
                x_range=[-3, 3, 1],
                length=10,
                color=BLACK,
                include_numbers=True,
                label_direction=UP,
            ).move_to(DOWN*3)
            numbari.numbers.set_color(BLACK)
            self.play(ReplacementTransform(integern.copy(), numbari),ReplacementTransform(numbarw, numbari))
            self.wait(1)
            self.play(ReplacementTransform(integerss, integers), ReplacementTransform(integern, integers))
            rationalsb=MathTex(r"\mathbb{Q}", color=BLACK).scale(4)
            text13=Text("Rational Numbers", color=BLACK, font="Fira Sans").move_to(1.5*DOWN)
            self.play(Write(rationalsb), run_time=0.5)
            self.play(Write(text13), run_time=0.5)
            self.wait(1)
            rationalss=MathTex(r"\mathbb{Q}", color=BLACK).scale(1.5).move_to(4*LEFT+1.5*UP)
            self.play(ReplacementTransform(rationalsb, rationalss), ReplacementTransform(text13, rationaln.next_to(rationalss)))
            self.wait(0.5)
            numbarrn=NumberLine(
                x_range=[-3, 3, 1],
                length=10,
                color=BLACK,
                include_numbers=True,
                label_direction=UP,
            ).move_to(DOWN*3)
            numbarrn.numbers.set_color(BLACK)
            num1=MathTex(r"1.5 ","="," \\frac{3}{2}", color=BLACK).next_to(rationaln, DOWN*1.5)
            dot1=Dot(point=numbarrn.n2p(1.5)).set_color(BLACK)
            dot1_label=MathTex(r"\frac{3}{2}", color=BLACK).next_to(dot1, UP*1)
            
            self.play(ReplacementTransform(rationaln.copy(), numbarrn),ReplacementTransform(numbari, numbarrn))
            self.wait(0.5)
            self.play(Write(num1))
            self.wait(0.5)
            self.play(ReplacementTransform(num1.copy()[0], dot1), ReplacementTransform(num1.copy()[-1], dot1_label))
            # text14=Text("        We will talk more about\nrational numbers in future videos").scale(0.75).next_to(num1, DOWN*1)
            # self.play(Write(text14))
            self.wait(0.5)
            self.play(
                ReplacementTransform(rationalss, rationals), 
                ReplacementTransform(rationaln, rationals),
                Unwrite(num1),
                Unwrite(dot1_label),
                Uncreate(dot1),
                )
            realsb=MathTex(r"\mathbb{R}", color=BLACK).scale(4)
            text15=Text("Real numbers", color=BLACK, font="Fira Sans").move_to(1.5*DOWN)
            self.play(Write(realsb), run_time=0.5)
            self.play(Write(text15), run_time=0.5)
            self.wait(1)
            realss=MathTex(r"\mathbb{R}", color=BLACK).scale(1.5).move_to(4*LEFT+1.5*UP)
            self.play(ReplacementTransform(realsb, realss), ReplacementTransform(text15, realn.next_to(realss)))
            self.wait(0.5)
            numbarrl=NumberLine(
                x_range=[-1, 4, 1],
                length=10,
                color=BLACK,
                include_numbers=True,
                label_direction=UP,
            ).move_to(DOWN*3)
            numbarrl.numbers.set_color(BLACK)
            dots2=Dot(point=numbarrl.n2p(np.sqrt(2))).set_color(BLACK)
            dots2label=MathTex(r"\sqrt{2}", color=BLACK).next_to(dots2, UP*1).scale(0.5)
            dots3=Dot(point=numbarrl.n2p(np.sqrt(3))).set_color(BLACK)
            dots3label=MathTex(r"\sqrt{3}", color=BLACK).next_to(dots3, UP*1).scale(0.5)
            dotgr=Dot(point=numbarrl.n2p((1+np.sqrt(5))/2)).set_color(BLACK)
            dotgrlabel=MathTex(r"\phi", color=BLACK).next_to(dotgr, UP*1).scale(0.5)
            dotpi=Dot(point=numbarrl.n2p(PI)).set_color(BLACK)
            dotpilabel=MathTex(r"\pi", color=BLACK).next_to(dotpi, UP*1).scale(0.75)
            self.play(
                ReplacementTransform(realn.copy(), numbarrl),
                ReplacementTransform(numbarrn, numbarrl),
                ReplacementTransform(realn.copy()[1], dots2label),
                ReplacementTransform(realn.copy()[5], dots3label),
                ReplacementTransform(realn.copy()[3], dotgrlabel),
                ReplacementTransform(realn.copy()[-2], dotpilabel),
                Create(dots2),
                Create(dots3),
                Create(dotgr),
                Create(dotpi),
                )
            self.wait(0.5)
            self.play(
                ReplacementTransform(realss, reals),
                ReplacementTransform(realn, reals),
            )
        
            imaginarysb=MathTex(r"\mathbb{C}", color=BLACK).scale(4)
            text16=Text("Complex numbers", color=BLACK, font="Fira Sans").move_to(1.5*DOWN)
            self.play(Write(imaginarysb), run_time=0.5)
            self.play(Write(text16), run_time=0.5)
            self.wait(1)
            imaginaryss=MathTex(r"\mathbb{C}", color=BLACK).move_to(1.5*UP+LEFT*4).scale(1.5)
            self.play(ReplacementTransform(imaginarysb, imaginaryss), ReplacementTransform(text16, imaginaryn.next_to(imaginaryss)))
            self.wait(0.5)

            axesc=(
                ComplexPlane(
                    x_range=(0, 3),
                    y_range=(0, 3),
                    x_length=4,
                    y_length=4,
                    axis_config={"include_numbers": True},
                )
                .add_coordinates(color=BLACK)
                .move_to(1.5 * DOWN)
            ).set_color(BLACK)
            # axesc.numbers.set_color(BLACK)
            cdot=Dot(axesc.n2p(1+2j), color=RED)
            cdot_label=MathTex("a","+","i","b", color=BLACK).next_to(cdot, UR, 0.1).scale(0.8)
            group1=VGroup(dots2, dotgr, dots3, dotpi)
            group2=VGroup(dots2label, dotgrlabel, dots3label, dotpilabel)
            self.play(
                ReplacementTransform(imaginaryss.copy(), axesc),
                ReplacementTransform(numbarrl, axesc),
                ReplacementTransform(imaginaryn.copy(), cdot),
                ReplacementTransform(imaginaryn.copy(), cdot_label),
                Uncreate(group1),
                Uncreate(group2),
            )
            self.wait(0.5)
            self.play(ReplacementTransform(imaginaryss.copy(), imaginarys))
            self.wait(1)
            groupt=VGroup(title2, naturals, wholes, integers, reals, imaginarys, imaginaryn, cdot_label, imaginaryss, rationals)
            
            # groupp=VGroup(kjssclogo, mathleticslogo)
            self.play(
                Unwrite(groupt),
                Uncreate(axesc),
                Uncreate(cdot),
            )


class Irrational(Scene):
    def construct(self):
        with register_font("assets/fonts/"):
            # Intro starts
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
            # Intro ends
            title=MarkupText("Irrational numbers", gradient=(RED, BLUE), font="Marcellus").scale(3)


















