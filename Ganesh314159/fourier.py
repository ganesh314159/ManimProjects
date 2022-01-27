from manim import *
import numpy as np
import itertools as it
from functools import reduce
import operator as op
import myconstants
from myconstants import *


# WARNING : THIS CODE IS MODIFIED ACCORDING TO MANIMCE V0.14.0, SO USE THAT VERSION ONLY ~Ganesh314159


########################################################################################
#     _    _         _                  _
#    / \  | |__  ___| |_ _ __ __ _  ___| |_
#   / _ \ | '_ \/ __| __| '__/ _` |/ __| __|
#  / ___ \| |_) \__ \ |_| | | (_| | (__| |_
# /_/   \_\_.__/|___/\__|_|  \__,_|\___|\__|
#  ____
# / ___|  ___ ___ _ __   ___  ___
# \___ \ / __/ _ \ '_ \ / _ \/ __|
#  ___) | (_|  __/ | | |  __/\__ \
# |____/ \___\___|_| |_|\___||___/
########################################################################################


class FourierCirclesScene(ZoomedScene):    #  <---- Works partially in ManimCE v0.14.0
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.n_vectors=10
        self.big_radius=2
        self.colors=[
            BLUE_D,
            BLUE_C,
            BLUE_E,
            GREY_BROWN,
        ]
        self.vector_config={
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.25,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 1.7,
        }
        self.circle_config={
            "stroke_width": 1,
        }
        self.base_frequency=1
        self.slow_factor=0.5
        self.center_point=ORIGIN
        self.parametric_function_step_size=0.001
        self.drawn_path_color=YELLOW
        self.drawn_path_stroke_width=2
        self.interpolate_config=[0, 1]
        # Zoom config
        self.include_zoom_camera=False
        self.scale_zoom_camera_to_full_screen=False
        self.scale_zoom_camera_to_full_screen_at=4
        self.zoom_factor=0.3
        self.zoomed_display_height=3
        self.zoomed_display_width=4
        self.image_frame_stroke_width=1
        self.zoomed_camera_config={
            "default_frame_stroke_width": 3,
            "cairo_line_width_multiple": 0.05,
        }
        self.zoom_position=lambda mob: mob.move_to(ORIGIN)
        self.zoom_camera_to_full_screen_config={
            "run_time": 3,
            "func": there_and_back_with_pause,
            "velocity_factor": 1
        }
        self.wait_before_start=2
        self.foreground_mobjects=[]

    def setup(self):
        ZoomedScene.setup(self)
        self.slow_factor_tracker = ValueTracker(
            self.slow_factor
        )
        self.vector_clock = ValueTracker(0)
        self.add(self.vector_clock)

    def add_vector_clock(self):
        self.vector_clock.add_updater(
            lambda m, dt: m.increment_value(
                self.get_slow_factor() * dt
            )
        )

    def get_slow_factor(self):
        return self.slow_factor_tracker.get_value()

    def get_vector_time(self):
        return self.vector_clock.get_value()

    def get_freqs(self):
        n = self.n_vectors
        all_freqs = list(range(n // 2, -n // 2, -1))
        all_freqs.sort(key=abs)
        return all_freqs

    def get_coefficients(self):
        return [complex(0) for _ in range(self.n_vectors)]

    def get_color_iterator(self):
        return it.cycle(self.colors)

    def get_rotating_vectors(self, freqs=None, coefficients=None):
        vectors = VGroup()
        self.center_tracker = VectorizedPoint(self.center_point)

        if freqs is None:
            freqs = self.get_freqs()
        if coefficients is None:
            coefficients = self.get_coefficients()

        last_vector = None
        for freq, coefficient in zip(freqs, coefficients):
            if last_vector:
                center_func = last_vector.get_end
            else:
                center_func = self.center_tracker.get_location
            vector = self.get_rotating_vector(
                coefficient=coefficient,
                freq=freq,
                center_func=center_func,
            )
            vectors.add(vector)
            last_vector = vector
        return vectors

    def get_rotating_vector(self, coefficient, freq, center_func):
        vector = Vector(RIGHT, **self.vector_config)
        vector.scale(abs(coefficient))
        if abs(coefficient) == 0:
            phase = 0
        else:
            phase = np.log(coefficient).imag
        vector.rotate(phase, about_point=ORIGIN)
        vector.freq = freq
        vector.coefficient = coefficient
        vector.center_func = center_func
        vector.add_updater(self.update_vector)
        return vector

    def update_vector(self, vector, dt):
        time = self.get_vector_time()
        coef = vector.coefficient
        freq = vector.freq
        phase = np.log(coef).imag

        vector.set_length(abs(coef))
        vector.set_angle(phase + time * freq * TAU)
        vector.shift(vector.center_func() - vector.get_start())
        return vector

    def get_circles(self, vectors):
        return VGroup(*[
            self.get_circle(
                vector,
                color=color
            )
            for vector, color in zip(
                vectors,
                self.get_color_iterator()
            )
        ])

    def get_circle(self, vector, color=BLUE):
        circle = Circle(color=color, **self.circle_config)
        circle.center_func = vector.get_start
        circle.radius_func = vector.get_length
        circle.add_updater(self.update_circle)
        return circle

    def update_circle(self, circle):
        circle.set(width=2 * circle.radius_func())
        circle.move_to(circle.center_func())
        return circle

    def get_vector_sum_path(self, vectors, color=YELLOW):
        coefs = [v.coefficient for v in vectors]
        freqs = [v.freq for v in vectors]
        center = vectors[0].get_start()

        path = ParametricFunction(
            lambda t: center + reduce(op.add, [
                complex_to_R3(
                    coef * np.exp(TAU * 1j * freq * t)
                )
                for coef, freq in zip(coefs, freqs)
            ]),
            # t_min=0,
            # t_max=1,
            t_range=np.array([0, 1]),
            color=color,
            dt=self.parametric_function_step_size,
        )
        return path

    def get_drawn_path_alpha(self):
        return self.get_vector_time()

    def get_drawn_path(self, vectors, stroke_width=None, **kwargs):
        if stroke_width is None:
            stroke_width = self.drawn_path_stroke_width
        path = self.get_vector_sum_path(vectors, **kwargs)
        broken_path = CurvesAsSubmobjects(path)
        broken_path.curr_time = 0
        start, end = self.interpolate_config

        def update_path(path, dt):
            alpha = self.get_drawn_path_alpha()
            n_curves = len(path)
            for a, sp in zip(np.linspace(0, 1, n_curves), path):
                b = (alpha - a)
                if b < 0:
                    width = 0
                else:
                    width = stroke_width * interpolate(start, end, (1 - (b % 1)))
                sp.set_stroke(width=width)
            path.curr_time += dt
            return path

        broken_path.set_color(self.drawn_path_color)
        broken_path.add_updater(update_path)
        return broken_path

    def get_y_component_wave(self,
                             vectors,
                             left_x=1,
                             color=PINK,
                             n_copies=2,
                             right_shift_rate=5):
        path = self.get_vector_sum_path(vectors)
        wave = ParametricFunction(
            lambda t: op.add(
                right_shift_rate * t * LEFT,
                path.function(t)[1] * UP
            ),
            t_min=path.t_min,
            t_max=path.t_max,
            color=color,
        )
        wave_copies = VGroup(*[
            wave.copy()
            for x in range(n_copies)
        ])
        wave_copies.arrange(RIGHT, buff=0)
        top_point = wave_copies.get_top()
        wave.creation = ShowCreation(
            wave,
            run_time=(1 / self.get_slow_factor()),
            rate_func=linear,
        )
        cycle_animation(wave.creation)
        wave.add_updater(lambda m: m.shift(
            (m.get_left()[0] - left_x) * LEFT
        ))

        def update_wave_copies(wcs):
            index = int(
                wave.creation.total_time * self.get_slow_factor()
            )
            wcs[:index].match_style(wave)
            wcs[index:].set_stroke(width=0)
            wcs.next_to(wave, RIGHT, buff=0)
            wcs.align_to(top_point, UP)
        wave_copies.add_updater(update_wave_copies)

        return VGroup(wave, wave_copies)

    def get_wave_y_line(self, vectors, wave):
        return DashedLine(
            vectors[-1].get_end(),
            wave[0].get_end(),
            stroke_width=1,
            dash_length=DEFAULT_DASH_LENGTH * 0.5,
        )

    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt)
        samples = np.array([
            path.point_from_proportion(t)
            for t in ts
        ])
        samples -= self.center_point
        complex_samples = samples[:, 0] + 1j * samples[:, 1]

        return [
            np.array([
                np.exp(-TAU * 1j * freq * t) * cs
                for t, cs in zip(ts, complex_samples)
            ]).sum() * dt for freq in freqs
        ]

    def zoom_config(self):
        # This is not in the original version of the code.
        self.activate_zooming(animate=False)
        self.zoom_position(self.zoomed_display)
        self.zoomed_camera.frame.add_updater(lambda mob: mob.move_to(self.vectors[-1].get_end()))

    def scale_zoom_camera_to_full_screen_config(self):
        # This is not in the original version of the code.
        def fix_update(mob, dt, velocity_factor, dt_calculate):
            if dt == 0 and mob.counter == 0:
                rate = velocity_factor * dt_calculate
                mob.counter += 1
            else:
                rate = dt * velocity_factor
            if dt > 0:
                mob.counter = 0
            return rate

        fps = 1 / self.camera.frame_rate
        mob = self.zoomed_display
        mob.counter = 0
        velocity_factor = 1 # self.zoom_camera_to_full_screen_config["velocity_factor"]
        mob.start_time = 0
        run_time = self.zoom_camera_to_full_screen_config["run_time"]
        run_time *= 2
        mob_height = mob.get_height()
        mob_width = mob.get_width()
        mob_center = mob.get_center()
        ctx = self.zoomed_camera.cairo_line_width_multiple

        def update_camera(mob, dt):
            line = Line(
                mob_center,
                self.camera.frame.get_center()
            )
            mob.start_time += fix_update(mob, dt, velocity_factor, fps)
            if mob.start_time <= run_time:
                alpha = mob.start_time / run_time
                alpha_func = self.zoom_camera_to_full_screen_config["func"](alpha)
                coord = line.point_from_proportion(alpha_func)
                mob.set(height=
                    interpolate(
                        mob_height,
                        self.camera.frame.get_height(),
                        alpha_func
                    ),
                    # stretch=True
                )
                mob.set(width=
                    interpolate(
                        mob_width,
                        self.camera.frame.get_width(),
                        alpha_func
                    ),
                    # stretch=True
                )
                self.zoomed_camera.cairo_line_width_multiple = interpolate(
                    ctx,
                    self.camera.cairo_line_width_multiple,
                    alpha_func
                )
                mob.move_to(coord)
            return mob

        self.zoomed_display.add_updater(update_camera)

class AbstractFourierOfTexSymbol(FourierCirclesScene):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=50
        self.center_point=ORIGIN
        self.slow_factor=0.05
        self.n_cycles=None
        self.run_time=10
        self.tex="$\Pi$"
        self.start_drawn=True
        self.path_custom_position=lambda mob: mob
        self.max_circle_stroke_width=1
        self.tex_class=Tex
        self.tex_config={
            "fill_opacity": 0,
            "stroke_width": 1,
            "stroke_color": WHITE
        }
        self.include_zoom_camera=False
        self.scale_zoom_camera_to_full_screen=False
        self.scale_zoom_camera_to_full_screen_at=1
        self.zoom_position=lambda mob: mob.scale(0.8).move_to(ORIGIN).to_edge(RIGHT)

    def construct(self):
        # This is not in the original version of the code.
        self.add_vectors_circles_path()
        if self.wait_before_start != None:
            self.wait(self.wait_before_start)
        self.add_vector_clock()
        self.add(self.vector_clock)
        if self.include_zoom_camera:
            self.zoom_config()
        if self.scale_zoom_camera_to_full_screen:
            self.run_time -= self.scale_zoom_camera_to_full_screen_at
            self.wait(self.scale_zoom_camera_to_full_screen_at)
            self.scale_zoom_camera_to_full_screen_config()
        if self.n_cycles != None:
            if not self.scale_zoom_camera_to_full_screen:
                for n in range(self.n_cycles):
                   self.run_one_cycle()
            else:
                cycle = 1 / self.slow_factor
                total_time = cycle * self.n_cycles
                total_time -= self.scale_zoom_camera_to_full_screen_at
                self.wait(total_time)
        elif self.run_time != None:
            self.wait(self.run_time)

    def add_vectors_circles_path(self):
        path = self.get_path()
        self.path_custom_position(path)
        coefs = self.get_coefficients_of_path(path)
        vectors = self.get_rotating_vectors(coefficients=coefs)
        circles = self.get_circles(vectors)
        self.set_decreasing_stroke_widths(circles)
        drawn_path = self.get_drawn_path(vectors)
        if self.start_drawn:
            self.vector_clock.increment_value(1)
        self.add(path)
        self.add(vectors)
        self.add(circles)
        self.add(drawn_path)

        self.vectors = vectors
        self.circles = circles
        self.path = path
        self.drawn_path = drawn_path

    def run_one_cycle(self):
        time = 1 / self.slow_factor
        self.wait(time)

    def set_decreasing_stroke_widths(self, circles):
        mcsw = self.max_circle_stroke_width
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=max(
                mcsw / k,
                mcsw,
            ))
        return circles

    def get_path(self):
        tex_mob = self.tex_class(self.tex, **self.tex_config)
        tex_mob.set(height=6)
        path = tex_mob.family_members_with_points()[0]
        return path

