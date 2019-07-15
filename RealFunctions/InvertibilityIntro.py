from manimlib.imports import *
import numpy as np

def doubling_line(x):
    return 2*x

def hidden_flat_line(x):
    return 0

def parabola(x):
    return x**2

def cubic(x):
    return (0.5*x)**3

def invCubic(x):
    x*=8
    if(x >= 0):
        return x**(1./3.)
    else:
        return -((-x)**(1./3.))

class CubicIsFunction(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -5.5,
        "y_max" : 5.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }  
    def construct(self):
        self.setup_axes(animate=True)
        
        graph = self.get_graph(cubic,self.function_color)
        vert_line = self.get_vertical_line_to_graph(2,graph,color=YELLOW) #this might be made to go to graph_obj if you use ReplacementTransform in previous line
        hori_line = self.get_graph(lambda x : 1, color = YELLOW, x_min = 2, x_max = 0) #reversing axes works exactly the way i want here
        hori_line2 = self.get_graph(lambda x : 1, color = YELLOW, x_min = 0, x_max = 2) #reversing axes works exactly the way i want here
        line =Line(self.coords_to_point(2,1),self.coords_to_point(2,0 ),color=YELLOW)
        reflectLine = self.get_graph(lambda x: x,YELLOW)
        cubeRoot = self.get_graph(invCubic,self.function_color)
        self.wait(4)
        self.play(ShowCreation(graph))
        self.play(ShowCreation(vert_line))
        self.wait()
        self.play(ShowCreation(hori_line))
        self.wait(1.5)
        self.play(FadeOut(vert_line),FadeOut(hori_line))
        self.play(ShowCreation(hori_line2))
        self.wait(0.5)
        self.play(ShowCreation(line))
        self.wait()
        self.play(FadeOut(line),FadeOut(hori_line2))
        self.wait(2)
        self.play(ShowCreation(reflectLine))
        self.wait(1)
        self.play(Transform(graph, cubeRoot))
        self.wait(15)


