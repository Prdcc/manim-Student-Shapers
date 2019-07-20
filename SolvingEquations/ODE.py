from manimlib.imports import *
import numpy as np

class ODEField(GraphScene):
    CONFIG = {
        "x_min" : -4.5,
        "x_max" : 4.5,
        "y_min" : -3,
        "y_max" : 3,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0,
    }
    def construct(self):
        self.setup_axes(animate=False)
        def getField(xPos,yPos):
            magnitude = 0.5
            derivative = yPos-xPos
            angle = np.arctan(derivative)
            y = np.sin(angle)
            x = np.cos(angle)
            
            return magnitude*(RIGHT*x + UP*y)


        vectors = [Vector(getField(x,y), color = YELLOW).shift(RIGHT*x+UP*y)
        for x in np.arange(-10,10,1)
        for y in np.arange(-9,9,1)
        ] #List of vectors pointing to each grid point
        
        
        draw_field = VGroup(*vectors) #Pass list of vectors to create a VGroup
        
        self.play(ShowCreation(draw_field)) #Draw VGroup on screen
        self.wait(2)
        minX = -10
        maxX=10
        def solution(c):
            return lambda x: c*np.exp(x)+x+1

        def getUpdateFunction(startValue, endValue, f):

            def update(graph, alpha):
                currValue = interpolate(startValue, endValue, alpha)
                newGraph = self.get_graph(f(currValue),graph.color,x_max=maxX,x_min = minX)
                graph.become(newGraph)
                return graph
            
            return update
        fGraph = self.get_graph(solution(-1),BLUE,x_max=maxX,x_min = minX)
        self.play(ShowCreation(fGraph))
        self.play(UpdateFromAlphaFunc(fGraph,getUpdateFunction(-1,2,solution)),run_time=10)
        self.wait(3)
        dot = Dot(self.coords_to_point(0,1.25), color=YELLOW)
        self.play(ShowCreation(dot))
        self.play(UpdateFromAlphaFunc(fGraph,getUpdateFunction(2,0.25,solution)),run_time=3)
        #self.play(ShowCreation(exponential),run_time=4)
        self.wait(10)

class ConstantDerivativeV2(GraphScene):
    CONFIG = {
        "x_min" : -4.5,
        "x_max" : 4.5,
        "y_min" : -3,
        "y_max" : 3,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0,
    }
    def construct(self):
        self.setup_axes(animate=False)
        b=0.4
        def getField(xPos,yPos):
            magnitude = 0.5
            derivative = b
            angle = np.arctan(derivative)
            y = np.sin(angle)
            x = np.cos(angle)
            
            return magnitude*(RIGHT*x + UP*y)


        vectors = [Vector(getField(x,y), color = YELLOW).shift(RIGHT*x+UP*y)
        for x in np.arange(-10,10,1)
        for y in np.arange(-9,9,1)
        ] #List of vectors pointing to each grid point
        
        
        draw_field = VGroup(*vectors) #Pass list of vectors to create a VGroup
        
        self.play(ShowCreation(draw_field)) #Draw VGroup on screen
        self.wait(2)
        minX = -10
        maxX=10
        def solution(c):
            return lambda x: b*x+c
        def getLineGraph(c):
            return self.get_graph(solution(c),BLUE,x_max=maxX,x_min = minX)
        correctLine = getLineGraph(-1)
        lines = VGroup(*[getLineGraph(c) for c in np.arange(-5,5,0.5)])
        self.play(ShowCreation(correctLine), ShowCreation(lines))
        self.wait(3)
        dot = Dot(self.coords_to_point(0,-1), color=YELLOW)
        self.play(ShowCreation(dot))
        self.play(FadeOut(lines))
        #self.play(ShowCreation(exponential),run_time=4)
        self.wait(10)

class ConstantDerivative(GraphScene):
    CONFIG = {
        "x_min" : -4.5,
        "x_max" : 4.5,
        "y_min" : -3,
        "y_max" : 3,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0,
    }
    def construct(self):
        self.setup_axes(animate=False)
        b=0.4
        def getField(xPos,yPos):
            magnitude = 0.5
            derivative = b
            angle = np.arctan(derivative)
            y = np.sin(angle)
            x = np.cos(angle)
            
            return magnitude*(RIGHT*x + UP*y)


        vectors = [Vector(getField(x,y), color = YELLOW).shift(RIGHT*x+UP*y)
        for x in np.arange(-10,10,1)
        for y in np.arange(-9,9,1)
        ] #List of vectors pointing to each grid point
        
        
        draw_field = VGroup(*vectors) #Pass list of vectors to create a VGroup
        
        self.play(ShowCreation(draw_field)) #Draw VGroup on screen
        self.wait(2)
        minX = -10
        maxX=10
        def solution(c):
            return lambda x: b*x+c

        def getUpdateFunction(startValue, endValue, f):

            def update(graph, alpha):
                currValue = interpolate(startValue, endValue, alpha)
                newGraph = self.get_graph(f(currValue),graph.color,x_max=maxX,x_min = minX)
                graph.become(newGraph)
                return graph
            
            return update
        fGraph = self.get_graph(solution(-1),BLUE,x_max=maxX,x_min = minX)
        self.play(ShowCreation(fGraph))
        self.play(UpdateFromAlphaFunc(fGraph,getUpdateFunction(-1,2,solution)),run_time=10)
        self.wait(3)
        dot = Dot(self.coords_to_point(0,1.25), color=YELLOW)
        self.play(ShowCreation(dot))
        self.play(UpdateFromAlphaFunc(fGraph,getUpdateFunction(2,0.25,solution)),run_time=3)
        #self.play(ShowCreation(exponential),run_time=4)
        self.wait(10)