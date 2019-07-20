from manimlib.imports import *
import numpy as np

class SumODE(GraphScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 6,
        "y_min" : -2,
        "y_max" : 2,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : UP*3
    }  
    def construct(self):
        self.setup_axes(animate=False)
        def getF(a):
            return lambda x: np.sin(x)+a*(np.exp(0.2*x)-(0.3*x)**2)
        def getFSecond(a):
            return lambda x: -np.sin(x)+a*(0.04*np.exp(0.2*x)-0.6)
        def getSum(a):
            return lambda x: getF(a)(x)+getFSecond(a)(x)

        startA = -1.3
        f = self.get_graph(getF(startA),BLUE)
        labelF = self.get_graph_label(f,label="f",color=BLUE)
        fSecond = self.get_graph(getFSecond(startA),RED)
        labelFSecond = self.get_graph_label(fSecond,label="f''",color=RED)
        fSum = self.get_graph(getSum(startA),YELLOW)
        labelFSum = self.get_graph_label(fSum,label="f+f''",color=YELLOW)

        functions = VGroup(f,labelF,fSecond,labelFSecond,fSum,labelFSum)

        self.play(
            ShowCreation(functions),
            run_time=3
        )
        
        def update(fs,alpha):
            currA = interpolate(startA,0,alpha)
            fNew = self.get_graph(getF(currA),BLUE)
            labelFNew = self.get_graph_label(fNew,label="f",color=BLUE)
            fSecondNew = self.get_graph(getFSecond(currA),RED)
            labelFSecondNew = self.get_graph_label(fSecondNew,label="f''",color=RED)
            fSumNew = self.get_graph(getSum(currA),YELLOW)
            labelFSumNew = self.get_graph_label(fSumNew,label="f+f''",color=YELLOW)
            newFunctions = VGroup(fNew,labelFNew,fSecondNew,labelFSecondNew,fSumNew,labelFSumNew)
            fs.become(newFunctions)
            return fs

        self.play(
            UpdateFromAlphaFunc(functions,update),
            run_time = 5
        )

        self.wait(10)
        