from manimlib.imports import *
import numpy as np
from numpy import sqrt

def sin_graph(x):
    return np.sin(x)
def parabola_graph(x):
    return x*x
#    circle shape should also be here
def exponential_cos_graph(x):
    return np.cos(np.exp(-0.1 * x**2 + 2))
def cubed(x):
    return x**3
def quartic(x):
    return x**4
def one_over_x(x):
    return 1/x
def positive_sigmoid(x):
    return 1/(1+np.exp(x)) - 0.5
def negative_sigmoid(x):
    return 1/(1+np.exp(-x)) - 0.5 
def just_a_line(x):
    return 0.5*x
def hidden_flat_line(x):
    return 0
def three(x):
    return 3
def two(x):
    return 2
def positive_circle(x):
    sqrt(1-x**2)
def positive_circle(x):
    -sqrt(1-x**2)

class PlotSinInv(GraphScene):
    CONFIG = {
        "x_min" : -1,
        "x_max" : 1,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0,
        "funcs" : [sin_graph,parabola_graph, exponential_cos_graph,just_a_line]#,cubed,quartic]
    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.sinInv,x_max=(-0.01))
        func_graphR=self.get_graph(self.sinInv,x_min=(0.01),color=BLUE)
 
        self.play(ShowCreation(func_graph),ShowCreation(func_graphR),run_time=1.5)
        self.wait(4)
    def sinInv(self,x):
        return np.sin(1/x)



class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
        "center_point" : 0,
        "funcs" : [sin_graph,parabola_graph, exponential_cos_graph,just_a_line]#,cubed,quartic]
    }   
        
    def construct(self):
        self.setup_axes(animate=True)
        
        circle = Circle(color =BLUE)
        
        func_graphs = [self.get_graph(f,self.function_color) for f in self.funcs]
        func_graphs.insert(4,circle)
        #all_my_shapes = func_graphs
        #func_graphs = func_graphs.append(circle)
        
        graph_object = self.get_graph(sin_graph,self.function_color) #change this if you start with something else
        hidden_line = self.get_graph(hidden_flat_line,self.function_color)
        
        positive_sigmoid_graph = self.get_graph(positive_sigmoid,self.function_color)
        negative_sigmoid_graph = self.get_graph(negative_sigmoid,self.function_color)
        
        positive_one_over_x = self.get_graph(lambda x : 1/x, color = BLUE, x_min = 0.1, x_max = 10)
        negative_one_over_x = self.get_graph(lambda x : 1/x, color = BLUE, x_min = -10, x_max = -0.1)
        dt=0.2
        self.play(ShowCreation(graph_object))
        self.wait(dt)
    
        for i in range(1,len(func_graphs)):#this is a bit messed up, try to make graph_object a flat line first
            self.play(Transform(graph_object, func_graphs[i]),run_time = 1.5)
            self.wait(dt)
        
        self.play(ShowCreation(hidden_line),Transform(graph_object, positive_sigmoid_graph),Transform(hidden_line, negative_sigmoid_graph),run_time =1.5)
        self.wait(dt)
        self.play(Transform(graph_object,positive_one_over_x),Transform(hidden_line,negative_one_over_x))
        self.play(FadeOut(hidden_line, run_time = 1)) #double sigmoid graph
        
        self.play(Transform(graph_object, func_graphs[0],runtime = 1.5)) #make the animation loopr
        self.wait(6)
#tk you wanted to include the indicator function for the rationals
    

class DoubleSigmoidNotFunction(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -5,
        "y_max" : 5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0,
    }   
        
    def construct(self):
        self.setup_axes(animate=False)
        positivePar = lambda x: sqrt(x+10)
        negativePar = lambda x: -sqrt(x+10)
        negative_sigmoid_graph = self.get_graph(negativePar,self.function_color)
        positive_sigmoid_graph = self.get_graph(positivePar,self.function_color)
        
        vert_line_pos = self.get_vertical_line_to_graph(2,positive_sigmoid_graph,color=YELLOW)
        vert_line_neg = self.get_vertical_line_to_graph(2,negative_sigmoid_graph,color=YELLOW) #if you want to make it nice, add a ball that'll go to the graph, will visualise the fuckedupedness of multifunctions
        
        self.play(ShowCreation(negative_sigmoid_graph),ShowCreation(positive_sigmoid_graph))
        self.wait()
        self.play(ShowCreation(vert_line_pos))
        self.play(ShowCreation(vert_line_neg))
        self.wait(10)

class EmptyFunctionNotFunction(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0,
    }   
        
    def construct(self):
        self.setup_axes(animate=False)
        
        hori_line_three = self.get_graph(lambda x : 0.5, color = BLUE, x_min = -10, x_max = 0)
        hori_line_two = self.get_graph(lambda x : 1, color = BLUE, x_min = 2, x_max = 10)

        vert_line_three = self.get_vertical_line_to_graph(-5,hori_line_three,color=YELLOW)
        vert_line_two = self.get_vertical_line_to_graph(4,hori_line_two,color=YELLOW)#if you want to make it nice, add a ball that'll go to the graph, will visualise the fuckedupedness of multifunctions
        vert_line_doesnt_work = self.get_vertical_line_to_graph(1,self.get_graph(lambda x: 2), color=YELLOW)
        
        question_marks = TexMobject("???")
        label_coord = self.coords_to_point(1,0)
        question_marks = question_marks.next_to(label_coord,RIGHT+ UP)
        
        self.play(ShowCreation(hori_line_three),ShowCreation(hori_line_two))
        self.wait()
        self.play(ShowCreation(vert_line_three),ShowCreation(vert_line_two),ShowCreation(vert_line_doesnt_work),ShowCreation(question_marks),run_time=1)
        self.wait(10)
#tk do the circle one and the rescreen showing all three graphs

class CircleNotFunction(GraphScene):
    CONFIG = {
        "x_min" : -3.5,
        "x_max" : 3.5,
        "y_min" : -2.5,
        "y_max" : 2.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0,
    }   
        
    def construct(self):
        self.setup_axes(animate=False)
        
        positive_circ_graph = self.get_graph(lambda x : sqrt(1-x**2), color = BLUE, x_min = -1, x_max = 1)
        negative_circ_graph = self.get_graph(lambda x : -sqrt(1-x**2), color = BLUE, x_min = -1, x_max = 1)
        
        vert_line_pos_circ = self.get_vertical_line_to_graph(1/sqrt(2),positive_circ_graph,color=YELLOW)
        vert_line_neg_circ = self.get_vertical_line_to_graph(1/sqrt(2),negative_circ_graph,color=YELLOW) #if you want to make it nice, add a ball that'll go to the graph, will visualise the fuckedupedness of multifunctions
        
        vert_line_doesnt_work_circ = self.get_vertical_line_to_graph(2,self.get_graph(lambda x: 2), color=YELLOW)
        
        question_marks = TexMobject("???")
        label_coord = self.coords_to_point(2,0)
        question_marks = question_marks.next_to(label_coord,RIGHT+ UP)
        
        
        self.play(ShowCreation(negative_circ_graph),ShowCreation(positive_circ_graph))
        self.wait()
        self.play(ShowCreation(vert_line_pos_circ),ShowCreation(vert_line_neg_circ),ShowCreation(vert_line_doesnt_work_circ),ShowCreation(question_marks))
        self.wait(10)