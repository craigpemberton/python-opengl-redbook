#!/usr/bin/python

from Window import *

# XXX reshape
# glOrtho(-4, 4, -4*(GLfloat)h/(GLfloat)w, 4*(GLfloat)h/(GLfloat)w, -4, 4)
# glOrtho(-4*(GLfloat)w/(GLfloat)h, 4*(GLfloat)w/(GLfloat)h, -4, 4, -4, 4)

class BezierMesh(Window):
	'''Renders a lighted filled Bezier surface using two-dimensional evaluators.'''

	def __init__(self):
		'''Constructor'''
		super(BezierMesh, self).__init__("bezmesh.c", "Bezier Mesh", 500, 500, 4)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)
		self.controlPoints =	( ( (-1.5, -1.5, 4), (-0.5, -1.5, 2), (0.5, -1.5, -1), (1.5, -1.5,  2) ),
					  ( (-1.5, -0.5, 1), (-0.5, -0.5, 3), (0.5, -0.5,  0), (1.5, -0.5, -1) ),
					  ( (-1.5,  0.5, 4), (-0.5,  0.5, 0), (0.5,  0.5,  3), (1.5, 0.5,   4) ),
					  ( (-1.5, 1.5, -2), (-0.5, 1.5, -2), (0.5,  1.5,  0), (1.5, 1.5,  -1) ) )
		glEnable(GL_DEPTH_TEST)
		glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, self.controlPoints) #XXX probably wrong   #3,4   #12,4
		glEnable(GL_MAP2_VERTEX_3)
		glEnable(GL_AUTO_NORMAL)
		glMapGrid2f(20, 0, 1, 20, 0, 1)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
		glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 2, 1))
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.6, 0.6, 0.6, 1))
		glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
		glMaterialfv(GL_FRONT, GL_SHININESS, (50))

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glRotatef(85, 1, 1, 1)
		glEvalMesh2(GL_FILL, 0, 20, 0, 20)
		glPopMatrix()
		glFlush()

if __name__ == '__main__':
	BezierMesh().run()
