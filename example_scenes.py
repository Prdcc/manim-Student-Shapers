#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

def exponential_cos(x):
    return np.cos(np.exp( (-x**2) + 2))


class ExponentialCosConstruction(GraphScene):
    CONFIG = {
        "x_min" : -3,
        "x_max" : 3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-3,4,1),
        "center_point" : 0,
    }   
        
    def construct(self):
        self.setup_axes(animate=True)
        
        #latex isnt fully installed yet
        #exp_cos_definition = TexMobject("\cos\left(e^{-x^2 +2}\right)")
        #label_coord = self.coords_to_point(-3,5)
        #exp_cos_definition = question_marks.next_to(label_coord)
        
        
        exponential_cos_graph = self.get_graph(exponential_cos,self.function_color) #you're not using this in the end, see list stuff
        
        vert_line_pos = self.get_vertical_line_to_graph(2,exponential_cos_graph,color=YELLOW)
        
        
        #some illustration to show its even maybe, otherwise v/o
        
        roots = [0.671,1.244,-0.671,-1.244] #actual coords of the points
        roots = [self.coords_to_point(x,0) for x in roots]
        root_dots = [Dot().next_to(root,RIGHT*0) for root in roots]
              
        tps = [(0,0.4484),(0.40264,1),(-0.40264,1),(0.92481,-1),(-0.92481,-1)]
        tps = [self.coords_to_point(tp[0],tp[1]) for tp in tps]
        
        tp_points = [Dot(color = RED).next_to(tp,RIGHT*0) for tp in tps]
        tp_intervals = [(-0.1,0.1),(0.3,0.485),(0.85,1),(-0.485,-0.3),(-1,-0.85)]
        
                
        tp_interval_parts =[]
        for tp_interval in tp_intervals:
            xmin, xmax = tp_interval[0], tp_interval[1]
            tp_interval_parts += [self.get_graph(lambda x : exponential_cos(x), color = BLUE, x_min = xmin, x_max = xmax)]
        
        hori_asymptote= DashedLine(self.coords_to_point(-3, 1), self.coords_to_point(3, 1),color = WHITE)

        
        

        #all the other intervals around interesting characteristics you can reveal
        #maybe one that just shows the rest of the graph so it doesnt look weird or you miss a gap. also if you want to transform it from there, having a fully stiched together one hiding it the back ground, you can fade that in (while screen doesnt see a difference)
        #then fade out all jigsaw parts and then transform the stiched one, exponential_cos_graph. #also useful to maybe just do a positive one too, so you can illustrate evenness later. idk what to do about showing periodicities
        
        #now you're gonna wanna keep these in separate lists, so you can loop and make sure equally important things get shown at once. loop inside self.play i mean, over showcreaation
        #you can show them at different times here now too. just so you dont have to keep track of where they would be if you collated alll these lists together for some reason
                
        
        self.wait()
        
        #self.play(ShowCreation(exp_cos_definition))        
        for root_dot in root_dots:
            self.play(ShowCreation(root_dot))
        self.wait()
        

        
        for tp_dot in tp_points:
            self.play(ShowCreation(tp_dot))
            
        for tp_part in tp_interval_parts:
            self.play(ShowCreation(tp_part))
            
        self.wait(3)
        
        self.play(ShowCreation(hori_asymptote))
        
        self.play(ShowCreation(exponential_cos_graph),run_time = 2)
        self.wait()
        
        #putting all myobjects together as one VGroup now in order tofade them out at once
        root_dots = VGroup(*root_dots)
        tp_points = VGroup(*tp_points)
        tp_interval_parts = VGroup(*tp_interval_parts)
        self.play(FadeOut(root_dots),FadeOut(tp_points),FadeOut(tp_interval_parts),FadeOut(hori_asymptote))
        self.wait()

# See old_projects folder for many, many more
