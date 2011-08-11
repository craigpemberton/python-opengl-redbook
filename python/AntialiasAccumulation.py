#!/usr/bin/python

from Window import *
from jitter import *

class AccumulatorAntialias(Window):
	''' Use the accumulation buffer to do full-scene antialiasing on a scene with orthographic parallel projection.'''
	def __init__(self):
		'''Initialize lighting and other values.'''
		super(AccumulatorAntialias, self).__init__("Accumulator Antialias", 800, 800, True)
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_ACCUM|GLUT_DEPTH)
		self.source = "accanti.c"
		self.acSize = 8
		mat_ambient 	= (1, 1, 1, 1)
		mat_specular	= (1, 1, 1, 1)
		light_position	= (0, 0, 10, 1)
		lm_ambient	= (0.2, 0.2, 0.2, 1)
		glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
		glMaterialf(GL_FRONT, GL_SHININESS, 50)
		glLightfv(GL_LIGHT0, GL_POSITION, light_position)
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lm_ambient)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_FLAT)
		glClearAccum(0, 0, 0, 0)

	def displayObjects(self):
		''' '''
		torus_diffuse	= (0.7, 0.7,   0, 1)
		cube_diffuse	= (  0, 0.7, 0.7, 1)
		sphere_diffuse	= (0.7,   0, 0.7, 1)
		octa_diffuse	= (0.7, 0.4, 0.4, 1)
		glPushMatrix()
		glRotatef(30, 1, 0, 0)
		glPushMatrix()
		glTranslatef(-0.80, 0.35, 0) 
		glRotatef(100, 1, 0, 0)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, torus_diffuse)
		glutSolidTorus(0.275, 0.85, 16, 16)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-0.75, -0.50, 0) 
		glRotatef(45, 0, 0, 1)
		glRotatef(45, 1, 0, 0)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, cube_diffuse)
		glutSolidCube(1.5)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(0.75, 0.60, 0) 
		glRotatef(30, 1, 0, 0)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, sphere_diffuse)
		glutSolidSphere(1, 16, 16)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(0.70, -0.90, 0.25) 
		glMaterialfv(GL_FRONT, GL_DIFFUSE, octa_diffuse)
		glutSolidOctahedron()
		glPopMatrix()
		glPopMatrix()

	def display(self):
		''' '''
		viewport = glGetIntegerv(GL_VIEWPORT)
		glClear(GL_ACCUM_BUFFER_BIT)
		for jitter in range(self.acSize):
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
			glPushMatrix()
			# 4.5 is the distance in world space between left and right and bottom and top.
			# This formula converts fractional pixel movement to world coordinates.
			glTranslatef(j8[jitter][0]*4.5/viewport[2], j8[jitter][1]*4.5/viewport[3], 0)
			self.displayObjects()
			glPopMatrix()
			glAccum(GL_ACCUM, 1.0/self.acSize)
		glAccum(GL_RETURN, 1)
		glFlush()

	def reshape(self, w, h):
		''' '''
		glViewport(0, 0,w, h)
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
