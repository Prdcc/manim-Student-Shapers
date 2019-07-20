from manimlib.imports import *
import numpy as np
from math import erf

class PlotGraphs(GraphScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 6,
        "y_min" : -2.5,
        "y_max" : 2.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0
    }   
    def construct(self):
        erfInt = lambda x: erf(x)+0.5*PI**0.5+0.11
        self.setup_axes(animate=True)
        derivative = lambda x: -2*x*np.exp(-x**2)
        exponential = lambda x: np.exp(-x**2)
        derivativeObj = self.get_graph(derivative,self.function_color,x_min=-6,x_max=6)
        erfObj = self.get_graph(erfInt,YELLOW,x_min=-6,x_max=6)
        expObj = self.get_graph(exponential,WHITE,x_min=-6,x_max=6)
        labelExp = self.get_graph_label(expObj, label = "B", direction= UP*0.55+LEFT*0.15)
        labelDer = self.get_graph_label(derivativeObj, label = "A", direction= DOWN*0.55+LEFT*0.15)
        labelErf = self.get_graph_label(erfObj, label = "C")

        expComp = Mobject().add(expObj,labelExp)
        erfComp = Mobject().add(erfObj,labelErf)
        derComp = Mobject().add(derivativeObj,labelDer)

        self.wait(2)
        self.play(ShowCreation(derComp),ShowCreation(expComp),ShowCreation(erfComp),
            run_time=2
        )
        self.wait(12)

        opacity=0.3
        derivativeFaded = self.get_graph(derivative,self.function_color,stroke_opacity = opacity)
        erfFaded = self.get_graph(erfInt,YELLOW,stroke_opacity = opacity)
        expFaded = self.get_graph(exponential,WHITE,stroke_opacity = opacity)
        self.add(derivativeFaded, erfFaded, expFaded)       #add faded underneath
        def getDot(x, y):
            return Dot(self.coords_to_point(x,y),color=ORANGE)
        def getPath(func,minX,maxX):
            return self.get_graph(func,x_min=minX,x_max=maxX)


        self.play(
            FadeOut(expComp),
            FadeOut(derComp)
        )
        self.wait()
        maximumExp = Dot(self.coords_to_point(0,1),color=ORANGE)
        self.play(
            FadeIn(expComp),
            FadeIn(maximumExp),
            FadeOut(erfComp)
        )
        self.wait()
        derMaxVal =  0.5**0.5
        maxDer = Dot(self.coords_to_point(-derMaxVal,derivative(-derMaxVal)),color=ORANGE)
        minDer = Dot(self.coords_to_point(derMaxVal,derivative(derMaxVal)),color=ORANGE)
        self.play(
            FadeOut(maximumExp),
            FadeIn(derComp),
            FadeOut(expComp),
            FadeIn(maxDer),
            FadeIn(minDer)
        )
        self.wait(2)
        origin = getDot(0,0)
        self.play(
            FadeOut(maxDer),
            FadeOut(minDer),
            FadeIn(origin)
        )
        self.wait(3)
        self.play(
            FadeOut(origin),
            FadeOut(derComp),
            FadeIn(expComp),
            FadeIn(maximumExp)
        )
        self.wait(6)
        self.play(
            FadeOut(maximumExp),
            FadeIn(derComp)
        )

        travDotDer = getDot(0,0)
        travDotExp = getDot(0,0)
        smallValuesDer = getPath(derivative,-6,-1.5)
        smallValuesExp = getPath(exponential,-6,-1.5)
        self.play(
            MoveAlongPath(travDotDer,smallValuesDer),
            MoveAlongPath(travDotExp,smallValuesExp),
            run_time=2
        )
        self.wait()

        midValuesDer = getPath(derivative,-1.5,1.5)
        midValuesExp = getPath(exponential,-1.5,1.5)
        self.play(
            MoveAlongPath(travDotDer,midValuesDer),
            MoveAlongPath(travDotExp,midValuesExp),
            run_time=6
        )
        
        self.play(
            FadeOut(travDotDer),
            FadeOut(travDotExp)
        )
        self.wait(2)



        self.play(
            FadeOut(derComp),
            FadeIn(erfComp)
        )
        self.wait(4)

        travDotErf = getDot(0,0)
        midValuesErf = getPath(erfInt,-1.5,1.5)
        self.play(
            MoveAlongPath(travDotErf,midValuesErf),
            MoveAlongPath(travDotExp,midValuesExp),
            run_time=2
        )

        self.wait(9)
        BIGValuesErf = getPath(erfInt,1.5,6)
        BIGValuesExp = getPath(exponential,1.5,6)
        self.play(
            MoveAlongPath(travDotErf,BIGValuesErf),
            MoveAlongPath(travDotExp,BIGValuesExp),
            run_time=8
        )

        self.wait(15)


class PlotDer(GraphScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 6,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    def construct(self):
        self.setup_axes(animate=False)
        func = lambda x: -2*x*np.exp(-x**2)
        graphObj = self.get_graph(func, BLUE)
        graph_lab = self.get_graph_label(graphObj, label = "A",color=WHITE)
        self.play(ShowCreation(graphObj), ShowCreation(graph_lab))
        self.wait(4)

class PlotExp(GraphScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 6,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    def construct(self):
        self.setup_axes(animate=False)
        func = lambda x: np.exp(-x**2)
        graphObj = self.get_graph(func, BLUE)
        graph_lab = self.get_graph_label(graphObj, label = "B",color=WHITE)
        self.play(ShowCreation(graphObj), ShowCreation(graph_lab))
        self.wait(4)

class PlotInt(GraphScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 6,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    def construct(self):
        self.setup_axes(animate=False)
        func = erf
        graphObj = self.get_graph(func, BLUE)
        graph_lab = self.get_graph_label(graphObj, label = "C",color=WHITE)
        self.play(ShowCreation(graphObj), ShowCreation(graph_lab))
        self.wait(4)

class PlotExercise(GraphScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 6,
        "y_min" : -2.5,
        "y_max" : 2.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0
    }   
    def construct(self):
        erfInt = lambda x:  1.53846* np.exp(0.2*x)* (1.5*np.sin(0.3*x) + np.cos(0.3*x))-2
        self.setup_axes(animate=False)
        derivative = lambda x: np.exp(0.2*x)*(0.2*np.cos(0.3*x) - 0.3*np.sin(0.3*x))
        exponential = lambda x: np.exp(0.2*x)*np.cos(0.3*x)
        derivativeObj = self.get_graph(derivative,self.function_color,x_min=-6,x_max=6)
        erfObj = self.get_graph(erfInt,YELLOW,x_min=-6,x_max=6)
        expObj = self.get_graph(exponential,WHITE,x_min=-6,x_max=6)
        labelExp = self.get_graph_label(expObj, label = "B")
        labelDer = self.get_graph_label(derivativeObj, label = "A")
        labelErf = self.get_graph_label(erfObj, label = "C")

        expComp = Mobject().add(expObj,labelExp)
        erfComp = Mobject().add(erfObj,labelErf)
        derComp = Mobject().add(derivativeObj,labelDer)

        self.play(ShowCreation(derComp),ShowCreation(expComp),ShowCreation(erfComp),
            run_time=2
        )
        self.wait(12)