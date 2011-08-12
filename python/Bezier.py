#!/usr/bin/python
'''Use evaluators to draw a Bezier curve.'''

from Window import *

class Bezier(Window):
	'''Use evaluators to draw a Bezier curve.'''

	def __init__(self):
		'''Constructor'''
		super(Bezier, self).__init__("bezcurve.c", "Bezier", 500, 500, True)
		self.controlPoints = ((-4/5.0, -4/5.0, 0),( -2/5.0, 4/5.0, 0), (2/5.0, -4/5.0, 0), (4/5.0, 4/5.0, 0))
		glClearColor(0, 0, 0, 0)
		glShadeModel(GL_FLAT)
		glMap1f(GL_MAP1_VERTEX_3, 0, 1, self.controlPoints)
		glEnable(GL_MAP1_VERTEX_3)

	def display(self):
		'''Display the control points as dots.'''
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glBegin(GL_LINE_STRIP)
		for i in range(31):
			glEvalCoord1f(float(i)/31)
		glEnd()
		glPointSize(5)
		glColor3f(1, 1, 0)
		glBegin(GL_POINTS)
		for point in self.controlPoints:
			glVertex3fv(point)
		glEnd()
		glFlush()

if __name__ == '__main__':
	Bezier().run()
