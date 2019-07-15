from manimlib.imports import *
import numpy as np

class CosPeriodic(GraphScene):
    CONFIG = {
        "x_min" : -TAU,
        "x_max" : TAU,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
    }   
    def construct(self):
        def cosTrans(x0):
            return self.get_graph(lambda x: np.cos(x-x0),color=BLUE)
        
        
        self.setup_axes(animate=True)
        cosFlipped = self.get_graph(lambda x: np.cos(x), color=BLUE, x_min=TAU,x_max=-TAU)
        cosObj = cosTrans(0)
        cosLeft = self.get_graph(np.cos,x_max=0)
        cosRight = self.get_graph(np.cos,x_min = 0)
        dot1 = Dot(color = YELLOW)
        dot2 = Dot(color = YELLOW)
        periodicDef = TextMobject("Periodic \\\\$\\exists k>0:\\forall x, f(x)=f(x+k)$").next_to(cosLeft, UR*1)
        self.play(ShowCreation(cosObj))
        self.wait(4)
        self.play(MoveAlongPath(dot1,cosLeft),MoveAlongPath(dot2,cosRight), run_time =3)
        self.play(ShowCreation(periodicDef))
        

        self.wait(2)        #reflect cosine
        evenDef = TextMobject("Even \\\\$\\forall x, f(x)=f(-x)$").next_to(cosLeft, UR*1)
        self.play(FadeOut(dot1),FadeOut(dot2))
        self.play(Transform(cosObj,cosFlipped))
        self.play(Transform(periodicDef,evenDef))
        self.wait(9)
        sinObj = self.get_graph(np.sin, self.function_color)

        self.play(Transform(cosObj,sinObj))     #Transform to sin
        self.wait(2.5)
        oddDef = TextMobject("Odd \\\\$\\forall x, f(x)=-f(-x)$").next_to(cosLeft, UR*1)
        
        self.play(Rotate(cosObj,180*DEGREES,about_point=OUT),run_time=2)    #Rotate sin
        self.play(Transform(periodicDef,oddDef))
        self.wait(10)
    
class RotateFunction2(Scene):
    def construct(self):
        dot_center=Dot()
        dot_below=Dot(color=RED).next_to(dot_center,DOWN*3)
 
        self.add(dot_center,dot_below)
        self.play(Rotate(dot_below,360*DEGREES,about_point=dot_center.get_center()),run_time=10)
        self.wait()