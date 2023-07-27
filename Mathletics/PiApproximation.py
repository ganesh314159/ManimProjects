from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
BLUE = "#7097e2"
RED = "#ed1c24"

# General definition of pi as the ratio of a circle's circumference to its diameter
class PiDefinition(Scene):
    def construct(self):
        # Introduction
        title1 = Text("Mathletics Club", color=BLUE).move_to(UP*2).scale(2)
        title2 = Tex(r"\textbf{Presents}").scale(1.5)
        title3 = Tex(r"\textbf{Pi Approximation}", color=RED).move_to(DOWN*2).scale(1.5)
        self.play(Write(title1))
        self.play(Write(title2))
        self.play(Write(title3))
        # self.wait(2)
        # group = VGroup(title1, title2, title3)
        # self.play(FadeOut(group))
        # self.wait(0.5)
        # tex00 = MathTex(r"\pi").scale(2.8)
        # self.play(Write(tex00))
        # self.wait(2)
        # self.play(tex00.animate.move_to(LEFT*4))
        # tex01 = MathTex(r"=").scale(1.8).next_to(tex00, RIGHT)
        # self.play(Write(tex01))
        # tex02 = MathTex(r"\frac{Circumference}{Diameter}").scale(1.8).next_to(tex01, RIGHT)  
        # tex02[0][0:13].set_color(RED)
        # tex02[0][14:23].set_color(BLUE)
        # self.play(Write(tex02))
        # self.wait(2)
        # group = VGroup(tex00, tex01, tex02)
        # self.play(group.animate.move_to(DOWN*2.2+LEFT*2.5))
        # self.wait(2)
        # # Create circle and line
        # circle = Circle(radius=1.5, color=RED).move_to(UP*1.5)
        # diameter = Line(start=RIGHT*1.5, end=LEFT*1.5, color=BLUE).move_to(circle.get_center()) # make this as diameter
        # self.play(TransformFromCopy(tex02[0][0:13], circle))
        # self.play(TransformFromCopy(tex02[0][14:23], diameter))
        # self.wait(2)
        # # wrap diameter around circle
        # arc1 = AnnularSector(inner_radius=1.47, outer_radius=1.53, start_angle=0, angle=2, color=BLUE, arc_center=circle.get_center())
        # arc11 = Arc(start_angle=0, angle=2, radius=1.5, color=BLUE, arc_center=circle.get_center())
        # self.play(TransformFromCopy(diameter, arc1))
        # arcbrace1 = ArcBrace(arc=arc11, direction=RIGHT)
        # self.play(DrawBorderThenFill(arcbrace1))
        # brace1label = MathTex(r"1").scale(0.8).next_to(arcbrace1, RIGHT)
        # self.play(Write(brace1label))
        # arc2 = AnnularSector(inner_radius=1.47, outer_radius=1.53, start_angle=2, angle=2, color=BLUE, arc_center=circle.get_center())
        # arc22 = Arc(start_angle=2, angle=2, radius=1.5, color=BLUE, arc_center=circle.get_center())
        # self.play(TransformFromCopy(diameter, arc2))
        # arcbrace2 = ArcBrace(arc=arc22, direction=RIGHT)
        # self.play(DrawBorderThenFill(arcbrace2))
        # brace2label = MathTex(r"1").scale(0.8).next_to(arcbrace2, LEFT)
        # self.play(Write(brace2label))
        # arc3 = AnnularSector(inner_radius=1.47, outer_radius=1.53, start_angle=4, angle=2, color=BLUE, arc_center=circle.get_center())
        # arc33 = Arc(start_angle=4, angle=2, radius=1.5, color=BLUE, arc_center=circle.get_center())
        # self.play(TransformFromCopy(diameter, arc3))
        # arcbrace3 = ArcBrace(arc=arc33, direction=RIGHT)
        # self.play(DrawBorderThenFill(arcbrace3))
        # brace3label = MathTex(r"1").scale(0.8).next_to(arcbrace3, DOWN)
        # self.play(Write(brace3label))
        # self.wait(2)
        # tex03 = MathTex(r"=").scale(1.8).next_to(tex02, RIGHT)
        # self.play(Create(tex03))
        # tex04 = MathTex(r"1",r"+",r"1",r"+",r"1",r"+",r".14159").next_to(tex03, RIGHT)
        # tex05 = MathTex(r"3.14159...").scale(1.8).next_to(tex03, RIGHT)
        # self.play(TransformFromCopy(brace1label, tex04[0]))
        # self.play(Write(tex04[1]))
        # self.play(TransformFromCopy(brace2label, tex04[2]))
        # self.play(Write(tex04[3]))
        # self.play(TransformFromCopy(brace3label, tex04[4]))
        # self.wait(2)
        # arc4 = AnnularSector(inner_radius=1.47, outer_radius=1.53, start_angle=6, angle=0.28318, color=BLUE, arc_center=circle.get_center())
        # arc44 = Arc(start_angle=6, angle=0.28318, radius=1.5, color=BLUE, arc_center=circle.get_center())
        # self.play(TransformFromCopy(diameter, arc4))
        # self.play(Write(tex04[5]))
        # arcbrace4 = ArcBrace(arc=arc44, direction=RIGHT)
        # self.play(Create(arcbrace4))
        # brace4label = MathTex(r"0.14159").scale(0.8).next_to(arcbrace4, RIGHT)
        # self.play(Write(brace4label))
        # self.play(TransformFromCopy(brace4label, tex04[6]))
        # self.wait(2)
        # self.play(Transform(tex04, tex05))
        # self.wait(2)
        

