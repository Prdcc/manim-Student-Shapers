from manimlib.imports import *

NEW_BLUE = "#68a8e1"

class Riemann(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
        "axes_color" : GREEN,
    }

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=False)
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        graph = self.get_graph(func,x_min=-1,x_max=11)
        graph.set_color(BLUE)
        
        self.graph=graph
        iteraciones=6

        self.rect_list = self.get_riemann_rectangles_list(
            graph, iteraciones,start_color=PURPLE,end_color=ORANGE,x_min = 0.75,x_max=9.5
        )
        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x : 0,x_max=11,x_min=1.5), dx = 0.5,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),
            x_min = 0.75,x_max=9.5
        )
        rects = self.rect_list[0]

        self.play(ShowCreation(graph))
        self.transform_between_riemann_rects(
            flat_rects, rects, 
            replace_mobject_with_target_in_scene = True,
            run_time=0.9
        )
        self.wait(8)

class PlotMaxMin(GraphScene):
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
        self.setup_axes(animate=True)
        function = lambda x: x**3/3+x**2/2-2*x

        funcGraph = self.get_graph(function, self.function_color)
        self.play(ShowCreation(funcGraph))

        lineMax = self.get_graph(lambda x:10/3, YELLOW, x_min=-3.5, x_max=-0.5)
        dotMax = Dot(self.coords_to_point(-2,10/3),color=YELLOW)
        lineMin = self.get_graph(lambda x:-7/6, YELLOW, x_min=-0.5, x_max=2.5)
        dotMin = Dot(self.coords_to_point(1,-7/6),color=YELLOW)

        self.play(ShowCreation(dotMin),ShowCreation(dotMax))
        self.wait(1)
        self.play(ShowCreation(lineMax),ShowCreation(lineMin))
        self.wait(1.5)

        vectorMax = Vector(direction=DOWN,color=YELLOW).shift(self.coords_to_point(-2,10/3))
        vectorMin = Vector(direction=UP,color=YELLOW).shift(self.coords_to_point(1,-7/6))
        self.play(ShowCreation(vectorMax))
        self.play(ShowCreation(vectorMin))
        arcMax = self.get_graph(function, YELLOW, x_min= -2.8,x_max=-1)
        arcMin = self.get_graph(function, YELLOW, x_min= 0.2,x_max=1.65)
        self.wait(7)
        self.play(ShowCreation(arcMin))
        self.wait(1.75)
        self.play(ShowCreation(arcMax))

        self.wait(8)


class SecantTangent(GraphScene):
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
        definition=TextMobject("\\small$$f'(x)=\\lim_{h\\rightarrow 0}\\frac{f(x+h)-f(x)}{h}$$")
        definition.move_to(UP*1)
        def getDot(x,y):
            return Dot(self.coords_to_point(x,y),color=YELLOW)

        def getPath(startX,startY,endX,endY):
            return Line(start=self.coords_to_point(startX,startY),end=self.coords_to_point(endX,endY),color=YELLOW)
        
        self.wait(3)
        self.play(ShowCreation(definition))
        self.wait(1)
        self.play(Transform(definition,definition.copy().move_to(RIGHT*3.5+DOWN*1.5)),run_time=1)
        self.setup_axes(animate=False)
        square = lambda x: x**2

        parabola = self.get_graph(square,BLUE)
        h=1.5
        startX=1
        pointX = getDot(startX,0)
        pointXH = getDot(startX,0)
        labelH = TextMobject("$h$")
        
        hSegment = getPath(startX,0,startX+h,0)
        labelH = TextMobject("$h$").next_to(hSegment,direction=DOWN*0.45)
        hSegmentComp = Mobject()
        hSegmentComp.add(hSegment,labelH)
        self.play(ShowCreation(parabola))
        self.play(ShowCreation(pointX))
        self.wait()
        self.play(MoveAlongPath(pointXH,hSegment),ShowCreation(hSegmentComp))
        
        xPathUp=getPath(startX,0,startX,square(startX))
        xhPathUp=getPath(startX+h,0,startX+h,square(startX+h))
        deltaFSegment=getPath(startX+h,square(startX),startX+h,square(startX+h))
        deltaFLabel = TextMobject("$f(x+h)-f(x)$").next_to(deltaFSegment,direction=RIGHT*0.5)
        deltaFComp = Mobject()
        deltaFComp.add(deltaFSegment,deltaFLabel)
        hSegmentPathUp=getPath(startX+h/2,0,startX+h/2,square(startX))

        self.wait()
        self.play(
            MoveAlongPath(pointX,xPathUp),
            MoveAlongPath(pointXH,xhPathUp),
            MoveAlongPath(hSegment,hSegmentPathUp),
            MaintainPositionRelativeTo(labelH,hSegment)
        )
        self.play(ShowCreation(deltaFComp))
        
        def getSecantEquation(x,h):
                m = (square(x+h)-square(x))/h
                return lambda y: m*(y-x)+square(x)
        
        secant = self.get_graph(getSecantEquation(startX,h),YELLOW)
        self.play(ShowCreation(secant))
        self.wait(4)
        linesStart = VGroup(*[secant,hSegment,deltaFSegment,pointXH])
        newH = 0.1
        def update(linesToUpdate, alpha):
            currH = interpolate(h, newH, alpha)
            
            newSecant = self.get_graph(
                getSecantEquation(startX,currH), color = YELLOW
            )
            newHSegment = getPath(startX,square(startX),startX+currH,square(startX))
            newDeltaFSegment = getPath(startX+currH,square(startX),startX+currH,square(startX+currH))
            newPoint = getDot(startX+currH,square(startX+currH))
            newLines = VGroup(*[newSecant,newHSegment,newDeltaFSegment,newPoint])
            linesToUpdate.become(newLines)
            return linesToUpdate
        
        self.play(
            UpdateFromAlphaFunc(linesStart, update),
            MaintainPositionRelativeTo(labelH,hSegment),
            MaintainPositionRelativeTo(deltaFLabel,deltaFSegment),
            run_time=3
        )

        self.wait(15)