class LinearIsInvertible(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -5.5,
        "y_max" : 5.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        self.setup_axes(animate=False)
        
        graph_object = self.get_graph(hidden_flat_line,self.function_color)
        line_obj = self.get_graph(doubling_line,self.function_color)
        vert_lines = self.get_vertical_lines_from_graph(line_obj,-2.5,2.5,6,color=YELLOW) #this might be made to go to graph_obj if you use ReplacementTransform in previous line
        hori_lines = VGroup(*[
            self.get_graph(lambda y : 2*x, color = YELLOW, x_min = 0, x_max = x)
            for x in np.linspace(-2.5, 2.5, 6)
        ])
        definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto 2x \\end{align*}").move_to(DR*2)
        definitionInj=TextMobject("I. Surjectivity\\\\$\\forall y\\in Y\\exists x\\in X:f(x)=y$").move_to(UP*3+LEFT*3)
        self.play(ShowCreation(graph_object))
        self.play(Transform(graph_object,line_obj),ShowCreation(definition))
        self.wait(5)
        self.play(ShowCreation(hori_lines))
        self.play(ShowCreation(vert_lines))
        self.play(ShowCreation(definitionInj))
        self.wait(6)

class LinearIsBijective(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -5.5,
        "y_max" : 5.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        self.setup_axes(animate=False)
        
        graph_object = self.get_graph(doubling_line,self.function_color)
        line_obj = self.get_graph(doubling_line,self.function_color)
        vert_lines = self.get_vertical_lines_from_graph(line_obj,-2.5,2.5,6,color=YELLOW) #this might be made to go to graph_obj if you use ReplacementTransform in previous line
        hori_line = self.get_graph(lambda x : 4, color = YELLOW, x_min = 2, x_max = 0) #reversing axes works exactly the way i want here
        hori_lines = VGroup(*[
            self.get_graph(lambda y : 2*x, color = YELLOW, x_min = 0, x_max = x)
            for x in np.linspace(-2.5,2.5,6)
        ])
        vertLinesInj= self.get_vertical_lines_to_graph(line_obj,1,2,2,color=YELLOW) #this might be made to go to graph_obj if you use ReplacementTransform in previous line
        horiLinesInj = VGroup(*[
            self.get_graph(lambda y : 2*x, color = YELLOW, x_min = x, x_max = 0)
            for x in np.linspace(1, 2, 2)
        ])
        text = TextMobject("I+II $\\Rightarrow$ Bijective / Invertible").move_to(UL*3+LEFT*0.5)
        definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto 2x \\end{align*}").move_to(DR*2)
        self.add(graph_object,definition)
        self.play(ShowCreation(vertLinesInj))
        self.play(ShowCreation(horiLinesInj))
        self.play(
            FadeOut(vertLinesInj),
            FadeOut(horiLinesInj),
            run_time=0.5
        )

        self.play(ShowCreation(hori_lines))
        self.play(ShowCreation(vert_lines))
        self.play(ShowCreation(text))
        invText = TextMobject("$f^{-1}$").next_to(text,direction=DOWN)
        self.wait(2)
        self.play(ShowCreation(invText))
        self.wait(6)

class LinearIsInjective(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -5.5,
        "y_max" : 5.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        self.setup_axes(animate=False)
        
        graph_object = self.get_graph(hidden_flat_line,self.function_color)
        line_obj = self.get_graph(doubling_line,self.function_color)
        vert_lines = self.get_vertical_lines_to_graph(line_obj,1,2,2,color=YELLOW) #this might be made to go to graph_obj if you use ReplacementTransform in previous line
        hori_lines = VGroup(*[
            self.get_graph(lambda y : 2*x, color = YELLOW, x_min = x, x_max = 0)
            for x in np.linspace(1, 2, 2)
        ])

        definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto 2x \\end{align*}").move_to(DR*2)
        definitionInj=TextMobject("II. Injectivity\\\\\\small{$\\forall x_1,x_2\\in X:f(x_1)=f(x_2)$\\\\ $\\Rightarrow x_1=x_2$}").move_to(UP*3+LEFT*3)
        self.play(ShowCreation(graph_object),run_time=0.5)
        self.play(Transform(graph_object,line_obj),ShowCreation(definition))
        self.play(ShowCreation(vert_lines))
        self.play(ShowCreation(hori_lines))
        self.wait(3.5)
        self.play(ShowCreation(definitionInj))
        self.wait(6)
class ParabolaNotInjective(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -5.5,
        "y_max" : 5.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        self.setup_axes(animate=False)
        graph_object = self.get_graph(hidden_flat_line,self.function_color)
        parabola_obj = self.get_graph(parabola,self.function_color)
        
        #vert_line = self.get_vertical_line_to_graph(2,line_obj,color=YELLOW)
        hori_line_to_right = self.get_graph(lambda x : 4, color = YELLOW, x_min = 2, x_max = 0)
        hori_line_to_left = self.get_graph(lambda x : 4, color = YELLOW, x_min = -2, x_max = 0)
        #vert_line_right = self.get_vertical_line_to_graph(2,sneaky_line_obj)
        
        vertLines = self.get_vertical_lines_to_graph(parabola_obj,-2,2,2,color=YELLOW)
        definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto x^2 \\end{align*}").move_to(DL*2)
        
        self.play(ShowCreation(graph_object))
        self.play(Transform(graph_object,parabola_obj),ShowCreation(definition))
        
        self.play(ShowCreation(vertLines))
        self.play(
            ShowCreation(hori_line_to_left),
            ShowCreation(hori_line_to_right)
        )

        self.wait(6)

class PossibleTypes(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -5.5,
        "y_max" : 5.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        dt=0.3
        self.setup_axes(animate=False)
        cubic = lambda x: 3*((0.5*x)**3-2*(0.5*x))
        graphObj = self.get_graph(lambda x: 0,self.function_color)
        cubicObj = self.get_graph(cubic,self.function_color)

        vert_lines = self.get_vertical_lines_from_graph(cubicObj,-3, 3, 6,color=YELLOW) #this might be made to go to graph_obj if you use ReplacementTransform in previous line


        self.play(ShowCreation(graphObj))
        self.play(Transform(graphObj,cubicObj))
        hori_lines = VGroup(*[
            self.get_graph(lambda y: cubic(x), color = YELLOW, x_min = 0, x_max = x)
            for x in np.linspace(-3, 3, 6)
        ])
        self.play(ShowCreation(hori_lines),ShowCreation(vert_lines),runtime =0.2)

        root1 = (1-5**0.5)
        root2 = (1+5**0.5)
        hori_line_to_right = self.get_graph(lambda x : 3, color = YELLOW, x_min = root2, x_max = 0)
        hori_line_to_left = self.get_graph(lambda x : 3, color = YELLOW, x_min = root1, x_max = 0)
        
        vertLines = self.get_vertical_lines_to_graph(cubicObj,root1,root2,2,color=YELLOW)

        self.play(FadeOut(hori_lines), FadeOut(vert_lines),ShowCreation(vertLines),
            ShowCreation(hori_line_to_left),
            ShowCreation(hori_line_to_right),runtime =dt
        )
        self.wait(dt)

        arctan = lambda x: 2.5*np.arctan(x)
        arctanObj = self.get_graph(arctan, self.function_color)

        self.play(
            FadeOut(hori_line_to_left),
            FadeOut(hori_line_to_right),
            FadeOut(vertLines),
            Transform(graphObj,arctanObj),runtime =dt
        )

        root = np.tan(2/2.5)
        horiRight = self.get_graph(lambda x : 2, color = YELLOW, x_min = root, x_max = 0)
        horiLeft = self.get_graph(lambda x : -2, color = YELLOW, x_min = -root, x_max = 0)
        
        vertLines = self.get_vertical_lines_to_graph(arctanObj,-root,root,2,color=YELLOW)

        self.play(ShowCreation(vertLines),ShowCreation(horiLeft), ShowCreation(horiRight),runtime =dt)
        self.play(FadeOut(horiLeft),FadeOut(horiRight),FadeOut(vertLines),runtime =dt)

        hori_line_to_right = self.get_graph(lambda x : -4, color = YELLOW, x_min = 0, x_max = 7)
        hori_line_to_left = self.get_graph(lambda x : -4, color = YELLOW, x_min = 0, x_max = -7)

        question_marks = TexMobject("???")
        label_coord = self.coords_to_point(4,-5)
        question_marks = question_marks.next_to(label_coord,DR)
        self.play(ShowCreation(hori_line_to_right),ShowCreation(hori_line_to_left),ShowCreation(question_marks),runtime =dt)




        parabolaObj = self.get_graph(lambda x: x**2, self.function_color)
        self.play(FadeOut(question_marks),FadeOut(hori_line_to_left),FadeOut(hori_line_to_right),Transform(graphObj,parabolaObj),runtime =dt)
        hori_line_to_right = self.get_graph(lambda x : -2, color = YELLOW, x_min = 0, x_max = 7)
        hori_line_to_left = self.get_graph(lambda x : -2, color = YELLOW, x_min = 0, x_max = -7)

        horiRight = self.get_graph(lambda x : 4, color = YELLOW, x_min = 2, x_max = 0)
        horiLeft = self.get_graph(lambda x : 4, color = YELLOW, x_min = -2, x_max = 0)
        #vert_line_right = self.get_vertical_line_to_graph(2,sneaky_line_obj)
        
        vertLines = self.get_vertical_lines_to_graph(parabolaObj,-2,2,2,color=YELLOW)
        self.play(
            ShowCreation(hori_line_to_right),ShowCreation(hori_line_to_left),ShowCreation(question_marks.next_to(label_coord,DR + 2.5*UP)),
            ShowCreation(horiRight),ShowCreation(horiLeft),ShowCreation(vertLines),runtime =dt
        )

        self.wait(6)

class ParabolaNotSurjective(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -5.5,
        "y_max" : 5.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        self.setup_axes(animate=False)
        graph_object = self.get_graph(hidden_flat_line,self.function_color)
        parabola_obj = self.get_graph(parabola,self.function_color)
        definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto x^2 \\end{align*}").move_to(DL*2)
        
        hori_line_to_right = self.get_graph(lambda x : -1, color = YELLOW, x_min = 0, x_max = 7)
        hori_line_to_left = self.get_graph(lambda x : -1, color = YELLOW, x_min = 0, x_max = -7)

        question_marks = TexMobject("???")
        label_coord = self.coords_to_point(4,-1)
        question_marks = question_marks.next_to(label_coord,DR)

        self.play(ShowCreation(graph_object))
        self.play(Transform(graph_object,parabola_obj),ShowCreation(definition))
        
        self.wait()
        self.play(ShowCreation(hori_line_to_right),ShowCreation(hori_line_to_left),ShowCreation(question_marks))
        self.wait(2.5)
        self.play(FadeOut(question_marks),FadeOut(hori_line_to_left),FadeOut(hori_line_to_right),FadeOut(definition))
        functions = [lambda x: 4*np.cos(x), lambda x: x**3, lambda x: 5*np.exp(-x**2)]
        funcGraphs = [self.get_graph(f,self.function_color) for f in functions]

        for f in funcGraphs:
            self.play(Transform(graph_object,f))
            self.wait()
        self.wait(4)