from manimlib.imports import *
import numpy as np

class Spring(Line):
    CONFIG = {
        "loopiness" : 5,
        "loop_radius" : 0.3,
        "color" : GREY
    }

    def generate_points(self):
        ## self.start, self.end
        length = get_norm(self.end-self.start)
        angle = angle_of_vector(self.end-self.start)
        micro_radius = self.loop_radius/length
        m = 2*np.pi*(self.loopiness+0.5)
        scaleFactor = length/(1+2*micro_radius)
        def loop(t):
            return micro_radius*(
                RIGHT + np.cos(m*t)*LEFT + np.sin(m*t)*UP
            )
        #new_epsilon = self.epsilon

        self.set_points_smoothly([
            t*RIGHT + loop(t)
            for t in np.arange(-1, 1, 0.1/(m*micro_radius)/length)
        ])
        self.scale(length/(1+2*micro_radius))
        self.rotate(angle)
        self.shift(self.start)

class OscillatingSpring(Scene):
    def construct(self):
        amplitude = 4
        def getCentrePos(t):
            return amplitude*RIGHT*np.sin(t)+RIGHT*2
        def getSquare(t):
            return Square(side_length=1).move_to(getCentrePos(t))
        def getForce(t):
            return Vector(direction=-amplitude*RIGHT*np.sin(t)/3,color=YELLOW).shift(getCentrePos(t))
        def getSpring(t):
            return Spring(start=getCentrePos(t)*0.53+LEFT*3,end=getCentrePos(t)*1.04+RIGHT*0.2)
            #return Spring(start=LEFT*4,end=getCentrePos(t))
        def getDot(t):
            return Dot(getCentrePos(t),color=YELLOW)
        mass = getSquare(0)
        forceVector = getForce(0)
        spring = getSpring(0)
        dot = getDot(0)
        elementsToUpdate = VGroup(*[mass,spring,dot,forceVector])
        t = 0
        dt = 0.1
        def update(elements):
            nonlocal t
            t += dt
            newSquare = getSquare(t)
            newForce = getForce(t)
            newSpring = getSpring(t)
            newDot = getDot(t)
            newElements = VGroup(*[newSquare,newSpring,newDot,newForce])
            elements.become(newElements)
            return elements
        
        self.play(ShowCreation(elementsToUpdate))
        self.wait()
        self.play(UpdateFromFunc(elementsToUpdate, update),run_time=24)
        self.wait(5)

