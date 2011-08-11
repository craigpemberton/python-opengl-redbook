#!/usr/bin/python
''' Use the accumulation buffer to do full-scene antialiasing on a scene with orthographic parallel projection.'''

from Window import *
from jitter import *

class AccumulatorAntialias(Window):
	''' Use the accumulation buffer to do full-scene antialiasing on a scene with orthographic parallel projection.'''
	def __init__(self):
		'''Initialize lighting and other values.'''
		super(AccumulatorAntialias, self).__init__("accanti.c", "Accumulator Antialias", 800, 800, True)
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_ACCUM|GLUT_DEPTH)
		glMaterialfv(GL_FRONT, GL_AMBIENT,  (1, 1, 1, 1))
		glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
		glMaterialf (GL_FRONT, GL_SHININESS, 50)
		glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 10, 1))
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1))
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_FLAT)
		glClearAccum(0, 0, 0, 0)

	@staticmethod
	def displayObjects():
		'''Show a torus, a cube, a sphere, and an octahedron.'''
		glPushMatrix()
		glRotatef(30, 1, 0, 0)
		glPushMatrix()
		glTranslatef(-0.80, 0.35, 0) 
		glRotatef(100, 1, 0, 0)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.7, 0.7, 0, 1))
		glutSolidTorus(0.275, 0.85, 16, 16)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-0.75, -0.50, 0) 
		glRotatef(45, 0, 0, 1)
		glRotatef(45, 1, 0, 0)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0.7, 0.7, 1))
		glutSolidCube(1.5)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(0.75, 0.60, 0) 
		glRotatef(30, 1, 0, 0)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.7, 0, 0.7, 1))
		glutSolidSphere(1, 16, 16)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(0.70, -0.90, 0.25) 
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.7, 0.4, 0.4, 1))
		glutSolidOctahedron()
		glPopMatrix()
		glPopMatrix()

	def display(self):
		'''Display function.'''
		viewport = glGetIntegerv(GL_VIEWPORT)
		glClear(GL_ACCUM_BUFFER_BIT)
		for jitter in range(8):
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
			glPushMatrix()
			# 4.5 is the distance in world space between left and right and bottom and top.
			# This formula converts fractional pixel movement to world coordinates.
			glTranslatef(J8[jitter][0]*4.5/viewport[2], J8[jitter][1]*4.5/viewport[3], 0)
			self.displayObjects()
			glPopMatrix()
			glAccum(GL_ACCUM, 1.0/8)
		glAccum(GL_RETURN, 1)
		glFlush()

	def reshape(self, w, h):
		'''XXX Should not be overridden.'''
		glViewport(0, 0, w, h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		if(w <= h):
			glOrtho(-2.25, 2.25, -2.25*h/w, 2.25*h/w, -10, 10)
		else:
			glOrtho(-2.25*w/h, 2.25*w/h, -2.25, 2.25, -10, 10)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

if __name__ == '__main__':
	AccumulatorAntialias().run()
