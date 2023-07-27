from manim import *
import numpy as np
from concurrent.futures import ProcessPoolExecutor

config.frame_size=(1080,1080)
MATHLETIS_COLOR = "#7097e2"
SOMAIYA_COLOR = "#ed1c24"

class SierpinkskiTri(Scene):
    def construct(self):
        text0 = Text("Sierpinkski Triangle", font="Times New Roman Cyr").scale(2)
        text1 = Text("Let's play a game, shall we?", font="Times New Roman Cyr").scale(1).move_to(UP*5.5)
        text2 = Text("Take three points as vertices of triangle.", font="Times New Roman Cyr").scale(1).move_to(DOWN*5)
        text3 = Text("Take any point randomly inside triangle.", font="Times New Roman Cyr").scale(1).move_to(DOWN*6)
        text41 = Text("Now choose any one point randomly,", font="Times New Roman Cyr").scale(1).move_to(DOWN*5)
        text42 = Text("from the three vertices of triangle.", font="Times New Roman Cyr").scale(1).move_to(DOWN*6)
        text51 = Text("Now plot a point exactly midway", font="Times New Roman Cyr").scale(1).move_to(DOWN*4.5)
        text52 = Text("between the point inside triangle", font="Times New Roman Cyr").scale(1).move_to(DOWN*5.5)
        text53 = Text("and the point chosen from vertices.", font="Times New Roman Cyr").scale(1).move_to(DOWN*6.5)
        text6 = Text("Repeat the process for the new point.", font="Times New Roman Cyr").scale(1).move_to(DOWN*6)
        self.play(Write(text0))
        self.wait(2)
        self.play(Transform(text0, text1))
        no_of_points = 1002 # int(input("No. of points : "))
        dota = Dot(point=UP*4, radius=0.05)
        dotb = Dot(point=LEFT*5*np.cos(PI/6)+DOWN*6*np.sin(PI/6), radius=0.05)
        dotc = Dot(point=RIGHT*5*np.cos(PI/6)+DOWN*6*np.sin(PI/6), radius=0.05)
        self.wait(1)
        self.play(Write(text2))
        self.wait(1)
        dotabc = VGroup(dota, dotb, dotc)
        self.play(Create(dotabc))
        self.wait(1)
        vertices = [dota, dotb, dotc]
        nth_point = 1
        text70 = Text("No. of points = ", font="Times New Roman Cyr").scale(0.8).move_to(UP*4+LEFT*4.5)
        text71 = Text(f"{nth_point}", font="Times New Roman Cyr").scale(0.8).move_to(UP*4+LEFT*2)
        dot0 = Dot(point=DOWN+LEFT*1.2, radius=0.05)
        self.play(Write(text3), Write(text70), Write(text71))
        self.wait(1)
        self.play(Create(dot0))
        self.wait(1)
        self.play(FadeOut(text2), FadeOut(text3))
        self.wait(0.5)
        self.play(Write(text41), Write(text42))
        self.wait(1)
        self.play(Circumscribe(dotb), run_time=2)   
        self.wait(0.5)    
        dot = []
        def plot_point(vert, ref_dot):
            dotp = dot0.copy().move_to((vertices[vert].get_center()+ref_dot.get_center())/2)
            return dotp
        dot1 = dot0.copy().move_to((dotb.get_center()+dot0.get_center())/2)
        nth_point = 2
        text72 = Text(f"{nth_point}", font="Times New Roman Cyr").scale(0.8).move_to(UP*4+LEFT*2)
        self.play(FadeOut(text41), FadeOut(text42))
        self.wait(0.5)
        self.play(Write(text51), Write(text52), Write(text53))
        self.wait(1)
        self.play(Create(dot1), ReplacementTransform(text71, text72))
        self.wait(0.5)
        self.play(FadeOut(text51), FadeOut(text52), FadeOut(text53))
        self.wait(0.5)
        self.play(Write(text6))
        dotp = dot1.copy()
        for i in range(no_of_points - 2):
            vertex = np.random.randint(0,3)
            dot.append(plot_point(vertex, dotp))
            dotp = dot[i].copy()
            
        self.wait(1)
        # self.add(text70)
        text71 = text72
        nth_point = 3
        # text72 = Text(f"{nth_point}", font="Times New Roman Cyr").scale(1).move_to(UP*4+LEFT*1.5)
        group1 = VGroup()
        print(len(dot))
        for j in range(101, 1000):
            group1.add(dot[j])
        
        group2 = VGroup()
        for j in range(0, 1000):
            group2.add(dot[j])
        
        for i in range(no_of_points - 2):    
            # text72 = Text(f"{nth_point}", font="Times New Roman Cyr").scale(0.8).move_to(UP*4+LEFT*2)
            # self.add(dot[i]).remove(text71).add(text72)
            # self.wait(1/nth_point)
            # text71 = text72
            # nth_point += 1
            if nth_point <= 10:
                text72 = Text(f"{nth_point}", font="Times New Roman Cyr").scale(0.8).move_to(UP*4+LEFT*2)
                self.add(dot[i]).remove(text71).add(text72)
                self.wait(0.5)
                text71 = text72
                nth_point += 1
            elif 10 < nth_point <= 100:
                text72 = Text(f"{nth_point}", font="Times New Roman Cyr").scale(0.8).move_to(UP*4+LEFT*2)
                self.add(dot[i]).remove(text71).add(text72)
                self.wait(0.1)
                text71 = text72
                nth_point += 1
        
        text72 = Text(f"1000", font="Times New Roman Cyr").scale(0.8).move_to(UP*4+LEFT*2)
        self.add(group1).remove(text71).add(text72)
                
            
        
        self.wait(1)
        self.play(FadeOut(text6))
        text8 = Text("Now, let's see what we have got.", font="Times New Roman Cyr").scale(1).move_to(DOWN*4.5)
        text9 = Text("This figure is known as Sierpinkski Triangle.", font="Times New Roman Cyr").scale(1).move_to(DOWN*5.5)
        self.play(Write(text8))
        self.wait(1)
        self.play(Write(text9))
        self.wait(2)
        self.play(FadeOut(text8), FadeOut(text9), FadeOut(dotabc), FadeOut(dot0), FadeOut(text70), FadeOut(text71), FadeOut(text72), FadeOut(dot1), FadeOut(text1), FadeOut(text0), FadeOut(group1), FadeOut(group2 )) 
        self.wait(1)
        
        
class SierpinkskiSquare(Scene):
    def construct(self):
        no_of_points = 10000 # int(input("No. of points : "))
        vert1 = Dot(point=UP*4+LEFT*4, radius=0.05)
        vert2 = Dot(point=UP*4+RIGHT*4, radius=0.05)
        vert3 = Dot(point=DOWN*4+RIGHT*4, radius=0.05)
        vert4 = Dot(point=DOWN*4+LEFT*4, radius=0.05)
        vertices = [vert1, vert2, vert3, vert4]
        vertgroup = VGroup(vert1, vert2, vert3, vert4)
        self.add(vertgroup)
        self.wait(1)
        
        def get_dots(vert, ref_dot):
            dot = Dot(point=((vertices[vert].get_center()+ref_dot.get_center())/2), radius=0.05)
            return dot
        dot = []
        dot0 = Dot(point=DOWN+LEFT*1.2, radius=0.05)
        dotp = dot0.copy()
        for i in range(no_of_points):
            vertex = np.random.randint(0,4)
            dot.append(get_dots(vertex, dotp))
            dotp = dot[i].copy()
        
        
        for i in range(no_of_points):
            self.add(dot[i])
            self.wait(0.5)
        


