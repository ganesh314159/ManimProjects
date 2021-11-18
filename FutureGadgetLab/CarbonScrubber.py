from manim import *
import numpy as np

class AFC(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 60, 10],
            y_range=[0, 2.5, 0.5],
            x_length=9,
            y_length=6,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 60, 10),
                # "numbers_with_elongated_ticks": np.arange(0, 60, 10),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 2.5, 0.5),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels(
            x_label=Tex("Temperature").scale(0.75),
            y_label=Tex("AFC").scale(0.75)
        )
        x_vals = [25, 40, 55]
        y_vals_KF = [0.134, 0.084, 0.052]
        y_vals_n = [1.61, 1.52, 1.43]
        y_vals_R2 = [0.9997, 0.9996, 0.9995]
        y_vals_are = [2.26, 2.37, 2.38]
        # y_vals_

        graph_KF=axes.plot_line_graph(x_values=x_vals, y_values=y_vals_KF, line_color=PURE_RED)
        kf_label=Tex("KF").next_to(graph_KF, UP, buff=0.1)
        graph_n=axes.plot_line_graph(x_values=x_vals, y_values=y_vals_n, line_color=GREEN)
        n_label=Tex("n").next_to(graph_n, UP, buff=0.1)
        graph_R2=axes.plot_line_graph(x_values=x_vals, y_values=y_vals_R2, line_color=BLUE)
        r2_label=Tex("$R^2$").next_to(graph_R2, UP, buff=0.1)
        graph_are=axes.plot_line_graph(x_values=x_vals, y_values=y_vals_are, line_color=YELLOW)
        are_label=Tex("ARE%").next_to(graph_are, UP, buff=0.1)

        self.add(axes, axes_labels, graph_KF, kf_label, graph_R2, r2_label, graph_are, are_label, graph_n, n_label,)