class AbstractFourierFromSVG(AbstractFourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=101
        self.run_time=10
        self.start_drawn=True
        self.file_name="Pictures/c_clef.svg"
        self.svg_config={
            "fill_opacity": 0,
            "stroke_color": WHITE,
            "stroke_width": 1,
            "height": 7
        }

    def get_shape(self):
        shape = SVGMobject(self.file_name, **self.svg_config)
        return shape

    def get_path(self):
        shape = self.get_shape()
        path = shape.family_members_with_points()[0]
        return path

class FourierOfPaths(AbstractFourierOfTexSymbol):    #  <---- Doesn't work in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=100
        self.name_color=WHITE
        self.tex_class=Tex
        self.tex=None
        self.file_name=None
        self.tex_config={
            "stroke_color": WHITE,
            "fill_opacity": 0,
            "stroke_width": 3,
        }
        self.svg_config={}
        self.time_per_symbol=5
        self.slow_factor=1 / 5
        self.parametric_function_step_siz= 0.01
        self.include_zoom_camera=False
        self.scale_zoom_camera_to_full_screen=False

    def construct(self):
        self.add_vector_clock()
        if self.tex != None:
            name = self.tex_class(self.tex, **self.tex_config)
        elif self.file_name != None and self.tex == None:
            name = SVGMobject(self.file_name, **self.svg_config)
        max_width = FRAME_WIDTH - 2
        max_height = FRAME_HEIGHT - 2
        name.set(width=max_width)
        if name.get_height() > max_height:
            name.set(height=max_height)

        frame = self.camera.frame
        frame.save_state()

        vectors = VGroup(VectorizedPoint())
        circles = VGroup(VectorizedPoint())
        for path in name.family_members_with_points():
            for subpath in path.get_subpaths():
                sp_mob = VMobject()
                sp_mob.set_points(subpath)
                coefs = self.get_coefficients_of_path(sp_mob)
                new_vectors = self.get_rotating_vectors(
                    coefficients=coefs
                )
                new_circles = self.get_circles(new_vectors)
                self.set_decreasing_stroke_widths(new_circles)

                drawn_path = self.get_drawn_path(new_vectors)
                drawn_path.clear_updaters()
                drawn_path.set_style(**self.tex_config)
                drawn_path.set_style(**self.svg_config)

                static_vectors = VMobject().become(new_vectors)
                static_circles = VMobject().become(new_circles)

                self.play(
                    Transform(vectors, static_vectors, remover=True),
                    Transform(circles, static_circles, remover=True),
                    frame.set(height=1.5 * name.get_height()).animate.move_to(path),
                )

                self.add(new_vectors, new_circles)
                self.vector_clock.set_value(0)
                self.play(
                    Create(drawn_path),
                    rate_func=linear,
                    run_time=self.time_per_symbol
                )
                self.remove(new_vectors, new_circles)
                self.add(static_vectors, static_circles)

                vectors = static_vectors
                circles = static_circles
        self.play(
            FadeOut(vectors),
            FadeOut(circles),
            Restore(frame),
            run_time=2
        )
        self.wait(3)

########################################################################################
########################################################################################
########################################################################################

#  ____  _                 _        _____                _
# / ___|(_)_ __ ___  _ __ | | ___  |  ___|__  _   _ _ __(_) ___ _ __
# \___ \| | '_ ` _ \| '_ \| |/ _ \ | |_ / _ \| | | | '__| |/ _ \ '__|
#  ___) | | | | | | | |_) | |  __/ |  _| (_) | |_| | |  | |  __/ |
# |____/|_|_| |_| |_| .__/|_|\___| |_|  \___/ \__,_|_|  |_|\___|_|
#                   |_|
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Using Tex or Text
class FourierOfTexSymbol(AbstractFourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        # if start_draw = True the path start to draw
        self.start_drawn=True
        # Tex config
        self.tex_class=Tex
        self.tex="$\Sigma$"
        self.tex_config={
            "fill_opacity": 0,
            "stroke_width": 1,
            "stroke_color": WHITE
        }
        # Draw config
        self.drawn_path_color=YELLOW
        self.interpolate_config=[0, 1]
        self.n_vectors=50
        self.big_radius=2
        self.drawn_path_stroke_width=2
        self.center_point=ORIGIN
        # Duration config
        self.slow_factor=0.1
        self.n_cycles=None
        self.run_time=10
        # colors of circles
        self.colors=[
            BLUE_D,
            BLUE_C,
            BLUE_E,
            GREY_BROWN,
        ]
        # circles config
        self.circle_config={
            "stroke_width": 1,
        }
        # vector config
        self.vector_config={
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.25,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 1.7,
        }
        self.base_frequency=1
        # definition of subpaths
        self.parametric_function_step_size=0.001

# Tex examples -------------------------------------------
# n_vectors
class Tsymbol20vectors(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=20
        self.run_time=10
        self.tex_class=Tex
        self.tex="$\\tau$"

class Tsymbol50vectors(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=50
        self.run_time=10
        self.tex_class=Tex
        self.tex="$\\tau$"

class Tsymbol150vectors(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=150
        self.run_time=10
        self.tex_class=Tex
        self.tex="$\\tau$"

class SigmaSymbol150vectors(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=150
        self.run_time=10 # 10 seconds
        self.tex_class=Tex # <-------- Default
        self.tex="$\Sigma$"
        self.zoomed_camera_config={
            "default_frame_stroke_width": 3,
            "cairo_line_width_multiple": 0.05,
        }
        self.zoom_camera_to_full_screen_config={
            "run_time": 3,
            "func": there_and_back_with_pause,
            "velocity_factor": 1
        }
        self.zoomed_camera_image_mobject_config={}
        self.zoomed_display_height=3
        self.zoomed_display_width=4
        self.image_frame_stroke_width=1
        self.zoom_factor=0.3
        self.zoomed_camera_frame_starting_position=np.array([0., 0., 0.])
        self.zoomed_display_center=None
        self.zoomed_display_corner=np.array([1., 1., 0.])
        self.zoomed_display_corner_buff=0.5
        self.slow_factor=0.5
        self.foreground_mobjects=[]

        # self.slow_factor=0.1 # <------- Added by Ganesh314159

# slow_factor
class SlowFactor0_1(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=30
        self.run_time=7
        self.tex_class=Tex
        self.tex="$\\Sigma$"
        self.slow_factor=0.1

class SlowFactor0_3(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=30
        self.run_time=7
        self.tex_class=Tex
        self.tex="$\\Sigma$"
        self.slow_factor=0.3

class SlowFactor0_5(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=30
        self.run_time=7
        self.tex_class=Tex
        self.tex="$\\Sigma$"
        self.slow_factor=0.5


# start_drawn
class StartDrawTrue(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.slow_factor=0.05
        self.n_vectors=30
        self.run_time=15
        self.tex="$\\tau$"
        self.start_drawn=True

class StartDrawFalse(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.slow_factor=0.05
        self.n_vectors=30
        self.run_time=15
        self.tex="$\\tau$"
        self.start_drawn=False


# interpolate_config
class InterpolateConfig0to1(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.slow_factor=0.05
        self.n_vectors=30
        self.run_time=15
        self.tex="$\\tau$"
        self.interpolate_config=[0,1]


class InterpolateConfig0_3to_1(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.slow_factor=0.05
        self.n_vectors=30
        self.run_time=15
        self.tex="$\\tau$"
        self.interpolate_config=[0.3, 1]


class InterpolateConfig1_to_1(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.slow_factor=0.05
        self.n_vectors=30
        self.run_time=15
        self.tex="$\\tau$"
        self.interpolate_config=[1,1]


# n_cycles vs run_time
class NCyclesVsRunTime(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=30
        self.n_cycles=3
        self.tex="$\\tau$"

# wait_before_start
class WaitBeforeStart(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=30
        self.n_cycles=1
        self.tex="$\\tau$"
        self.wait_before_start=2

# center_point
class CenterPoint(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=30
        self.n_cycles=1
        self.tex="$\\tau$"
        self.center_point=RIGHT*3


# path_custom_position
class CustomPosition(FourierOfTexSymbol):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=30
        self.n_cycles=1
        self.tex="$\\tau$"
        self.center_point=UP*3
        self.path_custom_position=lambda mob: mob.to_edge(LEFT)
        self.circle_config={"stroke_opacity":1}

# o x o x o x o x o x o x o x o x o x o x o x o x o x o x o x o x o x o x o x o x
# SVG
class FourierFromSVG(AbstractFourierFromSVG): # <--- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        # if start_draw = True the path start to draw
        self.start_drawn = True
        # SVG file name
        self.file_name = "Pictures/c_clef.svg"
        self.svg_config = {
            "fill_opacity": 0,
            "stroke_color": WHITE,
            "stroke_width": 1,
            "height": 7
        }
        # Draw config
        self.drawn_path_color = YELLOW
        self.interpolate_config = [0, 1]
        self.n_vectors = 50
        self.big_radius = 2
        self.drawn_path_stroke_width = 2
        self.center_point = ORIGIN
        # Duration config
        self.slow_factor = 0.1
        self.n_cycles = None
        self.run_time = 10
        # colors of circles
        self.colors = [
            BLUE_D,
            BLUE_C,
            BLUE_E,
            GREY_BROWN,
        ]
        # circles config
        self.circle_config = {
            "stroke_width": 1,
        }
        # vector config
        self.vector_config = {
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.25,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 1.7,
        }
        self.base_frequency = 1
        # definition of subpaths
        self.parametric_function_step_size = 0.001

# file_name
class SVGDefault(FourierFromSVG):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=100
        self.n_cycles=1
        self.file_name="Pictures/c_clef.svg"

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# __        ___ _   _      
# \ \      / (_) |_| |__   
#  \ \ /\ / /| | __| '_ \  
#   \ V  V / | | |_| | | | 
#    \_/\_/  |_|\__|_| |_| 
#  _____                              _                                      
# |__  /___   ___  _ __ ___   ___  __| |   ___ __ _ _ __ ___   ___ _ __ __ _ 
#   / // _ \ / _ \| '_ ` _ \ / _ \/ _` |  / __/ _` | '_ ` _ \ / _ \ '__/ _` |
#  / /| (_) | (_) | | | | | |  __/ (_| | | (_| (_| | | | | | |  __/ | | (_| |
# /____\___/ \___/|_| |_| |_|\___|\__,_|  \___\__,_|_| |_| |_|\___|_|  \__,_|
# ---------------------------------------------------------------------------------------
# The following works in both Tex and SVG
# ---------------------------------------
#      ---------------------------
#          ----------------

# How activate it
class ZoomedActivate(FourierFromSVG):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init(self):
        super().__init__()
        self.slow_factor = 0.05
        self.n_vectors = 50
        self.n_cycles = 1
        self.file_name = "Pictures/c_clef.svg"
        self.include_zoom_camera = True
        self.zoom_position = lambda zc: zc.to_corner(DR)

# Zoomed camera: Moving camera
# Zoomed display: Static camera
# More info: https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/extra/faqs/faqs.md#zoomed-scene-example
class ZoomedConfig(FourierFromSVG):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.slow_factor = 0.05
        self.n_vectors = 150
        self.n_cycles = 1
        self.file_name = "Pictures/c_clef.svg"
        self.path_custom_position = lambda path: path.shift(LEFT*2)
        self.center_point = LEFT*2
        self.circle_config = {
            "stroke_width": 0.5,
            "stroke_opacity": 0.2,
        }
        # Zoom config
        self.include_zoom_camera = True
        self.zoom_position = lambda zc: zc.to_edge(RIGHT).set_y(0)
        self.zoom_factor = 0.5
        self.zoomed_display_height = 5
        self.zoomed_display_width = 5
        self.zoomed_camera_config = {
            "default_frame_stroke_width": 3,
            "cairo_line_width_multiple": 0.05,
            # What is cairo_line_width_multiple?
            # See here: https://stackoverflow.com/questions/60765530/manim-zoom-not-preserving-line-thickness
        }

# Move Zoomed display to full screen
class ZoomedDisplayToFullScreen(FourierOfTexSymbol):    #  <---- Works partially in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.slow_factor = 0.05
        self.n_vectors = 30
        self.run_time = 16
        self.tex = "$\\tau$"
        # Zoom config
        self.include_zoom_camera = True
        self.zoom_position = lambda zc: zc.to_corner(DR)
        # Zoomed display to Full screen config
        self.scale_zoom_camera_to_full_screen = True
        self.scale_zoom_camera_to_full_screen_at = 4 # Move the camera at 4 seconds
        self.zoom_camera_to_full_screen_config = {
            "run_time": 3,
            "func": smooth,
            "velocity_factor": 1
        }

class ZoomedDisplayToFullScreenWithRestore(ZoomedDisplayToFullScreen):    #  <---- Works partially in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.run_time=12
        self.zoom_camera_to_full_screen_config={
            "run_time": 12,
            "func": lambda t: there_and_back_with_pause(t, 1/10)
        }


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

#  ____                                   _   _
# |  _ \ _ __ __ ___      __  _ __   __ _| |_| |__
# | | | | '__/ _` \ \ /\ / / | '_ \ / _` | __| '_ \
# | |_| | | | (_| |\ V  V /  | |_) | (_| | |_| | | |
# |____/|_|  \__,_| \_/\_/   | .__/ \__,_|\__|_| |_|
#                            |_|

# //////////////////////////////////////////////////////////////////////////////////////////

class FourierOfPathsTB(FourierOfPaths):    #  <---- Works partially in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors=100
        self.tex_class=Text
        self.tex="TB"
        self.tex_config={
            "stroke_color": RED,
        }
        self.time_per_symbol=5
        self.slow_factor=1/5


# Convert objects to paths
# Inkscape example: [ToolBar] Path > Object to path
class FourierOfPathsSVG(FourierOfPaths):    #  <---- Works perfectly in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors = 100
        self.file_name = "Pictures/c_clef.svg"
        self.svg_config = {
            "stroke_color": RED,
        }
        self.time_per_symbol=5
        self.slow_factor = 1/5

# //////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////

#   ____          _                  
#  / ___|   _ ___| |_ ___  _ __ ___  
# | |  | | | / __| __/ _ \| '_ ` _ \ 
# | |__| |_| \__ \ || (_) | | | | | |
#  \____\__,_|___/\__\___/|_| |_| |_|
                                   
#     _          _                 _   _                 
#    / \   _ __ (_)_ __ ___   __ _| |_(_) ___  _ __  ___ 
#   / _ \ | '_ \| | '_ ` _ \ / _` | __| |/ _ \| '_ \/ __|
#  / ___ \| | | | | | | | | | (_| | |_| | (_) | | | \__ \
# /_/   \_\_| |_|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|___/
# x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-

class CustomAnimationExample(FourierCirclesScene):    #  <---- Doesn't work in ManimCE v0.14.0
    def __init__(self):
        super().__init__()
        self.n_vectors = 200
        self.slow_factor = 0.2
        self.fourier_symbol_config = {
            "stroke_width": 0,
            "fill_opacity": 0,
            "height": 4,
            "fill_color": WHITE
        }
        self.circle_config = {
            "stroke_width": 1,
            "stroke_opacity": 0.3,
        }
    def construct(self):
        t_symbol = Text("T", **self.fourier_symbol_config)
        c_clef_symbol = SVGMobject("Pictures/c_clef.svg", **self.fourier_symbol_config)
        c_clef_symbol.match_height(t_symbol)
        # set gradient
        for mob in [t_symbol,c_clef_symbol]:
            mob.set_sheen(0,UP)
            mob.set_color(color=[BLACK,GRAY,WHITE])
        group = VGroup(t_symbol,c_clef_symbol).arrange(RIGHT,buff=0.1)
        # set paths
        path1 = t_symbol.family_members_with_points()[0]
        path2 = c_clef_symbol.family_members_with_points()[0]
        # path 1 config
        coefs1 = self.get_coefficients_of_path(path1)
        vectors1 = self.get_rotating_vectors(coefficients=coefs1)
        circles1 = self.get_circles(vectors1)
        drawn_path1 = self.get_drawn_path(vectors1)
        # path 2 config
        coefs2 = self.get_coefficients_of_path(path2)
        vectors2 = self.get_rotating_vectors(coefficients=coefs2)
        circles2 = self.get_circles(vectors2)
        drawn_path2= self.get_drawn_path(vectors2)
        # text definition
        text = Text("Thanks for watch!")
        text.scale(1.5)
        text.next_to(group,DOWN)
        # all elements toget
        all_mobs = VGroup(group,text)
        # set mobs to remove
        vectors1_to_fade = vectors1.copy()
        circles1_to_fade = circles1.copy()
        vectors1_to_fade.clear_updaters()
        circles1_to_fade.clear_updaters()
        vectors2_to_fade = vectors2.copy()
        circles2_to_fade = circles2.copy()
        vectors2_to_fade.clear_updaters()
        circles2_to_fade.clear_updaters()

        self.play(
            *[
                GrowArrow(arrow)
                for vg in [vectors1_to_fade, vectors2_to_fade]
                for arrow in vg
            ],
            *[
                ShowCreation(circle)
                for cg in [circles1_to_fade, circles2_to_fade]
                for circle in cg
            ],
            run_time=2.5,
        )
        self.remove(
            *vectors1_to_fade,
            *circles1_to_fade,
            *vectors2_to_fade,
            *circles2_to_fade,
        )
        self.add(
            vectors1,
            circles1,
            drawn_path1.set_color(RED),
            vectors2,
            circles2,
            drawn_path2.set_color(BLUE),
        )
        self.add_vector_clock()

        # wait one cycle
        self.wait( 1 / self.slow_factor)
        self.bring_to_back(t_symbol,c_clef_symbol)
        self.play(
            t_symbol.set_fill,None,1,
            c_clef_symbol.set_fill,None,1,
            run_time=3
        )
        self.wait()
        # move camera
        self.play(
            self.camera_frame.set_height, all_mobs.get_height()*1.2,
            self.camera_frame.move_to, all_mobs.get_center()
        )
        self.wait(0.5)
        self.play(
            Write(text)
        )
        self.wait(10)

# x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
# x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
# x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-


