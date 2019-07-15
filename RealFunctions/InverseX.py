from manimlib.imports import *
import numpy as np

class Asymptotes(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -11,
        "y_max" : 11,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "center_point" : 0
    }   

    def construct(self):
        self.setup_axes(animate=True)
        leftSide = self.get_graph(lambda x: 1/x, BLUE, x_min=-3, x_max =-0.3)
        rightSide = self.get_graph(lambda x: 1/x, BLUE, x_min=3, x_max =0.3)
        leftSideAs = self.get_graph(lambda x: 1/x, BLUE, x_min=-0.3, x_max =-0.05)
        rightSideAs = self.get_graph(lambda x: 1/x, BLUE, x_min=0.3, x_max =0.05)
        leftSideAsInf = self.get_graph(lambda x: 1/x, BLUE, x_min=-3, x_max =-10)
        rightSideAsInf = self.get_graph(lambda x: 1/x, BLUE, x_min=3, x_max =10)
        text = TexMobject("Asymptote").move_to(LEFT*3+UP)
        definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto \\frac 1x \\end{align*}").move_to(DOWN*1.7+RIGHT*3)

        horiAsymptote = DashedLine(self.coords_to_point(-10,0), self.coords_to_point(10,0),color = WHITE)
        vertAsymptote = DashedLine(self.coords_to_point(0,-20), self.coords_to_point(0,20),color = WHITE)
        self.wait()
        self.play(ShowCreation(leftSide), ShowCreation(rightSide),ShowCreation(definition))
        self.wait()
        self.play(ShowCreation(vertAsymptote),run_time=0.5)
        self.play(ShowCreation(leftSideAs), ShowCreation(rightSideAs),run_time=3.5)
        self.wait(6)
        self.play(ShowCreation(text))
        self.wait(5.5)
        self.play(ShowCreation(horiAsymptote),run_time=0.5)
        self.play(ShowCreation(leftSideAsInf), ShowCreation(rightSideAsInf),run_time=2)
        self.wait()

        hyperbola = Mobject()
        hyperbola.add(rightSide,rightSideAs,rightSideAsInf)
        definitionHype=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto \\sqrt{1+x^2} \\end{align*}").move_to(DOWN*1.7+RIGHT*3.8)
        self.play(
            FadeOut(leftSide),
            FadeOut(leftSideAs),
            FadeOut(leftSideAsInf),
            Rotate(horiAsymptote, PI/4,about_point=OUT),
            Rotate(hyperbola, PI/4,about_point=OUT),
            Rotate(vertAsymptote, PI/4,about_point=OUT),
            Transform(definition, definitionHype)
        )

        self.wait(6)