from manim import * #manim -pql scene.py -a

class Matrixreflection(MovingCameraScene): #python has multiple inheritances
    def construct(self):
        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane(x_range = [-7,7,1], y_range = [-20,20,1], x_length = 14, y_length = 40)
        vect1 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(3, 0),
            stroke_color=YELLOW,
        ).add_tip()
        vect2 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(3, 0),
            stroke_color=YELLOW,
        ).add_tip()
        vect3 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(0, 3),
            stroke_color=YELLOW,
        ).add_tip()
        vect4 = Line(
            start=plane.coords_to_point(1.5, 1.5),
            end=plane.coords_to_point(1.5, 0),
            stroke_color=WHITE,
        )
        vect5 = Line(
            start=plane.coords_to_point(0, 1.5),
            end=plane.coords_to_point(1.5, 1.5),
            stroke_color=WHITE,
        )

        
        workingout = MathTex(r"x", font_size = 15).move_to([2,0.2,1])
        workingout1 = MathTex(r"\sin \theta  = \frac{x}{\sin \theta } ", font_size = 15).move_to([2,0.2,1])
        workingout2 = MathTex(r"\sin^{2} \theta  = x", font_size = 15).move_to([2,0.2,1])
        workingout3 = MathTex(r"1 - \sin^{2} \theta", font_size = 15).move_to([2,0.2,1])
        workingout4 = MathTex(r"\cos2\theta", font_size = 15).move_to([2,0.2,1])
        workingout5 = MathTex(r"y", font_size = 15).move_to([1.3,0.7,1]).rotate(PI/2)
        workingout6 = MathTex(r"\cos\theta = \frac{y}{\sin \theta }", font_size = 15).move_to([1.3,0.7,1]).rotate(PI/2)
        workingout7 = MathTex(r"\cos\theta\sin\theta = y ", font_size = 15).move_to([1.3,0.7,1]).rotate(PI/2)
        workingout8 = MathTex(r"\cos \theta\sin\theta = y  ", font_size = 15).move_to([1.3,0.7,1]).rotate(PI/2)
        workingout9 = MathTex(r"1/2\sin2\theta = y  ", font_size = 15).move_to([1.3,0.7,1]).rotate(PI/2)
        workingout10 = [ workingout5, workingout6 , workingout7, workingout8 ,workingout9 ]
        workingout11 = MathTex(r"\begin{bmatrix}1\\0  \end{bmatrix} \rightarrow \begin{bmatrix} 1-2\sin ^{2}\theta \\ 0+\sin2\theta \end{bmatrix}", font_size = 45).move_to([-4,1.5,1])
        workingout12 = MathTex(r"\begin{bmatrix}1\\0  \end{bmatrix} \rightarrow \begin{bmatrix} \cos2\theta \\ \sin2\theta \end{bmatrix}", font_size = 45).move_to([-4,1.5,1])
        workingout13 = MathTex(r"\cos\theta ", font_size = 35).rotate(-PI/4).next_to([0.55,2.25,1])
        workingout14 = [MathTex(r"t", font_size = 15).move_to([0.70,1.6,1]),
                        MathTex(r"\sin \theta =\frac{t}{\cos \theta }", font_size = 15).move_to([0.70,1.7,1]),
                        MathTex(r"\sin \theta\cos \theta = t", font_size = 15).move_to([0.70,1.7,1]),
                        MathTex(r"1/2\sin2\theta = t", font_size = 15).move_to([0.70,1.7,1]),
                        ]
        workingout15 = [MathTex(r"k", font_size = 15).move_to([-0.2,2.25,1]).rotate(PI/2), #best to present workingouts in arrays to iterate through them
                        MathTex(r"\cos \theta =\frac{k}{\cos \theta }", font_size = 15).move_to([-0.2,2.25,1]).rotate(PI/2),
                        MathTex(r"\cos^{2} \theta = k", font_size = 15).move_to([-0.2,2.25,1]).rotate(PI/2),
                        MathTex(r"\begin{bmatrix}0\\1 \end{bmatrix}\rightarrow \begin{bmatrix}0+\sin 2\theta \\ 1-2\cos ^{2}\theta \end{bmatrix}", font_size = 45).move_to([-4,1.5,1]),
                        MathTex(r"\begin{bmatrix}0\\1 \end{bmatrix}\rightarrow \begin{bmatrix}\sin 2\theta \\ -\cos2\theta \end{bmatrix}", font_size = 45).move_to([-4,1.5,1])
                        ]
        
        graph = plane.get_graph(lambda x: x, color = YELLOW)
        graph2 = DashedVMobject(plane.get_graph(lambda x: -x+3, color = YELLOW), num_dashes = 40)
        theta = Arc(radius=0.6, angle=PI/4, arc_center=[0,0,1])
        theta2 = Arc(radius =0.6,start_angle = -PI/2,angle=PI/4,arc_center=[1.5,1.5,1]) #ANGLE IS HOW MUCH IT ROTATES
        thetatext = MathTex(r"\theta", font_size = 25).shift(RIGHT*0.7, UP*0.25)
        angle =  MathTex(r"\theta", font_size = 25).next_to(theta2,DOWN*1.2, RIGHT*0.1)
        iangle = Arc(radius =0.6,start_angle = -PI/2,angle=PI/4,arc_center=[0,3,1])
        iangletext = MathTex(r"\theta", font_size = 25).next_to(iangle,DOWN*1.2, RIGHT*0.1)
        ihat = MathTex(r"\widehat{\imath }", font_size = 35).next_to([1.5,0,0], DOWN)
        sidelength = MathTex(r"\sin \theta ", font_size = 35).rotate(-PI/4).next_to([1.7,1,1])
        x1 = MathTex(r"\sin \theta ", font_size = 35).next_to([2,-0.5,1])
        writearray = [theta, thetatext, theta2, angle, ihat, sidelength]
        x2 = MathTex(r"1/2\sin2\theta = y  ", font_size = 15).move_to([-0.1, 2.25, 1]).rotate(PI/2)
        x3 = MathTex(r"\sin^{2} \theta  = x", font_size = 15).next_to([0.20,1.4,1])
        x4 = Tex("(1,0)", font_size = 35).move_to([3,-0.5,1])
        jhat = MathTex(r"\widehat{\jmath }", font_size = 35).move_to([-0.3, 1.5,1]).rotate(PI/2)
        x5 = Tex("(0,1)", font_size = 35).move_to([-0.5,3,1])
        y = Dot(point = [3,0,1])
        y2 = Dot(point = [0,3,1])
        y3 = MathTex(r"\cos^{2} \theta = k", font_size = 15).move_to([1.3,0.7,1]).rotate(PI/2)
        y4 = MathTex(r"1/2\sin2\theta = t", font_size = 15).move_to([2.0,0.2,1])
        
        full_frame = self.camera.frame.save_state()
        self.play(DrawBorderThenFill(plane), run_time = 3)
        self.play(self.camera.frame.animate.set(width=plane.width * 0.7).move_to([1.5,1.5,1]))
        self.play(GrowFromPoint(vect1, point=vect1.get_start()),run_time=1)
        self.play(Create(graph), run_time = 1)
        self.play(Create(graph2), run_time = 1) #draws from bottom, consider this in run time, may appear like empty time between animations.
        self.play(ReplacementTransform(vect2, vect3)) #changed these from replacement
        self.play(ReplacementTransform(vect1, y)) #transform doesnt actually remove mobject, replacement needed for this.
        self.play(ReplacementTransform(vect3, y2)) #note use of vector 3 now, this is what replacement does
        self.play(GrowFromPoint(vect4, point=vect4.get_start()),run_time=1)
        for i in range(0,6): #for has to be lowercase
            self.play(Write(writearray[i]))#Write only takes two arguments
        self.wait()
        prezoom = self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=plane.width * 0.5).move_to([2.0,0.5,1]))
        self.wait()
        self.play(FadeIn(x4)) #co-ordinate must be in array, 3d coords
        self.play(ReplacementTransform(workingout, workingout1), run_time = 2) #only two arguments
        self.wait()
        self.play(ReplacementTransform(workingout1,workingout2), run_time = 2)
        self.wait()
        for i in range (0,4): # 4 is not inclusive
            self.play(ReplacementTransform(workingout10[i],workingout10[i+1]), run_time = 2)
        self.play(Restore(prezoom))
        self.play(Create(vect5))
        self.play(Write(x2))
        self.play(Write(x3))
        self.play(self.camera.frame.animate.set(width=plane.width * 1).move_to([0,0,1]))
        self.play(Write(workingout11))
        self.play(Transform(workingout11,workingout12))
        self.wait()
        self.play(FadeOut(workingout11, workingout2, workingout9,theta2, ihat, sidelength, x2, x3, angle, x4,), run_time = 2)
        self.wait()
        self.play(Write(jhat))
        self.play(Write(iangle))
        self.play(Write(iangletext))
        self.play(Write(workingout13))
        self.play(self.camera.frame.animate.set(width=plane.width * 0.5).move_to([0.75,1.5,1]))
        self.play(FadeIn(x5))
        for i in range (0,3):
            self.play(ReplacementTransform(workingout14[i],workingout14[i+1]), run_time = 2)
        for i in range (0,2):
            self.play(ReplacementTransform(workingout15[i],workingout15[i+1]), run_time = 2)
        self.wait()
        self.play(Write(y3))
        self.play(Write(y4))
        self.play(self.camera.frame.animate.set(width=plane.width * 1).move_to([0,0,1]))
        self.play(Write(workingout15[3]))
        self.play(Transform(workingout15[3], workingout15[4]))
        self.wait(2)
        self.play(FadeOut(graph, graph2, theta, iangle, iangletext, vect5, vect4 ,vect3, vect1, plane,y, y2, workingout13,x5, thetatext, jhat,workingout14[3],
                          workingout15[3],workingout15[2],y3, y4), run_time = 3)
        self.play(self.camera.frame.animate.set(width=plane.width).move_to([0,0,1]))
        self.play(Write(Tex("Reflection Matrix", font_size = 50).move_to([0,1.5,1])))
        self.play(Write(MathTex(r"\begin{bmatrix}\cos2\theta &\sin2\theta \\ \sin2\theta& -\cos2\theta\end{bmatrix}",font_size = 50).move_to([0,0,1])))
        self.wait(2)
        
            
    
        

        
