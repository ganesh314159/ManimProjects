from manim import *
import numpy as np
config.background_color = "BLACK"


class Script(Scene):
    def construct(self):
        # bg=SVGMobject("Pictures/illuminati.svg")
        # self.add(bg)

        # <---Creating illuminati--->
        tri0 = Triangle(color=BLACK, fill_opacity=1, stroke_color="#ff0000", stroke_opacity=0.8).scale(2)
        tri1 = Triangle(color=BLACK, fill_opacity=1, stroke_color="#ff0000", stroke_opacity=0.8, stroke_width=8).scale(2.2).move_to(UP*0.305)
        tri2 = Triangle(color=BLACK, fill_opacity=1, stroke_color="#ff0000", stroke_opacity=0.8).scale(2.4).move_to(UP*0.355)
        tri = VGroup(tri2, tri1, tri0).scale(1)
        cir = Circle(color=BLACK, radius=1.5, fill_opacity=1, stroke_color="#ff0000", stroke_opacity=0.8, stroke_width=13).move_to(DOWN*0.15)
        # un = Union()
        spike0 = Polygram(
            [
                [-0.04,0,0],
                [0.04,0,0],
                [0,-2,0]
        ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*2.8)
        spike1 = Polygram(
            [
                [-0.04,0.03,0],
                [0.04,0,0],
                [0,-1,0]
        ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(LEFT*0.5+DOWN*2.24)
        spike2 = Polygram(
            [
                [-0.04,0,0],
                [0.04,0.03,0],
                [0,-1,0]
        ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(RIGHT*0.5+DOWN*2.24)
        spikes0=VGroup(spike0, spike1, spike2)
        spikes1=spikes0.copy().rotate(2*PI/3, about_point=cir.get_center())
        spikes2=spikes1.copy().rotate(2*PI/3, about_point=cir.get_center())
        ueyelid=ArcBetweenPoints(
            cir.get_center()+LEFT*1.05,
            cir.get_center()+RIGHT*1.05,
            angle=-PI/3,
            stroke_color="#ff0000",
            stroke_opacity=0.8
        )
        deyelid=ArcBetweenPoints(
            cir.get_center()+LEFT*1.05,
            cir.get_center()+RIGHT*1.05,
            angle=PI/3,
            stroke_color="#ff0000",
            stroke_opacity=0.8
        )
        eyelids=VGroup(
            ueyelid,
            deyelid,
            color="#ff0000",
            fill_opacity=0.8,
            stroke_color="#ff0000",
            stroke_opacity=0.8
        )
        eyeborder=ArcBetweenPoints(
            cir.get_center()+UP*0.23+LEFT*0.44,
            cir.get_center()+UP*0.23+RIGHT*0.44,
            angle=1.02*PI,
            stroke_color="#ff0000",
            stroke_opacity=0.8
        )
        eyeflash0 = Circle(radius=0.03, color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8).move_to(eyeborder.get_center()+UP*0.15+RIGHT*0.15)
        eyeflash1 = ArcPolygonFromArcs(
            ArcBetweenPoints(
                eyeflash0.get_center()+DOWN*0.05+RIGHT*0.15,
                eyeflash0.get_center()+DOWN*0.06+RIGHT*0.2,
                angle=TAU/5,
                stroke_color="#ff0000",
                stroke_opacity=0.8
            ),
            ArcBetweenPoints(
                eyeflash0.get_center()+DOWN*0.05+RIGHT*0.15,
                eyeflash0.get_center()+DOWN*0.24,
                angle=-TAU/5,
                stroke_color="#ff0000",
                stroke_opacity=0.8
            ),
            ArcBetweenPoints(
                eyeflash0.get_center()+DOWN*0.24,
                eyeflash0.get_center()+DOWN*0.06+RIGHT*0.2,
                angle=TAU/5,
                stroke_color="#ff0000",
                stroke_opacity=0.8
            ),
            color="#ff0000",
            fill_opacity=0.8,
            stroke_color="#ff0000",
            stroke_opacity=0.8
        )
        eyeball=VGroup(eyeborder, eyeflash0, eyeflash1)
        # ineye = Intersection(eyelids, eyeball)
        eye=VGroup(eyelids, eyeball)
        ispike0 = Polygram(
            [
                [-0.04,0,0],
                [0.04,0,0],
                [0,1,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(UP*0.75)
        ispike1 = Polygram(
            [
                [-0.04,-0.01,0],
                [0.04,0,0],
                [-0.1,0.75,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(UP*0.61+LEFT*0.25)
        ispike2 = Polygram(
            [
                [-0.04,0,0],
                [0.04,-0.01,0],
                [0.1,0.75,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(UP*0.61+RIGHT*0.25)
        ispike3 = Polygram(
            [
                [-0.04,0,0],
                [0.04,0,0],
                [0,-0.6,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*0.85)
        ispike4 = Polygram(
            [
                [-0.04,0.01,0],
                [0.04,0,0],
                [-0.08,-0.55,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*0.815+LEFT*0.25)
        ispike5 = Polygram(
            [
                [-0.04,0.02,0],
                [0.04,0,0],
                [-0.15,-0.5,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*0.75+LEFT*0.51)
        ispike6 = Polygram(
            [
                [-0.04,0.03,0],
                [0.04,0,0],
                [-0.2,-0.45,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*0.65+LEFT*0.77)
        ispike7 = Polygram(
            [
                [-0.04,0,0],
                [0.04,0.01,0],
                [0.08,-0.55,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*0.815+RIGHT*0.25)
        ispike8 = Polygram(
            [
                [-0.04,0,0],
                [0.04,0.02,0],
                [0.15,-0.5,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*0.75+RIGHT*0.51)
        ispike9 = Polygram(
            [
                [-0.04,0,0],
                [0.04,0.03,0],
                [0.2,-0.45,0]
            ], color="#ff0000", fill_opacity=0.8, stroke_color="#ff0000", stroke_opacity=0.8
        ).move_to(DOWN*0.65+RIGHT*0.77)
        ispikes=VGroup(ispike0, ispike1, ispike2, ispike3, ispike4, ispike5, ispike6, ispike7, ispike8, ispike8, ispike9)
        illuminati = VGroup(cir, tri, spikes0, spikes1, spikes2, eye, ispikes).scale(1.2).move_to(ORIGIN)
        boundry = AnimatedBoundary(tri, colors=["#0004ff"], cycle_rate=5)
        self.play(Create(illuminati), run_time=2)
        # Creation of Illuminati ended
        self.wait(1)
        # Starting subtitles
        # with register_font("assets/fonts/"):
        line0=Text("Hello, Mr. Kashyap.", font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        line1=Text('''I can't reveal my identity due to confidential

                            reasons,''', font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        line2=Text("but we are in desperate need of your help.", font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        line3=Text('''A very valuable artifact was recently stolen

              from UNESCO museum.''', font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        line4=Text('''It has been informed to us that it was last

          seen in Chichén-Itzá, Mexico.''', font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        line5=Text('''But when my team reached there, something

        very unusual happened with them.''', font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        line6=Text('''You are our last hope.''', font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        line7=Text('''And we are willing to pay a large sum of

                         money.''', font="Marcellus").move_to(DOWN*2.4).scale(0.8)
        brcir = Circle(radius=1.5, stroke_color="#ff0000").move_to(UP)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1.5), GrowFromPoint(line0, cir.get_center()))
        self.wait(0.5)
        self.play(FadeOut(line0, shift=DOWN))
        self.wait(0.5)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1), GrowFromPoint(line1, cir.get_center()), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(line1, shift=DOWN))
        self.wait(0.5)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1), GrowFromPoint(line2, cir.get_center()), run_time=1)
        self.wait(1)
        self.play(FadeOut(line2, shift=DOWN))
        self.wait(0.5)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1), GrowFromPoint(line3, cir.get_center()), run_time=1)
        self.wait(3)
        self.play(FadeOut(line3, shift=DOWN))
        self.wait(0.5)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1), GrowFromPoint(line4, cir.get_center()), run_time=1)
        self.wait(3.2)
        self.play(FadeOut(line4, shift=DOWN))
        self.wait(0.5)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1.5), GrowFromPoint(line5, cir.get_center()))
        self.wait(3)
        self.play(FadeOut(line5, shift=DOWN))
        self.wait(0.5)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1.5), GrowFromPoint(line6, cir.get_center()))
        self.wait(0.2)
        self.play(FadeOut(line6, shift=DOWN))
        self.wait(0.5)
        self.play(Broadcast(brcir, focal_point=cir.get_center(), run_time=1.5), GrowFromPoint(line7, cir.get_center()))
        self.wait(1.3)
        self.play(FadeOut(line7, shift=DOWN))
        self.wait(0.5)        
        self.play(Uncreate(eye))
        self.play(Uncreate(spikes0),Uncreate(spikes1),Uncreate(spikes2), Uncreate(ispikes))
        self.play(Uncreate(tri))
        self.play(Uncreate(cir))
        self.wait(0.5)
