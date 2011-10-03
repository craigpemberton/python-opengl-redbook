#!/usr/bin/python

from Window import *

class BezierSurface(Window):
	'''Renders a wireframe Bezier surface, using two-dimensional evaluators.'''

	def __init__(self):
		'''Constructor'''
		super(BezierSurface, self).__init__("bezsurf.c", "Bezier Surface", 500, 500, 4)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)
		self.controlPoints =	(((-1.5, -1.5,  4.0),
					  (-0.5, -1.5,  2.0),
					  ( 0.5, -1.5, -1.0),
					  ( 1.5, -1.5,  2.0),),
					 ((-1.5, -0.5,  1.0),
					  (-0.5, -0.5,  3.0),
					  ( 0.5, -0.5,  0.0),
					  ( 1.5, -0.5, -1.0),),
					 ((-1.5,  0.5,  4.0),
					  (-0.5,  0.5,  0.0),
					  ( 0.5,  0.5,  3.0),
					  ( 1.5,  0.5,  4.0),),
					 ((-1.5,  1.5, -2.0),
					  (-0.5,  1.5, -2.0),
					  ( 0.5,  1.5,  0.0),
					  ( 1.5,  1.5, -1.0),),)
		#glMap2f(GL_MAP2_VERTEX_3,  0, 1,  3, 4,  0, 1,  12, 4, &ctrlpoints[0][0][0]);
		glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, self.controlPoints)
		glEnable(GL_MAP2_VERTEX_3)
		glMapGrid2f(20, 0, 1, 20, 0, 1)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_FLAT)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glPushMatrix()
		glRotatef(85, 1, 1, 1)
		for j in range(8):
			glBegin(GL_LINE_STRIP)
			for i in range(30):
				glEvalCoord2f(i/30.0, j/8.0)
			glEnd()
			glBegin(GL_LINE_STRIP)
			for i in range(30):
				glEvalCoord2f(j/8.0, i/30.0)
			glEnd()
		glPopMatrix()
		glFlush()

if __name__ == '__main__':
	BezierSurface().run()
