from manimlib.imports import *
import numpy as np
from numpy import sqrt

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
        "center_point" : 0,
    }   
        
    def construct(self):
        self.setup_axes(animate=True)
        #latex isnt fully installed yet
        #exp_cos_definition = TexMobject("\cos\left(e^{-x^2 +2}\right)")
        #label_coord = self.coords_to_point(-3,5)
        #exp_cos_definition = question_marks.next_to(label_coord)
        def getStationary(x,y,isMin=True):
            direction = 0.5*(UP if isMin else DOWN)
            return Vector(direction=direction, color=YELLOW).shift(self.coords_to_point(x,y))
        
        exponential_cos_graph = self.get_graph(exponential_cos,self.function_color) #you're not using this in the end, see list stuff
        
        
        #some illustration to show its even maybe, otherwise v/o
        
        roots = [0.671,1.244,-0.671,-1.244] #actual coords of the points
        roots = [self.coords_to_point(x,0) for x in roots]
        root_dots = [Dot(color=YELLOW).next_to(root,RIGHT*0) for root in roots]
              
        tps = [(-0.92481,-1,True),(-0.40264,1,False),(0,0.4484,True),(0.40264,1,False),(0.92481,-1,True)]
        vectors=[getStationary(tp[0],tp[1],isMin=tp[2]) for tp in tps]
        tps = [self.coords_to_point(tp[0],tp[1]) for tp in tps]
        
        
        tp_points = [Dot(color = YELLOW).next_to(tp,RIGHT*0) for tp in tps]
                
        hori_asymptote= DashedLine(self.coords_to_point(-3, 1), self.coords_to_point(3, 1),color = YELLOW)

        
        

        #all the other intervals around interesting characteristics you can reveal
        #maybe one that just shows the rest of the graph so it doesnt look weird or you miss a gap. also if you want to transform it from there, having a fully stiched together one hiding it the back ground, you can fade that in (while screen doesnt see a difference)
        #then fade out all jigsaw parts and then transform the stiched one, exponential_cos_graph. #also useful to maybe just do a positive one too, so you can illustrate evenness later. idk what to do about showing periodicities
        
        #now you're gonna wanna keep these in separate lists, so you can loop and make sure equally important things get shown at once. loop inside self.play i mean, over showcreaation
        #you can show them at different times here now too. just so you dont have to keep track of where they would be if you collated alll these lists together for some reason
                
        
        self.wait(2)
        
        #self.play(ShowCreation(exp_cos_definition))   
        self.play(ShowCreation(root_dots[0]))
        self.play(ShowCreation(root_dots[1]))
        self.wait(8.5)
        self.play(ShowCreation(root_dots[2]),ShowCreation(root_dots[3]))
        self.wait(3)
        

        
        self.play(
            ShowCreation(tp_points[0]),
            ShowCreation(tp_points[1]),
            ShowCreation(tp_points[2]),
            ShowCreation(tp_points[3]),
            ShowCreation(tp_points[4])
        )

        self.wait(3.5)
        #minima vecs
        self.play(
            ShowCreation(vectors[0]),
            ShowCreation(vectors[2]),
            ShowCreation(vectors[4])
        )
        self.wait(0.5)
        #maxima vecs
        self.play(
            ShowCreation(vectors[1]),
            ShowCreation(vectors[3])
        )
            
        self.wait(5)
        
        rangeX = 1.5
        ctsGraph=self.get_graph(exponential_cos,BLUE,x_min=-rangeX,x_max=rangeX)
        self.play(ShowCreation(ctsGraph),run_time=3)

        self.wait(6)
        self.play(ShowCreation(hori_asymptote))
        negativeAsymptote=self.get_graph(exponential_cos,BLUE,x_min=-rangeX,x_max=-3)
        positiveAsymptote=self.get_graph(exponential_cos,BLUE,x_min=rangeX)
        self.play(ShowCreation(negativeAsymptote),ShowCreation(positiveAsymptote),run_time = 2)
        
        #putting all myobjects together as one VGroup now in order tofade them out at once
        root_dots = VGroup(*root_dots)
        tp_points = VGroup(*tp_points)
        vectors = VGroup(*vectors)
        self.play(FadeOut(root_dots),FadeOut(tp_points),FadeOut(hori_asymptote),FadeOut(vectors))
        self.wait(12)