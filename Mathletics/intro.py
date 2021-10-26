from manim import *
from manimpango import *
import numpy as np

class Introduction(Scene):
    def construct(self):
        title=MarkupText("Mathletics", gradient=(BLUE, PURE_RED))
        # logo=Tex("$\\mathbb{M}$", "$\\mathnormal{M}$", "$\\mathrm{M}$", "$\\mathit{M}$", "$\\mathbf{M}$", "$\\mathsf{M}$", "$\\mathtt{M}$").scale(3)
        logob=ImageMobject("mathletics.png").move_to(UP*2.5).scale(0.85)
        logos=ImageMobject("mathletics.png").move_to(UP*3.25+LEFT*5).scale(0.3)
        # logo=Tex("$\\mathrm{M}$").scale(4).move_to(UP)
        logotext1=MarkupText("Mathletics Club", gradient=(BLUE, RED)).next_to(logob, DOWN, buff=0.5)
        logotext2=MarkupText("Mathletics Club", gradient=(BLUE, RED)).scale(1).move_to(3.25*UP)
        kjssclogo1=ImageMobject("kjssclogo.png").move_to(UP).scale(1.5)
        kjssclogo2=ImageMobject("kjssclogo.png").move_to(UP*3.25+RIGHT*5).scale(0.5)
        ltext=Tex("launches").next_to(kjssclogo1, DOWN).scale(1.5)
        self.wait(0.5)
        self.play(FadeIn(kjssclogo1), run_time=1)
        self.play(Write(ltext))
        self.wait(1)
        self.play(ReplacementTransform(kjssclogo1, kjssclogo2), Unwrite(ltext))
        # self.wait(0.5)
        self.play(FadeIn(logob), run_time=1)
        # self.play(Write(logos, fill_color=None))
        self.play(Write(logotext1.next_to(logob, DOWN, buff=0.2)), run_time=1)
        self.wait(1)

        slogan=Tex('''Let us take you to the beautiful depths of\n
truth, because Math is the only place where\n
truth and beauty mean the same thing.''').next_to(logotext1, DOWN, buff=0.5)
        stext=Text("by").move_to(DOWN*2).scale(0.5)
        self.play(Write(slogan), run_time=1)
        # self.play(Write(stext), run_time=0.5)
        self.wait(1)
        self.play(
            ReplacementTransform(logotext1, logotext2),
            ReplacementTransform(logob, logos),
            Unwrite(slogan),
            # Unwrite(stext),
            # ReplacementTransform(kjssclogo1, kjssclogo2),
            run_time=1
        )
        self.wait(0.5)
        text00=Tex('''\\textbf{Activities under the Club}''')
        self.play(Write(text00), run_time=0.5)
        self.wait(0.5)
        text01=Tex('''\\textbf{Activities under the Club}''').move_to(UP*2)
        self.play(ReplacementTransform(text00, text01), run_time=0.5)
        self.wait(0.5)
        # dotp=np.linspace(start, stop)
        dot1=Dot([-6.5, 1, 0], radius=0.06)
        dot2=Dot([-6.5, 0, 0], radius=0.06)
        dot3=Dot([-6.5, -1, 0], radius=0.06)
        dot4=Dot([-6.5, -2, 0], radius=0.06)
        dot5=Dot([-6.5, -3, 0], radius=0.06)
        self.play(Create(dot1), run_time=0.5)
        act1=Text("Continuous posting of mathematical wisdom").scale(0.45).next_to(dot1)
        self.play(Write(act1), run_time=0.75)
        self.wait(0.5)
        self.play(Create(dot2), run_time=0.5)
        act2=Text('''Organizing weekly recreational activities in mathematics such as
puzzles, riddles, catch-problems, number games etc.''').scale(0.45).next_to(dot2)
        self.play(Write(act2), run_time=0.75)
        self.wait(0.5)
        self.play(Create(dot3), run_time=0.5)
        act3=Text("Organizing webinars by renowned mathematics scholar.").scale(0.45).next_to(dot3)
        self.play(Write(act3), run_time=0.75)
        self.wait(0.5)
        self.play(Create(dot4), run_time=0.5)
        act4=Text('''Celebrating days and events pertaining to the history of mathematics
or people of mathematics.''').scale(0.45).next_to(dot4)
        self.play(Write(act4), run_time=0.75)
        self.wait(0.5)
        self.play(Create(dot5), run_time=0.5)
        act5=Text("Organizing competitions on interesting mathematical topics.").scale(0.45).next_to(dot5)
        self.play(Write(act5), run_time=0.75)
        self.wait(1)
        groupa1=VGroup(act1, act2, act3, act4, act5)
        self.play(Unwrite(groupa1))
        self.wait(0.5)
        act6=Text("Organizing mathematical exhibitions/fairs.").scale(0.45).next_to(dot1)
        self.play(Write(act6), run_time=0.75)
        self.wait(0.5)
        act7=Text('''Organizing outings of mathematical interest such as visits to
Mathematical institutions, Museums, Banks, Market Places etc.''').scale(0.45).next_to(dot2)
        self.play(Write(act7), run_time=0.75)
        self.wait(0.5)
        act8=Text('''Organizing events of watching mathematical documentaries, movies together,
or even going to places close to nature.''').scale(0.45).next_to(dot3)
        self.play(Write(act8), run_time=0.75)
        self.wait(0.5)
        act9=Text('''Sharing mathematical stories, meaningful poem on mathematics,
presentations on some topics by the members.''').scale(0.45).next_to(dot4)
        self.play(Write(act9), run_time=0.75)
        self.wait(0.5)
        act10=Text("Discussions on real life applications of Mathematics.").scale(0.45).next_to(dot5)
        self.play(Write(act10), run_time=0.75)
        self.wait(1)
        groupa2=VGroup(act6, act7, act7, act8, act9, act10, text01)
        groupd=VGroup(dot1, dot2, dot3, dot4, dot5)
        self.play(
            Unwrite(groupa2),
            Uncreate(groupd),
            
        )

        mentionb=Tex("\\textbf{Honourable mention}")
        mentions=Tex("\\textbf{Honourable mention}").move_to(UP*2)
        self.play(Write(mentionb))
        self.wait(0.5)
        self.play(ReplacementTransform(mentionb, mentions))

        co_foundt=Tex("Co-founder").move_to(UP*1)
        co_found1=Text("Hetvik Gada").move_to(LEFT*3).scale(0.5)
        co_found2=Text("Mihir Myatra").scale(0.5)#.move_to(UP*1)
        co_found3=Text("Garima Joshi").move_to(RIGHT*3).scale(0.5)
        self.play(Write(co_foundt), run_time=0.5)
        self.play(Write(co_found1), run_time=0.5)
        self.play(Write(co_found2), run_time=0.5)
        self.play(Write(co_found3), run_time=0.5)
        self.wait(1)

        hod=Text("Mr. Subhash Krishnan").scale(0.5).move_to(DOWN*2+LEFT*3.25)
        hodt=Tex("HOD of Department of Mathematics").next_to(hod, DOWN).scale(0.6)
        principle=Text("Dr. Pradnya Prabhu").scale(0.5).move_to(DOWN*2+RIGHT*3)
        principlet=Tex('''Principal\n
K. J. Somaiya College of Science and Commerce''').next_to(principle, DOWN).scale(0.6)
        self.play(Write(hod), run_time=0.5)
        self.play(Write(hodt.next_to(principlet, LEFT, buff=0.8)), run_time=0.5)
        self.play(Write(principle), run_time=0.5)
        self.play(Write(principlet), run_time=0.5)
        self.wait(1)

        grouphm=VGroup(co_foundt,co_found1,co_found2,co_found3,hod,hodt,principle,principlet)
        self.play(
            Unwrite(grouphm),
            FadeOut(logos),
            Unwrite(logotext2),
            FadeOut(kjssclogo2),
            Unwrite(mentions)
        )

        
        