# Start with chronological history of pi
class Timeline(MovingCameraScene):
    def construct(self):
        numberline = NumberLine(
            x_range=[-2000, 2100, 100],
            length=75,
            include_numbers=True,
            include_tip=True,
            label_direction=DOWN,
            # axis_config={
            #     "numbers_to_include": np.arange(-2000, 2000, 100),
            #     "font_size": 24,
            # },
        ).next_to(ORIGIN, DOWN)
        indicator = ArrowTriangleFilledTip(color=RED).rotate(PI/2).scale(0.5).next_to(numberline.n2p(2023), UP)
        
        self.play(Create(numberline), Create(indicator))
        self.wait()
        self.play(self.camera.frame.animate.move_to(indicator.get_center()))
        self.wait()
# 1. Babylonians (1900-1680 BC) - 3.125
class Babylonians(Scene):
    def construct(self):
        tex01 = MathTex(r"\text{1. Babylonians (1900-1680 BC)}").scale(1.5).to_edge(UP)
        self.play(Write(tex01))
        self.wait(2)
        tex02 = MathTex(r"3.125").scale(1.8).next_to(tex01, DOWN)
# 2. Egyptians (1650 BC) - 3.1605
# 3. Archimedes (287-212 BC) - 3.1410
class Archimedes(Scene):
    def construct(self):
        tex01 = MathTex(r"\text{1. Archimedes (287-212 BC)}").scale(1.5).to_edge(UP)
        self.play(Write(tex01))
        self.wait(2)
        circle = Circle(radius=2, color=GREEN, stroke_width=1.0)
        self.play(Create(circle))
        self.wait()
        self.play(FadeOut(tex01))
        
        def get_radius(n, polygon):
            return Line(start=circle.get_center(), end=polygon.get_vertices()[n], color=PURPLE, stroke_width=1.0)
        
        polygon1 = RegularPolygon(n=6, color=PURPLE, fill_color=PURPLE, stroke_width=1.0).scale(2)
        radii6 = []
        for i in range (0, 6):
            radii6.append(get_radius(i, polygon1))
        self.play(Create(polygon1))
        self.wait()
        self.play(Create(VGroup(*radii6)))
        self.wait()
        
        tex02 = MathTex(r"\frac{6}{2}=3").move_to(LEFT*4.5)
        self.play(Write(tex02))
        self.wait()
        
        polygon11 = RegularPolygon(n=4, radius=2.83, color=RED, stroke_width=1.0).rotate(PI/4)
        self.play(Create(polygon11))
        self.wait()
        
        tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        self.play(Write(tex03))
        self.wait()
        
        tex04 = MathTex(r"3",r"< \pi <",r"4").move_to(UP*3)
        self.play(Write(tex04[1]))
        self.play(ReplacementTransform(tex02, tex04[0]), ReplacementTransform(tex03, tex04[2]))
        
        self.wait(2)
        
        text1 = Text(f"Perimeter of inscribed\npolygon:").scale(0.6).move_to(LEFT*4.5+UP)
        fcn = MathTex("c_n = 2r Sin(\\frac{180^\\circ}{n})").scale(0.8).next_to(text1, DOWN)
        n = MathTex("n = \\text{Number of sides}").scale(0.8).next_to(fcn, DOWN)
        text2 = Text(f"Perimeter of \ncircumscribed polygon:").scale(0.6).move_to(RIGHT*4.5+UP)
        fCN = MathTex("C_N = 2r Tan(\\frac{180^\\circ}{N})").scale(0.8).next_to(text2, DOWN)
        N = MathTex("N = \\text{Number of sides}").scale(0.8).next_to(fCN, DOWN)
        self.play(Write(text1), Write(text2))
        self.play(Write(fcn), Write(fCN))
        self.play(Write(n), Write(N))
        
        polygon2 = RegularPolygon(n=12, color=PURPLE, stroke_width=1.0).scale(2)
        radii12 = []
        cn = 12*np.sin(180*DEGREES/12)
        Cn = 8*np.tan(180*DEGREES/8)
        tex05 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon22 = RegularPolygon(n=8, radius=2.16, color=RED, stroke_width=1.0).rotate(PI/4)
        for i in range (0, 12):
            radii12.append(get_radius(i, polygon2))
        self.play(
            ReplacementTransform(polygon1, polygon2),
            ReplacementTransform(VGroup(*radii6), VGroup(*radii12)),
            ReplacementTransform(polygon11, polygon22),
            ReplacementTransform(tex04, tex05)
            )
        self.wait()
        
        polygon3 = RegularPolygon(n=24, color=PURPLE, stroke_width=1.0).scale(2)
        radii24 = []
        cn = 24*np.sin(180*DEGREES/24)
        Cn = 16*np.tan(180*DEGREES/16)
        tex06 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon33 = RegularPolygon(n=16, radius=2.05, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex07 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 24):
            radii24.append(get_radius(i, polygon3))
        self.play(
            ReplacementTransform(polygon2, polygon3),
            ReplacementTransform(VGroup(*radii12), VGroup(*radii24)),
            ReplacementTransform(polygon22, polygon33),
            ReplacementTransform(tex05, tex06)
        )
        self.wait()
        
        polygon4 = RegularPolygon(n=48, color=PURPLE, stroke_width=1.0).scale(2)
        radii48 = []
        cn = 48*np.sin(180*DEGREES/48)
        Cn = 32*np.tan(180*DEGREES/32)
        tex07 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon44 = RegularPolygon(n=32, radius=2.02, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex08 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 48):
            radii48.append(get_radius(i, polygon4))
        self.play(
            ReplacementTransform(polygon3, polygon4), 
            ReplacementTransform(VGroup(*radii24), VGroup(*radii48)),
            ReplacementTransform(polygon33, polygon44),
            ReplacementTransform(tex06, tex07)
            )
        self.wait()
        
        polygon5 = RegularPolygon(n=96, color=PURPLE, stroke_width=1.0).scale(2)
        radii96 = []
        cn = 96*np.sin(180*DEGREES/96)
        Cn = 64*np.tan(180*DEGREES/64)
        tex08 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon55 = RegularPolygon(n=64, radius=2.01, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 96):
            radii96.append(get_radius(i, polygon5))
        self.play(
            ReplacementTransform(polygon4, polygon5),
            ReplacementTransform(VGroup(*radii48), VGroup(*radii96)),
            ReplacementTransform(polygon44, polygon55),
            ReplacementTransform(tex07, tex08)
            )
        self.wait()
        
        polygon6 = RegularPolygon(n=194, color=PURPLE, stroke_width=1.0).scale(2)
        radii194 = []
        cn = 194*np.sin(180*DEGREES/194)
        Cn = 128*np.tan(180*DEGREES/128)
        tex09 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon66 = RegularPolygon(n=128, radius=2, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 194):
            radii194.append(get_radius(i, polygon6))
        self.play(
            ReplacementTransform(polygon5, polygon6),
            ReplacementTransform(VGroup(*radii96), VGroup(*radii194)),
            ReplacementTransform(polygon55, polygon66),
            ReplacementTransform(tex08, tex09)
            )
        self.wait()
        
        polygon7 = RegularPolygon(n=388, color=PURPLE, stroke_width=1.0).scale(2)
        radii388 = []
        cn = 388*np.sin(180*DEGREES/388)
        Cn = 256*np.tan(180*DEGREES/256)
        tex10 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon77 = RegularPolygon(n=256, radius=2, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 388):
            radii388.append(get_radius(i, polygon7))
        self.play(
            ReplacementTransform(polygon6, polygon7),
            ReplacementTransform(VGroup(*radii194), VGroup(*radii388)),
            ReplacementTransform(polygon66, polygon77),
            ReplacementTransform(tex09, tex10)
        )
        self.wait()
        
        polygon8 = RegularPolygon(n=388*2, color=PURPLE, stroke_width=1.0).scale(2)
        radii776 = []
        cn = 388*2*np.sin(180*DEGREES/(388*2))
        Cn = 512*np.tan(180*DEGREES/(512))
        tex11 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon88 = RegularPolygon(n=512, radius=2, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 388*2):
            radii776.append(get_radius(i, polygon8))
        self.play(
            ReplacementTransform(polygon7, polygon8),
            ReplacementTransform(VGroup(*radii388), VGroup(*radii776)),
            ReplacementTransform(polygon77, polygon88),
            ReplacementTransform(tex10, tex11)
        )
        self.wait()
        
        polygon9 = RegularPolygon(n=388*2*2, color=PURPLE, stroke_width=1.0).scale(2)
        radii38822 = []
        cn = 388*2*2*np.sin(180*DEGREES/(388*2*2))
        Cn = 512*2*np.tan(180*DEGREES/(512*2))
        tex12 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon99 = RegularPolygon(n=512*2, radius=2, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 388*2*2):
            radii38822.append(get_radius(i, polygon9))
        self.play(
            ReplacementTransform(polygon8, polygon9),
            ReplacementTransform(VGroup(*radii776), VGroup(*radii38822)),
            ReplacementTransform(polygon88, polygon99),
            ReplacementTransform(tex11, tex12)
        )
        self.wait()
        
        polygon10 = RegularPolygon(n=388*4*2, color=PURPLE, stroke_width=1.0).scale(2)
        radii38842 = []
        cn = 388*4*2*np.sin(180*DEGREES/(388*4*2))
        Cn = 512*4*np.tan(180*DEGREES/(512*4))
        tex13 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon1010 = RegularPolygon(n=512*4, radius=2, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 388*2*4):
            radii38842.append(get_radius(i, polygon10))
        self.play(
            ReplacementTransform(polygon9, polygon10),
            ReplacementTransform(VGroup(*radii38822), VGroup(*radii38842)),
            ReplacementTransform(polygon99, polygon1010),
            ReplacementTransform(tex12, tex13)
        )
        self.wait()
        
        polygon11 = RegularPolygon(n=388*8*2, color=PURPLE, stroke_width=1.0).scale(2)
        radii38882 = []
        cn = 388*8*2*np.sin(180*DEGREES/(388*2*8))
        Cn = 512*8*np.tan(180*DEGREES/(512*8))
        tex14 =  MathTex(f"{cn}",r"< \pi <",f"{Cn}").move_to(UP*3)
        polygon1111 = RegularPolygon(n=512*8, radius=2, color=RED, stroke_width=1.0).rotate(PI/4)
        # tex03 = MathTex(r"\frac{8}{2}=4").move_to(RIGHT*4.5)
        for i in range (0, 388*8*2):
            radii38882.append(get_radius(i, polygon11))
        self.play(
            ReplacementTransform(polygon10, polygon11),
            ReplacementTransform(VGroup(*radii38842), VGroup(*radii38882)),
            ReplacementTransform(polygon1010, polygon1111),
            ReplacementTransform(tex13, tex14)
        )
        self.wait()
        
        self.play(Circumscribe(tex14))
        self.wait()
        
        
        
