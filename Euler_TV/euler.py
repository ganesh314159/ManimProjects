from manim import *
import numpy as np
# from introduction import *
# from ..CustomMobjects.geometry import *
config.frame_size=(720,720)


class Euler(Scene):
    def construct(self):
        logos=Text("e").scale(3)
        logot=Text("Euler TV").scale(0.5).next_to(logos, DOWN, buff=0.2)
        logo=VGroup(logos, logot).scale(0.75).move_to(UP*3.3+RIGHT*3.3)#.set_opacity(0.5)
        # triangle=CTriangle()
        title=Tex("Leonhard Euler").move_to(UP*3.3).scale(1.2)
        picture=ImageMobject("Pictures/leonard_euler").move_to(UP*1.15).scale(0.35)
        bd=Tex("Birth : 15 April 1707 , Death : 18 September 1783").scale(0.5).next_to(picture, DOWN, buff=0.2)
        # death=Tex("")
        paragraph=Tex('''Leonard euler was a Swiss mathematician,\n
physicist, astronomer, geographer,\n
logician and engineer.''').scale(0.75).next_to(bd, DOWN, buff=0.2)
        swipe=Tex("Swipe to see more\n","$\\rightarrow$").move_to(DOWN*3.3)


        self.add(
            logo,
            title,
            picture,
            bd, 
            paragraph,
            swipe,
            # triangle
        )

class EulerDisc1(Scene):
    def construct(self):
        title=Tex("Mathematical Notations").move_to(UP*3.3).scale(1.2)
        logos=Text("e").scale(3)
        logot=Text("Euler TV").scale(0.5).next_to(logos, DOWN, buff=0.2)
        logo=VGroup(logos, logot).scale(4).set_opacity(0.05).move_to(0.25*UP)
        dot1=Dot().move_to(UP*2+LEFT*3.5)
        note1=Tex('''He was the first one to write any\n
   mathematical function as $f(x)$.''').scale(0.75).next_to(dot1, RIGHT, buff=0.2)
        dot2=Dot().move_to(LEFT*3.5+UP*0.25)
        note2=Tex('''He was first to write e for base of natural\n
   logarithm. Also known as Eulers number.''').scale(0.75).next_to(dot2, RIGHT, buff=0.2)
        dot3=Dot().move_to(LEFT*3.5+DOWN*1.5)
        note3=Tex('''He was first to introduce $\pi$ as notation\n
       for ratio of circumference of circle to its\n
      diameter.''').scale(0.75).next_to(dot3, RIGHT, buff=0.2)
        dot4=Dot().move_to(LEFT*3.5+DOWN*3.25)
        note4=Tex('''He also introduced "$i$" as notation for $\sqrt{-1}$.''').scale(0.75).next_to(dot4, RIGHT, buff=0.2)


        
        self.add(
            title,
            dot1,
            note1,
            dot2,
            note2,
            dot3,
            note3,
            dot4,
            note4,
            logo
        )

class EulerDisc2(Scene):
    def construct(self):
        title=Tex("Complex analysis").move_to(UP*3.3).scale(1.2)
        logos=Text("e").scale(3)
        logot=Text("Euler TV").scale(0.5).next_to(logos, DOWN, buff=0.2)
        logo=VGroup(logos, logot).scale(4).set_opacity(0.1).move_to(0.25*UP)
        disc1=Tex('''He discovered what is now known as\n
Eulers Formula.''').move_to(UP*2).scale(0.75)
        eformula=MathTex("e^{i\\varphi}=cos(\\varphi)+isin(\\varphi)").move_to(UP)
        disc2=Tex("Euler's identity is special case of this :").move_to(UP*0).scale(0.75)
        iformula=MathTex("e^{i\pi}+1=0").move_to(DOWN)
        disc3=Tex('''This identity is particularly remarkable\n
as it involves e, $\pi$, i, 1, and 0,\n
arguably the five most important constants in\n
mathematics.''').scale(0.75).move_to(DOWN*2.5)


        self.add(
            title,
            logo,
            disc1,
            eformula,
            disc2,
            iformula,
            disc3
        )

