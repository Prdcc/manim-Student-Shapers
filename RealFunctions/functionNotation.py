from manimlib.imports import *

class TextScene(Scene):
    def construct(self):
        eng_objs = ["\\xrightarrow{function}","Domain","Codomain"]
        math_objs = ["f :","A","B"]
        english_definition = TexMobject("Domain \\,\\, \\xrightarrow{function} Codomain",substrings_to_isolate = eng_objs)
        math_definition = TexMobject("f : A \\xrightarrow{} B}",substrings_to_isolate = math_objs) #objects needed for eng -> maths definitions
        
        arrow = math_definition.get_parts_by_tex("\\xrightarrow{}")
        
        #objects needed for turning X and Y into \mathbb{R}s
        R_1 = math_definition.get_parts_by_tex("A")
        X = TexMobject("\\mathbb{R}").next_to(R_1,RIGHT*0)
        R_2 = math_definition.get_parts_by_tex("B")
        Y = TexMobject("\\mathbb{R}").next_to(R_2,RIGHT*0)   
        
        #the english to maths animation
        self.play(FadeIn(english_definition))
        self.wait(9)
        for eng, math in zip(eng_objs, math_objs):
            for eng_part, math_part in zip(english_definition.get_parts_by_tex(eng),math_definition.get_parts_by_tex(math)):
                self.wait(1)
                self.play(ReplacementTransform(eng_part,math_part))

        self.play(FadeIn(arrow))
        self.wait(9)

        self.play(ReplacementTransform(R_1,X))
        self.play(ReplacementTransform(R_2,Y))
        self.wait(5)

class ProblemsToAnswer(Scene):
    def construct(self):
        q1=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto x^3-x^2\\end{align*}")
        q2=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto e^{-x^2}\\end{align*}")
        q3=TextMobject("\\begin{align*}f:\\mathbb{R}\\setminus\\{0\\}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto \\sin(1/x)\\end{align*}")
        q4=TextMobject("\\begin{align*}f:\\mathbb{R}\\setminus\\{0\\}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto x\\sin(1/x)\\end{align*}")
        q1.next_to(q2,UP*2.5+LEFT*4)
        q2.next_to(q1,DOWN*7)
        q3.next_to(q1,RIGHT*13)
        q4.next_to(q3,DOWN*7)
        self.play(
            ShowCreation(q1),
            ShowCreation(q2),
            ShowCreation(q3),
            ShowCreation(q4)
        )
        self.wait(10)

class ContinuityDef(Scene):
    def construct(self):
        self.wait(4)
        definition=TextMobject("$\\forall x\\in \\mathbb{R}\\,\\forall\\epsilon>0\\,\\exists\\delta>0:|x-y|<\\delta\\Rightarrow|f(x)-f(y)|<\\epsilon$")
        #definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto y \\end{align*}")
        definition.move_to(UP*1)
        self.play(ShowCreation(definition))
        self.wait(15)

class DerivativeDef(Scene):
    def construct(self):
        definition=TextMobject("$f'(x)=\\lim_{h\\rightarrow 0}\\frac{f(x+h)-f(x)}{h}$")
        definition.move_to(UP*1)
        self.play(ShowCreation(definition))
        self.wait(15)

class FunctionDef(Scene):
    def construct(self):
        definition=TextMobject("\\begin{align*}f:\\mathbb{R}&\\rightarrow\\mathbb{R}\\\\x&\\mapsto \\cos(e^{-x^2+2})\\end{align*}", color=BLACK)
        definition.move_to(UP*1)
        self.add(definition)
        self.wait(15)
        
 