# 4. Zu Chongzhi (429-501 AD) - 3.1415926
# 5. Madhava of Sangamagrama (1350-1425 AD) - 3.14159265359
class M2adhava(Scene):
    def construct(self):
        tex01 = MathTex(r"\text{2. Madhava of Sangamagrama (1350-1425 AD)}").scale(1.2).to_edge(UP)
        self.play(Write(tex01))
        self.wait(2)
        # madhava = ImageMobject("madhava.png").scale(2).move_to(LEFT*4)
        text = Text("Madhava-Leibniz Series").scale(1).move_to(UP*2)
        formula = MathTex(r"\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + ...").scale(1.5)
        self.play(Write(text))
        self.play(Write(formula))
        self.wait(2)
        text1 = Text("Madhava-Leibniz Series").scale(0.5).move_to(UP*2+LEFT*4)
        formula1 = MathTex(r"\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + ...").scale(0.75).move_to(UP*1+LEFT*4)
        self.play(ReplacementTransform(text, text1), ReplacementTransform(formula, formula1))
        self.wait(0.5)
        
        text2 = Text("Based on:").scale(0.5).move_to(DOWN*0.1+LEFT*4)
        formula2 = MathTex("\pi=4ArcTan(1)").scale(0.75).move_to(LEFT*4+DOWN)
        self.play(Write(text2))
        self.play(Write(formula2))
        self.wait(2)
        
        cortext = Text("Correction term:").scale(0.5).move_to(DOWN*1.8+LEFT*4)
        corformula = MathTex("-\\frac{(-1)^n}{2n-1}\\pm\\frac{n^{2}+1}{4n^{3}+5n}").move_to(DOWN*3+LEFT*4)
        self.play(Write(cortext))
        self.play(Write(corformula))
        
        self.wait(2)
                
        text3 = Text("Another series:").scale(0.5).move_to(UP*2+RIGHT*2)
        formula3 = MathTex("\pi=6ArcTan(\\frac{1}{\\sqrt{3}})").scale(0.75).move_to(UP*1+RIGHT*2)
        formula4 = MathTex("\pi=\\sqrt{12}\\sum_{k=0}^\\infty\\frac{(\\frac{1}{-3})^{-k}}{2k+1}").scale(0.75).move_to(RIGHT*2+DOWN*0.4)
        
        self.play(Write(text3))
        self.play(Write(formula3))
        self.play(Write(formula4))
        self.wait(2)
        
        text4 = MathTex("\\text{Computed } \pi \\text{ to 11 decimal places using 75 terms}").scale(0.75).move_to(DOWN*2+RIGHT*2)
        self.play(Write(text4))
        formula5 = MathTex("3.14159265358").scale(1.2).move_to(DOWN*3+RIGHT*2)
        self.play(Write(formula5))
        # self.wait(2)
        formula6 = MathTex("3.1415926535897").scale(1.2).move_to(DOWN*3+RIGHT*2)
        self.play(ReplacementTransform(formula5, formula6))
        
        
        
