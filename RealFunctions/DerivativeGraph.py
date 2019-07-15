from manimlib.imports import *
import numpy as np

def f(x):
    return x**3 - x + 1
def Df(x):
    return 3* x**2 -1


runTime = 6

class TangentMoving(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -11,
        "y_max" : 11,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "tangent_color": YELLOW,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,6,1),
        "center_point" : 0,
        "include_solution" : True
    }   
    def construct(self):
        #self.setup_axes(animate=True)
        self.tangent_moving_along_curve()
        
        
    def get_tangent_line(self, x, graph, color = YELLOW): #function needed for tangent_moving_along_curve
        tangent_line = Line(LEFT, RIGHT, color = color)
        tangent_line.rotate(self.angle_of_tangent(x, graph))
        tangent_line.scale(2)
        tangent_line.move_to(self.input_to_graph_point(x, graph))
        return tangent_line

    def get_tangent_line_change_anim(self, tangent_line, new_x, graph, **kwargs): #function needed for tangent_moving_along_curve
        start_x = self.x_axis.point_to_number(
            tangent_line.get_center()
        )
        def update(tangent_line, alpha):
            
            x = interpolate(start_x, new_x, alpha)
            
            new_line = self.get_tangent_line(
                x, graph, color = tangent_line.get_color()
            )
            tangent_line.become(new_line)
            
            return tangent_line
        
        return UpdateFromAlphaFunc(tangent_line, update, **kwargs)

    def tangent_moving_along_curve(self): #cool animation
        self.setup_axes(animate=False)
        
        solution_graph = self.get_graph(f,self.function_color)
        
        wee_dot = Dot(color=YELLOW)        
        tangent = self.get_tangent_line(-5.5, solution_graph)
        wee_dot.move_to(tangent.get_center())
        
        
        #tangent_line = self.get_tangent_line(-3,solution_graph)
        tangent_change_anim = self.get_tangent_line_change_anim(tangent, 5.5, solution_graph, run_time = runTime)
        
        self.play(FadeIn(solution_graph))
        #self.play(ShowCreation(tangent))
        self.play(tangent_change_anim,MaintainPositionRelativeTo(wee_dot, tangent))
        self.wait(10)

class DerivativeGraphing(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -11,
        "y_max" : 11,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "tangent_color": YELLOW,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,6,1),
        "center_point" : 0,
        "include_solution" : True
    }   
    def construct(self):
        #self.setup_axes(animate=True)
        self.deriv_being_made()

    def deriv_being_made(self): #cool animation
        self.setup_axes(animate=False)
        
        deriv_graph = self.get_graph(Df,self.tangent_color)
        
        wee_dot = Dot()        
        self.wait()
        self.play(MoveAlongPath(wee_dot,deriv_graph.copy()),ShowCreation(deriv_graph),run_time=runTime)
        self.wait(10)