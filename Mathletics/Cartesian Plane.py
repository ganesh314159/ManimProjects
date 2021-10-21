
%%manim -qm -v WARNING Example

import numpy as np
config.media_width="100%"

class Example(Scene):
    def construct(self):
        # title00=Text("One of the greatest")
        # title00.move_to(UP*2)
        # title00.scale(2)
        # title01=Text("discovery of")
        # title01.move_to(DOWN*)
        # title01.scale(2)
        # title02=Text("all time")
        # title02.scale(2)
        # title02.move_to(DOWN*2)
        title03=MarkupText("Cartesian" + " Plane", gradient=(RED, BLUE))
        # title03.move_to(DOWN*1)
        title03.scale(2)
        
        # self.play(Write(title00), run_time=0.5)
        # self.play(Write(title01), run_time=0.5)
        self.play(Write(title03), run_time=2)
        self.wait(1)
        # self.play(ReplacementTransform(title00, title03),
        #           ReplacementTransform(title01, title03),
        #           ReplacementTransform(title02, title03))
        # self.wait(1.5)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "color": GREEN ,
                "stroke_width": 3
            },
            x_axis_config={
                "color": WHITE,
                "numbers_to_include": np.arange(-4, 5, 1),
            #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            y_axis_config={
                "color": WHITE,
                "numbers_to_include": np.arange(-4, 5, 1),
            #     "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            # background_line_style={
            #     "color": BLUE,
            #     "stroke_width": 3
            # },
            tips=True,
            
        )
        self.play(ReplacementTransform(title03, axes))
        self.wait(1.5)
        text00=Text("It was discovered by"+"\n   René Descartes").shift(UP*2.4+LEFT*2.5).scale(0.5)
        photo=Rectangle(width=1, height=1, stroke_width=0.5).shift(UP*1.3+LEFT*5.3)
        text01=Text("René Descartes"+"\n   1596 - 1650").shift(LEFT*5.3).scale(0.5)
        self.play(Write(text00), run_time=1)
        self.play(ReplacementTransform(text00.copy(), text01))
        self.wait(1.5)
        # self.play(FadeOut(text00), run_time=1)
        text20=Text("    It became connecting link"+"\nbetween Algebra and Geometry").shift(UP*2.7+RIGHT*4.2).scale(0.5)
        circle1=Circle(color=BLUE).scale(1.4)
        decimal=DecimalNumber()# .shift(UP*2+RIGHT*5)
        decimal.add_updater(lambda d: d.set_value(circle1.scale))
        tex00=MathTex("x^{2}","+","y^{2}","=","2").shift(UP*2+RIGHT*4)

        self.play(ReplacementTransform(text00, text20), run_time=1)
        self.play(Create(circle1), Write(tex00))
        # self.play(circle1.animate.set(radius=5))
        self.wait(1)
        tex01=MathTex("y","=","x","^{2}", color=BLUE).shift(UP*2+RIGHT*4)
        graph1=axes.get_graph(lambda x: x**2, color=BLUE, x_range=[-5,5])
        self.play(ReplacementTransform(circle1, graph1), ReplacementTransform(tex00, tex01))
        self.wait(3)
        sin_graph = axes.get_graph(lambda x: np.sin(x), x_range=[-4,4], color=BLUE)
        cos_graph = axes.get_graph(lambda x: np.cos(x), x_range=[-4,4], color=RED)
        # tex02=MathTex("y","=","Sin(x)", color=BLUE).shift(UP*2+RIGHT*4)
        # tex03=MathTex("y","=","Cos(x)", color=RED).shift(UP*1+RIGHT*4)

        sin_label = axes.get_graph_label(sin_graph, label="\\sin(x)", x_val=2, direction=UP / 2)
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)", x_val=-3, direction=DOWN / 1)
        self.play(Uncreate(graph1),
                  Create(sin_graph), 
                  Create(cos_graph),
                  Unwrite(tex01, run_time=0.5),
                  # Write(tex02),
                  # Write(tex03),
                  Write(sin_label),
                  Write(cos_label),
                  run_time=2)
        self.wait(3)
        self.play(Unwrite(text20),
                  # Unwrite(tex02),
                  # Unwrite(tex03),
                  Unwrite(sin_label),
                  Unwrite(cos_label),
                  Uncreate(sin_graph),
                  Uncreate(cos_graph),
                  Unwrite(text01),
                  run_time=1.5
        )
        text30=Text("It also played fundamental role").shift(LEFT*4+UP*3).scale(0.5)
        text31=Text("in development of Calculus").shift(LEFT*4+UP*2.5).scale(0.5)
        text32=Text("by Sir Issac Newton").shift(LEFT*4+UP*2).scale(0.5)
        text33=Text("and Gottfried Wilhelm Leibniz").shift(LEFT*4+UP*1.5).scale(0.5)
        text34=Text("Issac Newton"+"\n  1643-1727").shift(RIGHT*5.1+UP*0.5).scale(0.5)
        text35=Text("Gottfried Leibniz"+"\n     1646-1716").shift(RIGHT*5.1+DOWN*3.5).scale(0.5)
        tex10=MathTex("ln(x)")
        tex11=MathTex("e^{x}")

        graph2=axes.get_graph(lambda x: np.log(x), x_range=[0.00000000001, 4], color=BLUE)
        graph3=axes.get_graph(lambda x: np.e**x , x_range=[-4, 4], color=RED)
        graph2_label = axes.get_graph_label(graph2, label=tex10, x_val=3, direction=UP*1.5)
        graph3_label = axes.get_graph_label(graph3, label=tex11, x_val=-1, direction=UP)
        line0 = Line(axes.coords_to_point(0.5,1.64872), axes.coords_to_point(1.25,3.49034), color=GREEN, stroke_width=5)
        line1 = Line(axes.coords_to_point(0.5,1.64872), axes.coords_to_point(1.25,1.64872), color=GREEN, stroke_width=5)
        line2 = Line(axes.coords_to_point(1.25,3.49034), axes.coords_to_point(1.25,1.64872), color=GREEN, stroke_width=5)

        brace1 = Brace(line1, [0,-1,0], sharpness=1, buff=0.07, color=GREEN)
        brace2 = Brace(line2, [1,0,0], sharpness=1, buff=0.07, color=GREEN)
        brace1_label = Tex("$\\Delta x$").scale(0.8).next_to(brace1, DOWN*0.4)
        brace2_label = Tex("$f(x+\\Delta x)$").scale(0.8).next_to(brace2, RIGHT)
        # tex20=Tex("$f\\left( x \\right) = \\mathop {\\lim }\\limits_{\\Delta x \\to 0} \\frac{{f\\left( {x + \\Delta } \\right) - f\\left( x \\right)}}{\\Delta }$")
        tex20=MathTex("f'(x) = \lim_{\\Delta x \\rightarrow 0}","{","f(x+ \\Delta x)"," - ","f(x)"," \\over ","\\Delta x","}")
        tex21=MathTex(r"\int","_","a","^","b"," f'(x)","dx"," = ","f(b)","- ","f(a)")
        tex20.scale(0.85).shift(LEFT*3.8+DOWN*1.5)
        tex21.scale(0.85).shift(LEFT*3.8+DOWN*3)

        self.play(Write(text30), Create(graph2), Write(graph2_label))
        self.play(Write(text31), Create(graph3), Write(graph3_label))
        self.play(Write(text32))
        self.play(Write(text33), ReplacementTransform(text32.copy(), text34))
        self.play(ReplacementTransform(text33.copy(), text35))
        self.play(Create(line0))
        self.play(Create(line1), Create(line2))
        self.play(Create(brace1), Create(brace2))
        self.play(Create(brace1_label), Create(brace2_label))
        self.wait(1)
        self.play(ReplacementTransform(brace2_label.copy(), tex20[2]),
                  ReplacementTransform(brace1_label.copy(),tex20[-2]),
                  ReplacementTransform(graph3_label.copy(), tex20[-4]),
                  Write(tex20[0]),
                  Write(tex20[3]),
                  Write(tex20[-3]),
                  run_time=2
                 )

        line3=axes.get_vertical_line(axes.input_to_graph_point(2, graph2), color=YELLOW)
        line4=axes.get_vertical_line(axes.input_to_graph_point(3, graph2), color=YELLOW)
        area1=axes.get_area(graph2, x_range=[2,3], color=ORANGE, opacity=0.05)
        line3_label=MathTex("a").next_to(line3, LEFT*0.3).scale(0.85)
        line4_label=MathTex("b").next_to(line4, RIGHT*0.3).scale(0.85)


        self.play(Create(line3), Create(line4), FadeIn(area1))
        self.play(Write(line3_label), Write(line4_label))
        self.wait(1)
        self.play(Write(tex21[-4:]),
                  ReplacementTransform(area1.copy(), tex21[0]),
                  ReplacementTransform(area1.copy(), tex21[6]),
                 )
        self.play(ReplacementTransform(graph2_label.copy(), tex21[5]),
                  ReplacementTransform(line3_label.copy(), tex21[2]),
                  ReplacementTransform(line4_label.copy(), tex21[4])
                 )

        self.wait(2)
        group1 = VGroup(graph2, graph3, brace1, brace2, brace1_label, brace2_label, line0, line1, line2, line3, line4, )
        group2 = VGroup(text30, text31, text32, text33, text34, text35, tex10, tex11, tex20, tex21, line3_label, line4_label)
        self.play(Uncreate(group1), Unwrite(group2), FadeOut(area1))
        self.wait(0.5)

        text40=Text("Also there are"+"\nsome modified"+"\n   versions of"+"\ncartasian plane").shift(5*LEFT+2*UP).scale(0.5)
        text41=Text("  We will talk"+"\nabout them in"+"\n  later videos").shift(5*LEFT).scale(0.5)
        
        numbar=NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "color": WHITE ,
                "stroke_width": 3
            },
            x_axis_config={
                "color": ORANGE,
                "numbers_to_include": np.arange(-4, 5, 1),
                "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            y_axis_config={
                "color": ORANGE,
                "numbers_to_include": np.arange(-4, 5, 1),
                "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 3
            },
            tips=True,
        )
        text50=Text("Number Plane").shift(RIGHT*5+UP*2).scale(0.5)
        self.play(ReplacementTransform(axes, numbar), Write(text40), Write(text50),  run_time=3)
        self.wait(1)

        complexplane=ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "color": WHITE ,
                "stroke_width": 3
            },
            x_axis_config={
                "color": ORANGE,
                "numbers_to_include": np.arange(-4, 5, 1),
                "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            y_axis_config={
                "color": ORANGE,
                "numbers_to_include": np.arange(-4, 5, 1),
                "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 3
            },
            tips=True
         )
        complexplane.add_coordinates()
        text51=Text("Complex Plane").shift(RIGHT*5+UP*2).scale(0.5)
        self.play(ReplacementTransform(numbar, complexplane), ReplacementTransform(text50, text51))
        self.wait(1)
        
        polarplane = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=33.6,
            radius_config={"font_size": 33.6},
        ).add_coordinates()
        text52=Text("Polar Plane").shift(RIGHT*5+UP*2).scale(0.5)
        # self.play(ReplacementTransform(complexplane, polarplane), ReplacementTransform(text51, text52), Write(text41))
        self.play(Uncreate(complexplane))
        self.play(Write(text41), ReplacementTransform(text51, text52), Create(polarplane, run_time=2))

        self.wait(1)
        self.play(Uncreate(polarplane), Unwrite(text41), Unwrite(text52), run_time=1)