# 3. Ramanujan (1887-1920) - 3.141592653589793238462643383279502884197169399375105820974944592307816406286
class Ramanujan(Scene):
    def construct(self):
        tex01 = MathTex(r"\text{3. Ramanujan (1887-1920)}").scale(1.5).to_edge(UP)
        self.play(Write(tex01))
        self.wait(2)
        text = Text("Ramanujan Series").scale(1).move_to(UP*2)
        formula = MathTex(r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801}\sum_{k=0}^\infty\frac{(4k)!(1103+26390k)}{(k!)^4396^{4k}}").scale(1.5)
        self.play(Write(text))
        self.play(Write(formula))
        self.wait(2)
        text1 = Text("Ramanujan Series").scale(0.5).move_to(UP*2+LEFT*4)
        formula1 = MathTex(r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801}\sum_{k=0}^\infty\frac{(4k)!(1103+26390k)}{(k!)^4396^{4k}}").scale(0.75).move_to(UP*1+LEFT*4)
        self.play(ReplacementTransform(text, text1), ReplacementTransform(formula, formula1))
        self.wait(2)
        
        text2 = Text("Calculated Value using first term:").scale(0.5).move_to(DOWN*0.1+LEFT*4)
        formula2 = MathTex("\pi=\\frac{9801}{2206\\sqrt(2)} = 3.14159273").scale(0.75).move_to(LEFT*4+DOWN)
        
        self.play(Write(text2))
        self.play(Write(formula2))
        self.wait(2)
        
        text3 = Text("Chudnovsky Algorithm").scale(0.5).move_to(UP*2+RIGHT*2)
        formula3 = MathTex("\\frac{1}{\pi}=12\\sum_{k=0}^\\infty\\frac{(-1)^k(6k)!(13591409+545140134k)}{(3k)!(k!)^3(640320)^{3k+\\frac{3}{2}}}").scale(0.75).move_to(UP*1+RIGHT*3)
        self.play(Write(text3))
        self.play(Write(formula3))
        self.wait(2)
        text4 = MathTex("\\text{Calculated value of }","\pi").move_to(DOWN+RIGHT*2)
        text5 = MathTex("\\text{upto 200 Billion Digits using }").next_to(text4, DOWN)
        text6 = MathTex("\\text{Supercomputer and Ramanujans formula.}").next_to(text5, DOWN)
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Out(Scene):
    def construct(self):
        # text = Text("This short animated movie was created using").scale(0.8).move_to(UP*2)
        # text2 = Text("Manim, A Python Library and animation engine for explanatory math videos.").scale(0.5).move_to(UP)
        # text3 = Text("Created by Grant Sanderson of 3Blue1Brown.").scale(0.8)
        self.wait()
        text4 = Text("Thank you for watching!").scale(1.5)
        # self.play(Write(text))
        # self.play(Write(text2))
        # self.play(Write(text3))
        self.play(Write(text4))
        self.wait(2)
        self.play(FadeOut(text4), run_time=2)