class EulerIdentity(Scene):
    def construct(self):
        title=Tex("Euler's Formula").move_to(UP*3.3).scale(1.2)
        logos=Text("e").scale(3)
        logot=Text("Euler TV").scale(0.5).next_to(logos, DOWN, buff=0.2)
        logo=VGroup(logos, logot).scale(4).set_opacity(0.1).move_to(0.25*UP)
        complexplane=NumberPlane(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            y_length=5,
            axis_config={
                # "stroke_color": BLACK ,
                "stroke_width": 1.5
            },
            x_axis_config={
                # "color": ORANGE,
                # "numbers_to_include": np.arange(-1, 1, 1),
                # "numbers_with_elongated_ticks": np.arange(-1, 1, 1),
            },
            y_axis_config={
                # "color": ORANGE,
                # "numbers_to_include": np.arange(-1, 1, 1),
                # "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 3,
                "stroke_opacity": 0,
            },
            tips=True
        )
        circle=Circle(radius=2)
        b=1
        triangle=Polygon(
            [0,0,0],
            [b, 0, 0],
            [b, np.tan(60*DEGREES)*b,0],
            stroke_width=2
        )
        equation=MathTex("e^{i\\varphi}=cos(\\varphi)+isin(\\varphi)").scale(0.6).move_to(RIGHT*2.4+UP*2)
        dot1=Dot([b, np.tan(60*DEGREES)*b,0], radius=0.05)
        # dot1label=equation
        sine=MathTex("sin(\\varphi)").move_to(1.4*RIGHT+UP*0.7).scale(0.5)
        cosine=MathTex("cos(\\varphi)").next_to(triangle, DOWN, buff=0.001).scale(0.5)
        axislabel=complexplane.get_axis_labels(Tex("Re").scale(0.5), Tex("Im").scale(0.5))
        dot2=Dot(2,0,0)
        dot3=Dot(0,2,0)
        one=Tex("1").move_to(RIGHT*2.2+DOWN*0.2).scale(0.5)
        iota=Tex("$i$").move_to(UP*2.2+LEFT*0.2).scale(0.7)
        line1=Line([0,0,0],[b, np.tan(60*DEGREES)*b,0])
        line2=Line([0,0,0],[1,0,0])
        angle1=Angle(line2, line1, radius=0.25)
        phi=MathTex("\\varphi").scale(0.5).move_to(RIGHT*0.4+UP*0.2)
        quote=Text('''This is called as most remarkable formula in mathematics\n
                            by Richard Feynman''').scale(0.35).move_to(DOWN*3.2)

        self.add(
            title,
            logo,
            complexplane,
            circle,
            triangle,
            dot1,
            equation,
            sine,
            cosine,
            axislabel,
            one,
            iota,
            angle1,
            phi,
            quote
        )

class EulerDisc3(Scene):
    def construct(self):
        title=Tex("Analysis").move_to(UP*3.3).scale(1.2)
        logos=Text("e").scale(3)
        logot=Text("Euler TV").scale(0.5).next_to(logos, DOWN, buff=0.2)
        logo=VGroup(logos, logot).scale(4).set_opacity(0.1).move_to(0.25*UP)
        text00=Tex('''Discovered various powers series, the expression\n
of functions as sums of infinitely many terms.''').scale(0.75).move_to(UP*2.5)
        text01=Tex("Power series for $e$").scale(0.75).move_to(UP*1.8)
        power1=MathTex("e=\sum_{n=0}^{\infty} \\frac{1}{n!} = \lim_{n\\to\infty}\left(\\frac{1}{0!}+\\frac{1}{1!}+\\frac{1}{2!}+\cdots+\\frac{1}{n!}\\right)").scale(0.75).move_to(UP*1)
        text02=Tex("Power series for $\\tan^{-1}(z)$").scale(0.75)#.move_to()
        power2=MathTex("\\tan^{-1}(z)=\sum_{n=0}^{\infty }\\frac{(-1)^{n}z^{2n+1}}{2n+1}").scale(0.75).move_to(DOWN*1)
        text03=Tex('''Power series also helped him to solve famous\n
Basel problem of 1735''').scale(0.75).move_to(DOWN*2.3)
        power3=MathTex("\lim_{n\\to\infty}\left(\\frac{1}{1^{2}}+\\frac{1}{2^{2}}+\\frac{1}{3^{2}}+\cdots+\\frac{1}{n^{2}}\\right)=\\frac{\pi^{2}}{6}").scale(0.75).move_to(DOWN*3.3)

        self.add(
            title,
            logo,
            text00,
            text01,
            power1,
            text02,
            power2,
            text03,
            power3
        )

class EulerDisc4(Scene):
    def construct(self):
        title=Tex("Number Theory").move_to(UP*3.3).scale(1.2)
        logos=Text("e").scale(3)
        logot=Text("Euler TV").scale(0.5).next_to(logos, DOWN, buff=0.2)
        logo=VGroup(logos, logot).scale(4).set_opacity(0.1).move_to(0.25*UP)
        text00=Tex('''He proved that sum of reciprocals of\n
prime numbers diverges.''').scale(0.75).move_to(UP*2.4)
        formula1=MathTex("\sum_{p {\\text{prime}}}\\frac{1}{p}=\\frac {1}{2}+\\frac {1}{3}+\\frac {1}{5}+\\frac {1}{7}+\\frac {1}{11}+\cdots=\infty").scale(0.75).move_to(1.3*UP)
        text01=Tex('''He discovered relation between\n
Riemanns Zeta function and Prime numbers''').scale(0.75).move_to(UP*0.25)
        formula2=MathTex("\zeta(s)=\sum_{n=1}^{\infty}\\frac {1}{n^{s}}=\prod_{p{\\text{ prime}}}\\frac {1}{1-p^{-s}}").scale(0.75).move_to(DOWN*0.85)
        text02=Tex('''Euler proved Newton's identities,\n
Fermat's little theorem, Fermat's theorem\n
on sums of two squares, and made distinct\n
contributions to the Lagrange's four-square\n
theorem.''').scale(0.75).move_to(DOWN*2.7)

        self.add(
            title,
            logo,
            text00,
            formula1,
            text01,
            formula2,
            text02
        )