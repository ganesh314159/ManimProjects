from manim import *
import numpy as np
config.frame_size=(1080,1920)
class hetvik(Scene):
    def construct(self):
        text0=Text("Available at :").scale(1.5).move_to(UP*11)
        self.play(SpinInFromNothing(text0), run_time=2)
        text1=Text("SHIVAM FOODS", weight="BOLD").next_to(text0, DOWN*6.5).scale(2)
        self.play(GrowFromCenter(text1), run_time=1)
        logo1=ImageMobject("Pictures/hetvik-1.jpg").scale(1.3).move_to(UP*1.7)
        self.play(GrowFromCenter(logo1), run_time=1)
        addr=Text(''' Shop No.6, Nilkanth Shopping Centre,

   Cama Lane Corner, Ghatkopar West,

Mumbai Suburban, Maharashtra, 400086''').move_to(DOWN*6.6).scale(0.9)
        self.play(Write(addr), run_time=1)
        text2=Text(" Delivery Available").move_to(DOWN*10.3+RIGHT*0.7)
        home=ImageMobject("Pictures/home.png").next_to(text2, LEFT)
        self.play(GrowFromCenter(home), run_time=1)
        self.play(FadeIn(text2), run_time=1)
        self.wait(3)


class hetvik2(Scene):
    def construct(self):
        text0=Text("Available at:").scale(1.5).move_to(UP*10.5)
        # self.play(SpinInFromNothing(text0), run_time=2)
        text1=Text("SHIVAM FOODS", weight="BOLD").move_to(UP*8.5).scale(2)
        # self.play(GrowFromCenter(text1), run_time=1)
        logo1=ImageMobject("Pictures/hetvik-1.jpg").scale(1.3).move_to(UP*1.7)
        # self.play(GrowFromCenter(logo1), run_time=1)
        addr=Text(''' Shop No.6, Nilkanth Shopping Centre,

   Cama Lane Corner, Ghatkopar West,

Mumbai Suburban, Maharashtra, 400086''').move_to(DOWN*5.9).scale(0.9)
        # self.play(Write(addr), run_time=1)
        text2=Text(" Delivery Available").move_to(DOWN*9.1+RIGHT*0.7)
        home=ImageMobject("Pictures/home.png").next_to(text2, LEFT)
        # self.play(GrowFromCenter(home), run_time=1)
        # self.play(FadeIn(text2), run_time=1)
        text3=Text("DM for Orders / Contact: Henil Gala - 7045104467").move_to(DOWN*11.1).scale(0.75)
        rect1=Rectangle(height=24, width=13.5, stroke_width=7)
        group1=VGroup(text0, text1, addr, text2, rect1, text3)
        
        self.play(FadeIn(group1), FadeIn(home), FadeIn(logo1), run_time=3)
        self.wait(4)