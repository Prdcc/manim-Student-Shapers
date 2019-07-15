from manimlib.imports import *

class TrigRepresentationsScene(Scene):
    CONFIG = {
        "unit_length" : 2,
        "arc_radius" : 0.5,
        "axes_color" : GREEN,
        "circle_color" : RED,
        "theta_color" : YELLOW,
        "theta_height" : 0.3,
        "theta_value" : np.pi/5,
        "x_line_colors" : MAROON_B,
        "y_line_colors" : BLUE,

    }
    def setup(self):
        self.init_axes()
        self.init_circle()
        self.init_theta_group()

    def init_axes(self):
        self.axes = Axes(
            unit_size = self.unit_length
        )
        self.axes.set_color(self.axes_color)
        self.add(self.axes)

    def init_circle(self):
        self.circle = Circle(
            radius = self.unit_length,
            color = self.circle_color
        )
        self.add(self.circle)

    def init_theta_group(self):
        self.theta_group = self.get_theta_group()
        self.add(self.theta_group)

    def add_trig_lines(self, *funcs, **kwargs):
        lines = VGroup(*[
            self.get_trig_line(func, **kwargs)
            for func in funcs
        ])
        self.add(*lines)

    def get_theta_group(self):
        arc = Arc(0,
            self.theta_value, #i hcanged this
            radius = self.arc_radius,
            color = self.theta_color,
        )
        theta = TexMobject("\\theta")
        theta.shift(1.5*arc.point_from_proportion(0.5))
        theta.set_color(self.theta_color)
        theta.set_height(self.theta_height)
        line = Line(self.coords_to_point(0,0), self.get_circle_point())
        dot = Dot(line.get_end(), radius = 0.05)
        return VGroup(line, arc, theta, dot)

    def get_circle_point(self):
        return rotate_vector(self.unit_length*RIGHT, self.theta_value) #that used to be mult by RIGHT

    def get_trig_line(self, func_name = "sin", color = None):
        assert(func_name in ["sin", "tan", "sec", "cos", "cot", "csc"])
        is_co = func_name in ["cos", "cot", "csc"]
        if color is None:
            if is_co:
                color = self.y_line_colors 
            else:
                color = self.x_line_colors

        #Establish start point
        if func_name in ["sin", "cos", "tan", "cot"]:
            start_point = self.get_circle_point()
        else:
            start_point = ORIGIN

        #Establish end point
        if func_name is "sin":
            end_point = start_point[0]*RIGHT
        elif func_name is "cos":
            end_point = start_point[1]*UP
        elif func_name in ["tan", "sec"]:
            end_point = (1./np.cos(self.theta_value))*self.unit_length*RIGHT
        elif func_name in ["cot", "csc"]:
            end_point = (1./np.sin(self.theta_value))*self.unit_length*UP
        return Line(start_point, end_point, color = color)
    
    def get_line_brace_text(self, func_name = "sin"):
        line = self.get_trig_line(func_name)
        angle = line.get_angle()
        vect = rotate_vector(UP, angle)
        vect = np.round(vect, 1)
        if (vect[1] < 0) ^ (func_name is "sec"):
            vect = -vect
            angle += np.pi
        brace = Brace(
            Line(
                line.get_length()*LEFT/2,
                line.get_length()*RIGHT/2,
            ), 
            UP
        )
        brace.rotate(angle)
        brace.shift(line.get_center())
        
        if func_name == "sin": #when you dont know why its not working, just fix it
            brace.shift(DOWN*0.33 +RIGHT*0.4)
            
            
        brace.set_color(line.get_color())
        
        text = TexMobject("\\%s(\\theta)"%func_name)
        text.scale(0.75)
        text.add_background_rectangle()
        text.next_to(brace.get_center_of_mass(), vect, buff = 1.2*MED_SMALL_BUFF)
        return VGroup(line, brace, text)

    def get_tangent_line(self):
        return Line(
            self.unit_length*(1./np.sin(self.theta_value))*UP,
            self.unit_length*(1./np.cos(self.theta_value))*RIGHT,
            color = GREY
        )

class ExplainTrigFunctionDistances(TrigRepresentationsScene):
    CONFIG = {
        "alt_theta_val" : 2*np.pi/5,
    }
    def setup(self):
        TrigRepresentationsScene.setup(self)

    def construct(self):
        self.introduce_angle()
        self.show_sine_and_cosine()
    def introduce_angle(self):
        self.remove(self.circle)
        self.remove(self.theta_group)
        line, arc, theta, dot = self.theta_group
        line.rotate(-self.theta_value)
        brace = Brace(line, UP, buff = SMALL_BUFF)
        one = brace.get_text("1", buff = SMALL_BUFF)
        VGroup(line, brace, one).rotate(self.theta_value)
        one.rotate_in_place(-self.theta_value)
        self.circle.rotate(self.theta_value)

        words = TextMobject("Corresponding point")
        words.next_to(dot, UP+RIGHT, buff = 1.5*LARGE_BUFF)
        words.shift_onto_screen()
        arrow = Arrow(words.get_bottom(), dot, buff = SMALL_BUFF)

        self.play(
            ShowCreation(line),
            ShowCreation(arc),
        )
        self.play(Write(theta))
        self.play(
            ShowCreation(self.circle),
            Rotating(line, rate_func = smooth, in_place = False),
            run_time = 2
        )
        self.play(
            Write(words),
            ShowCreation(arrow),
            ShowCreation(dot)
        )
        self.wait()
        self.play(
            GrowFromCenter(brace),
            Write(one)
        )
        self.wait(2)
        self.play(*list(map(FadeOut, [
            words, arrow, brace, one
        ])))
        self.radial_line_label = VGroup(brace, one)

    def show_sine_and_cosine(self):
        sin_line, sin_brace, sin_text = sin_group = self.get_line_brace_text("sin")
        cos_line, cos_brace, cos_text = cos_group = self.get_line_brace_text("cos")

        self.play(ShowCreation(sin_line))
        self.play(
            GrowFromCenter(sin_brace),
            Write(sin_text),
        )
        self.play(ShowCreation(cos_line))
        self.play(
            GrowFromCenter(cos_brace),
            Write(cos_text),
        )
        self.wait()

        mover = VGroup(
            sin_group,
            cos_group,
            self.theta_group,
        )
        thetas = np.linspace(self.theta_value, self.alt_theta_val, 100)
        targets = []
        for theta in thetas:
            self.theta_value = theta
            targets.append(VGroup(
                self.get_line_brace_text("sin"),
                self.get_line_brace_text("cos"),
                self.get_theta_group()
            ))
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ],
            run_time = 5, 
            rate_func = there_and_back
        ))
        self.theta_value = thetas[0]

        self.wait()
        self.sin_group, self.cos_group = sin_group, cos_group