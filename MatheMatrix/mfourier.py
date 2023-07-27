from manim import *
import numpy as np
from scipy import signal

class Fou(Scene):
    def construct(self):
        title1 = Text("Fourier analysis").scale(2).move_to(UP*0.9)
        title2 = Text("In Short").next_to(title1, DOWN).scale(0.8)
        title3 = Text("by Ganesh314159").next_to(title2, DOWN).scale(0.8)
        self.play(Write(title1))
        self.play(Write(title2))
        self.play(Write(title3))
        self.wait(1)
        self.play(Unwrite(title1), Unwrite(title2), Unwrite(title3))
        self.wait(1)
        axes = Axes(
                x_range=[-5, 5, 1],
                y_range=[-10, 10, 1],
                x_length=16,
                y_length=14,
                axis_config={
                    "color": WHITE ,
                    "stroke_width": 3
                },
                x_axis_config={
                    # "color": WHITE,
                    "numbers_to_include": np.arange(0, 5, 1),
                #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
                },
                y_axis_config={
                    # "color": WHITE,
                    "numbers_to_include": np.arange(0, 10, 1),
                #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
                },
                # background_line_style={
                #     "color": BLUE,
                #     "stroke_width": 3
                # },
                tips=True,
                
            ).scale(0.8).move_to(LEFT*6+DOWN*2.5)

        self.play(Create(axes))
        fx_graph = axes.plot(lambda x: x, x_range = [-10, 5], color = RED)
        gx_graph = axes.plot(lambda x: 2*x, x_range = [-10, 5], color = BLUE)
        hx_graph = axes.plot(lambda x: 3*x, x_range = [-10, 10/3], color = YELLOW)
        fx_label = axes.get_graph_label(fx_graph, label=r"f(x) = x", x_val = 5, direction = UP, color = RED).scale(0.75)
        gx_label = axes.get_graph_label(gx_graph, label=r"g(x) = 2x", x_val = 5, direction = UP, color = BLUE).scale(0.75)
        hx_label = axes.get_graph_label(hx_graph, label=r"h(x) = 3x", x_val = 4.4, direction = LEFT, color = YELLOW).scale(0.75)
        self.play(Create(fx_graph), Create(gx_graph), Create(hx_graph), Write(fx_label), Write(gx_label), Write(hx_label))
        tex1 = MathTex("f(x) = x", color = RED).move_to(UP)
        tex2 = MathTex("g(x) = 2x", color = BLUE).move_to(DOWN)
        tex3 = MathTex("h(x) = 3x", " = ", "f(x)", "-", "g(x)", color = YELLOW).move_to(RIGHT)
        self.play(Write(tex1), run_time = 1)
        self.play(Write(tex2), run_time = 1)
        self.wait(0.5)
        self.play(Create(axes), run_time = 1.5)
        self.play(Transform(tex1, fx_graph), Transform(tex2, gx_graph), ReplacementTransform(tex1, fx_label), ReplacementTransform(tex2, gx_label), run_time = 1.5)
        self.wait(2)
        self.play(Write(tex3[0]), run_time = 2)
        self.wait(1)
        self.play(Write(tex3[1]), run_time = 0.5)
        self.play(ReplacementTransform(tex3[1].copy(), hx_label))
        self.play(ReplacementTransform(fx_label.copy(), tex3[2]), Write(tex3[3]), run_time = 0.5)
        self.play(ReplacementTransform(gx_label.copy(), tex3[4]), run_time = 0.5)
        self.wait(1)
        self.play(Unwrite(tex3))
        self.wait(1)

        fline = Line(axes.coords_to_point(3,0), axes.coords_to_point(3,3), color=RED, stroke_width=5)
        gline = Line(axes.coords_to_point(3,0), axes.coords_to_point(3,6), color=BLUE, stroke_width=5)
        hline = Line(axes.coords_to_point(3,0), axes.coords_to_point(3,9), color=YELLOW, stroke_width=5)
        fdot = Dot(axes.coords_to_point(3,3))
        gdot = Dot(axes.coords_to_point(3,6))
        hdot = Dot(axes.coords_to_point(3,9))
        fdot_label = Tex("(3, ","f(3)",")").move_to(axes.coords_to_point(3.7,3)).scale(0.5)
        gdot_label = Tex("(3, ","g(3)",")").move_to(axes.coords_to_point(3.7,6)).scale(0.5)
        hdot_label = Tex("(3, ","h(3)",")").move_to(axes.coords_to_point(2.3,9)).scale(0.5)
        # self.add(hline, gline, fline, fdot, gdot, hdot, fdot_label, gdot_label, hdot_label)

        self.play(Create(hline), Create(gline), Create(fline))
        self.play(Create(fdot), Create(gdot), Create(hdot))
        self.play(Write(fdot_label), Create(gdot_label), Create(hdot_label))
        self.wait(1)

        self.wait(1)

        fline2 = fline.copy().move_to(RIGHT*3+DOWN*1.5)
        gline2 = gline.copy().move_to(RIGHT*3+UP*1)
        hline2 = hline.copy().move_to(RIGHT*5+UP*0.1)
        fbrace = BraceBetweenPoints(axes.coords_to_point(3,0), axes.coords_to_point(3,3), direction = LEFT).next_to(fline2, LEFT)
        fbrace_label = MathTex("f(3)").next_to(fbrace, LEFT).scale(0.75)
        gbrace = BraceBetweenPoints(axes.coords_to_point(3,0), axes.coords_to_point(3,6), direction = LEFT).next_to(gline2, LEFT)
        gbrace_label = MathTex("g(3)").next_to(gbrace, LEFT).scale(0.75)
        hbrace = BraceBetweenPoints(axes.coords_to_point(3,0), axes.coords_to_point(3,9), direction = RIGHT).next_to(hline2, RIGHT)
        hbrace_label = MathTex("h(3)").next_to(hbrace, RIGHT).scale(0.75)
        # self.add(fline2, gline2, hline2, fbrace, gbrace, hbrace, fbrace_label, gbrace_label, hbrace_label)

        self.play(ReplacementTransform(fline.copy(), fline2), ReplacementTransform(gline.copy(), gline2), run_time = 1)
        self.play(Create(fbrace), Create(gbrace), run_time = 0.5)
        self.play(ReplacementTransform(fdot_label[1].copy(), fbrace_label), ReplacementTransform(gdot_label[1].copy(), gbrace_label), run_time = 0.5)
        self.wait(1)
        self.play(ReplacementTransform(fline2.copy(), hline2), ReplacementTransform(gline2.copy(), hline2))
        self.wait(0.5)
        self.play(Create(hbrace))
        self.play(ReplacementTransform(hdot_label[1].copy(), hbrace_label))
        self.wait(0.5)
        self.play(ReplacementTransform(hline2.copy(), hline))
        self.wait(1)
        group = VGroup(axes, fline, fline2, fbrace, fbrace_label, gline, gline2, gbrace, gbrace_label, hline, hline2, hbrace, hbrace_label, fx_graph, fx_label, fdot, fdot_label, gx_graph, gx_label, gdot, gdot_label, hx_graph, hx_label, hdot, hdot_label, )

        self.play(group.animate.move_to(LEFT*6+DOWN*4))
        self.add(hline, gline, fline, fdot)

        self.wait(1)
        gdx = axes.plot(lambda x: -2*x, x_range = [-10, 5], color = GREEN)
        gdx_label = axes.get_graph_label(gdx, label=r"g(x) = -2x", x_val = 5, direction = LEFT, color = GREEN, buff = 1).scale(0.75)
        gddot = Dot(axes.coords_to_point(3,-6))
        hdx = axes.plot(lambda x: -1*x, x_range = [-10, 5], color = ORANGE)
        hdx_label = axes.get_graph_label(hdx, label=r"h(x) = -x", x_val = 3.5, direction = RIGHT, color = ORANGE).scale(0.75)
        hddot = Dot(axes.coords_to_point(3,-3))
        gdline = Line(axes.coords_to_point(3,0), axes.coords_to_point(3,-6), color=GREEN, stroke_width=5)
        hdline = Line(axes.coords_to_point(3,0), axes.coords_to_point(3,-3), color=ORANGE, stroke_width=5)
        fline3 = fline.copy().move_to(RIGHT*3+DOWN*0.15)
        gline3 = gdline.copy().move_to(RIGHT*4.5+DOWN*1)
        hline3 = hdline.copy().move_to(RIGHT*6+DOWN*1.85)
        
        # self.add(gdx, hdx, gdline, hdline, gddot, hddot, gdx_label, hdx_label, fline3, gline3, hline3)

        self.play(Create(gdx), run_time = 0.5)
        self.play(Create(hdx), Write(gdx_label), Create(gdline), Create(gddot), Write(gdot_label))
        self.wait(1)
        self.play(Write(hdx_label), Create(hdline), Create(hddot))
        self.wait(1)
        self.play(ReplacementTransform(gdline.copy(), gline3), run_time = 0.5)
        self.play(ReplacementTransform(fline.copy(), fline3), run_time = 0.5)
        self.wait(1)
        self.play(Create(hline3))

        self.wait(1)
        group2 = VGroup(gdx, hdx, gdline, hdline, gddot, hddot, gdx_label, hdx_label, fline3, gline3, hline3, fline, fline2, fbrace, fbrace_label, gline, gline2, gbrace, gbrace_label, hline, hline2, hbrace, hbrace_label, fx_graph, fx_label, fdot, fdot_label, gx_graph, gx_label, gdot, gdot_label, hx_graph, hx_label, hdot, hdot_label, )

        self.play(Uncreate(group2))

        axes2 = Axes(
                x_range=[-10, 15, 1],
                y_range=[-5, 5, 1],
                x_length=16,
                y_length=8,
                axis_config={
                    "color": WHITE ,
                    "stroke_width": 3
                },
                x_axis_config={
                    # "color": WHITE,
                    "numbers_to_include": np.arange(0, 15, 2),
                #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
                },
                y_axis_config={
                    # "color": WHITE,
                    "numbers_to_include": np.arange(-5, 6, 1),
                #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
                },
                # background_line_style={
                #     "color": BLUE,
                #     "stroke_width": 3
                # },
                tips=True,
                
            ).scale(0.8).move_to(LEFT*5)
        self.play(Transform(axes, axes2))

        sinefunc = axes2.plot(lambda x: np.sin(x), x_range = [-10, 15], color = RED)
        sine_label = MathTex("sin(x)", color = RED).next_to(sinefunc, RIGHT).scale(0.75)
        cosfunc = axes2.plot(lambda x: np.cos(x), x_range = [-10, 15], color = BLUE)
        cos_label = MathTex("cos(x)", color = BLUE).next_to(cosfunc, DOWN).scale(0.75)
        self.play(Create(sinefunc), Create(cosfunc), run_time = 1)
        self.wait(0.5)
        self.play(Write(sine_label), Write(cos_label))
        sinecosfunc = axes2.plot(lambda x: np.sin(x)+np.cos(x), x_range = [-10, 15], color = PURPLE)
        sc_label = MathTex("sin(x)+cos(x)", color = PURPLE).next_to(sinecosfunc, UP).scale(0.75)
        self.play(ReplacementTransform(sinefunc.copy(), sinecosfunc), ReplacementTransform(cosfunc.copy(), sinecosfunc))
        self.play(Write(sc_label))
        self.wait(1)
        group3 = VGroup(sine_label, sinecosfunc, cosfunc, cos_label, sc_label)
        self.play(Uncreate(group3))
        self.wait(1)
        eqn = MathTex("\sum _{n = 1}^{10}sin(nx)").move_to(RIGHT*4+UP*2)
        self.play(Write(eqn))
        def nsine(x, n):
            sine = 0
            for i in range(n):
                sine = sine + np.sin(i*x)
            return sine

        sine = axes2.plot(lambda x: nsine(x, 2), color = RED)
        # self.play(Create(sine))
        self.wait(2)
        text = MathTex("n = 1").move_to(RIGHT*4+DOWN)
        self.play(Write(text))
        self.wait(1)
        for i in range(10):
            sine2 = axes2.plot(lambda x: nsine(x, i), color = RED)
            self.play(Transform(sinefunc, sine2), Transform(text, MathTex(f"n = {i+1}").move_to(RIGHT*4+DOWN)), run_time = 0.5)
            self.wait(0.5)

        self.wait(1)

        # self.add(sine, cosine)

        group4 = VGroup(sinefunc, text, eqn)
        self.play(Uncreate(group4))
        self.wait(1)
        axes3 = Axes(
                x_range=[-10, 10, 1],
                y_range=[-2, 2, 1],
                x_length=16,
                y_length=5,
                axis_config={
                    "color": WHITE ,
                    "stroke_width": 3
                },
                x_axis_config={
                    # "color": WHITE,
                    "numbers_to_include": np.arange(-10, 10, 2),
                #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
                },
                y_axis_config={
                    # "color": WHITE,
                    "numbers_to_include": np.arange(-2, 3, 1),
                #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
                },
                # background_line_style={
                #     "color": BLUE,
                #     "stroke_width": 3
                # },
                tips=True,
                
            ).scale(0.8).move_to(UP*1.5)
        self.play(Transform(axes, axes3))

        saw1 = axes3.plot(lambda x: x/2, x_range = [-1*np.pi, np.pi], color = BLUE)
        saw2 = saw1.copy().move_to(axes3.coords_to_point(2*np.pi))
        saw3 = saw1.copy().move_to(axes3.coords_to_point(-2*np.pi))
        self.wait(0.5)
        self.play(Create(saw1), Create(saw2), Create(saw3))
        self.wait(1)
    
        def fawtooth(x, n):
            func = 0
            for i in range(n):
                sign = (-1)**(i+1)
                func = func + sign*(1/(i+1))*np.sin(((2*np.pi*(i+1)*x)/(2*np.pi))+np.pi)
            return func
        
        fousaw = axes3.plot(lambda x: fawtooth(x, 2), color = RED)
        self.play(Create(fousaw), run_time = 0.5)
        for i in range(10):
            sine = axes3.plot(lambda x: fawtooth(x, i), color = RED)
            self.play(Transform(fousaw, sine) )
            self.wait(0.5)

        self.wait(2)
        # self.add(saw1, saw2, saw3, fousaw)

        group5 = VGroup(saw1, saw2, saw3, fousaw)
        self.play(Uncreate(group5))
        self.wait(1)
        # self.play(Uncreate(group4))

        sdot1 = Dot(axes3.coords_to_point(0,1), fill_color = BLACK, stroke_color = WHITE, stroke_width = 1)
        sdot2 = Dot(axes3.coords_to_point(0,-1))
        psfunc = axes3.plot(lambda x: 1, x_range = [0,np.pi], color = BLUE)
        nsfunc = axes3.plot(lambda x: -1, x_range = [-1*np.pi,0], color = BLUE)
        # self.add(psfunc, nsfunc, sdot1, sdot2)
        self.play(Create(psfunc), Create(nsfunc))
        self.play(Create(sdot1), Create(sdot2))
        def fstep(x, n, l):
            func = 0
            for i in range(n):
                func = func + (1/(i+1))*(1-np.cos(np.pi*(i+1)))*np.sin((2*np.pi*(i+1)*x)/l)
            return func

        eqn = MathTex(r"\frac{2A}{\pi} \sum_{n=1}^{10}\frac{1}{n}(1-cos(\pi n))sin(\frac{2\pi nx}{L})").move_to(LEFT*2+DOWN*2)
        self.play(Write(eqn))
        fsfunc = axes3.plot(lambda x: 0.65*fstep(x, 2, 2), color = RED)
        self.play(Create(fsfunc))
        text = MathTex("n = 1").move_to(RIGHT*3+DOWN*2)
        self.play(Write(text))
        for i in range(10):
            func = axes3.plot(lambda x: 0.65*fstep(x, i, 2*np.pi), color = RED)
            self.play(Transform(fsfunc, func), Transform(text, MathTex(f"n = {i+1}").move_to(RIGHT*3+DOWN*2)))
            self.wait(0.5)

        self.wait(1)
        # self.add(fsfunc)

        group6 = VGroup(axes, psfunc, nsfunc, sdot1, sdot2, fsfunc, eqn, text)

        self.play(Uncreate(group6))
        self.wait(1)





