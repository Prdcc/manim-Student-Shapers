from manimlib.imports import *
import numpy as np


class PlotParabola(GraphScene):
    CONFIG = {
        "x_min" : -4,
        "x_max" : 4,
        "y_min" : -3,
        "y_max" : 3,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : UP*3
    }   
    def construct(self):
        self.setup_axes(animate=True)
        def getParabola(c):
            return lambda x: x**2+c
        startC = -3
        def getRoots(c):
            if c==0:
                return 0,0
            else:
                return -(-c)**0.5,(-c)**0.5

        parabola = self.get_graph(getParabola(startC),BLUE)
        self.play(ShowCreation(parabola))
        roots = getRoots(startC)
        dotLeft=Dot(self.coords_to_point(roots[0],0),color=YELLOW)
        dotRight=Dot(self.coords_to_point(roots[1],0),color=YELLOW)
        self.play(ShowCreation(dotLeft),ShowCreation(dotRight))
        elementsStart = VGroup(parabola,dotLeft,dotRight)
        def update(linesToUpdate, alpha):
            currC = interpolate(startC, 0, alpha)
            
            newParabola = self.get_graph(
                getParabola(currC), color = BLUE
            )
            roots = getRoots(currC)
            newDotLeft=Dot(self.coords_to_point(roots[0],0),color=YELLOW)
            newDotRight=Dot(self.coords_to_point(roots[1],0),color=YELLOW)
            elementsNew = VGroup(newParabola,newDotLeft,newDotRight)
            linesToUpdate.become(elementsNew)
            return linesToUpdate
        
        self.play(UpdateFromAlphaFunc(elementsStart,update),run_time=5)
        self.wait()
        self.play(FadeOut(dotLeft),FadeOut(dotRight))
        self.wait()
        finalC =-startC
        def update2(linesToUpdate, alpha):
            currC = interpolate(0, finalC, alpha)
            
            newParabola = self.get_graph(
                getParabola(currC), color = BLUE
            )
            linesToUpdate.become(newParabola)
            return linesToUpdate
        self.play(UpdateFromAlphaFunc(parabola,update2),run_time=5)
        self.wait(10)


class HigherOrder(GraphScene):
    CONFIG = {
        "x_min" : -4,
        "x_max" : 4,
        "y_min" : -6,
        "y_max" : 6,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : UP*3
    }  
    def construct(self):
        self.setup_axes(animate=False)
        startingCoeff = np.array([1,-5,5,5,-6,-1],dtype=float)
        def getPoly(coeff):
            return lambda x: np.polyval(coeff,x)
        def getDots(coeff,h):
            coeff[-1]-=h
            r = np.roots(coeff)
            roots  = np.sort(r.real[abs(r.imag)<1e-5]) # discard imaginary roots
            nRoots = roots.size
            rootsActual = [roots[i%nRoots] for i in range(5)]
            dots = [Dot(self.coords_to_point(rootsActual[i],h), color=YELLOW) for i in range(5)]

            return VGroup(*dots)

        polynomialGraph = self.get_graph(getPoly(startingCoeff), BLUE)
        rootDots = getDots(startingCoeff,0)

        self.play(ShowCreation(polynomialGraph))
        self.play(ShowCreation(rootDots))

        finalQuadraticTerm = 6
        toUpdate = VGroup(polynomialGraph,rootDots)

        def update(elementsToUpdate, alpha):
            currQuad = interpolate(startingCoeff[3], finalQuadraticTerm, alpha)
            currCoeff = np.copy(startingCoeff)
            currCoeff[3] = currQuad
            newPoly = self.get_graph(
                getPoly(currCoeff), color = BLUE
            )
            roots = getDots(currCoeff,0)
            elementsNew = VGroup(newPoly,roots)
            elementsToUpdate.become(elementsNew)
            return elementsToUpdate
        self.play(UpdateFromAlphaFunc(toUpdate,update),run_time=5)
        self.wait(10)