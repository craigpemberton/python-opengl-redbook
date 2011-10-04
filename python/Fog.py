#!/usr/bin/python

from Window import *

class Fog(Window):
	'''Draws 5 red spheres, each at a different z distance from the eye, in different types of fog.'''
	'''In this program, there is a fixed density value, as well as fixed start and end values for the linear fog.'''

	def __init__(self):
		'''Initialize depth buffer, fog, light source, material property, and lighting model.'''
		super(Fog, self).__init__("fog.c", "Fog", 500, 500, 2.5)
		self.fogMode = GL_EXP
		self.keybindings['f']  = self.toggleFog
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glutInitWindowSize(500, 500)
		glEnable(GL_DEPTH_TEST)
		glLightfv(GL_LIGHT0, GL_POSITION, (0.5, 0.5, 3, 0))
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glMaterialfv(GL_FRONT, GL_AMBIENT,  (0.17450, 01175, 01175))
		glMaterialfv(GL_FRONT, GL_DIFFUSE,  (0.61424, 04136, 04136))
		glMaterialfv(GL_FRONT, GL_SPECULAR, (0.727811, 0.626959, 0.626959))
		glMaterialf(GL_FRONT, GL_SHININESS, 0.6*128)
		glEnable(GL_FOG)
		glFogi(GL_FOG_MODE, self.fogMode)
		glFogfv(GL_FOG_COLOR, (0.5, 0.5, 0.5, 1))
		glClearColor(0.5, 0.5, 0.5, 1) #fog color
		glFogf(GL_FOG_DENSITY, 0.35)
		glHint(GL_FOG_HINT, GL_DONT_CARE)
		glFogf(GL_FOG_START, 1)
		glFogf(GL_FOG_END, 5)

	def display(self):
		'''Draws 5 spheres at different z positions.'''
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.renderSphere(-2, -0.5, -1)
		self.renderSphere(-1, -0.5, -2)
		self.renderSphere( 0, -0.5, -3)
		self.renderSphere( 1, -0.5, -4)
		self.renderSphere( 2, -0.5, -5)
		glFlush()

	def renderSphere(self, x, y, z):
		'''Render a sphere at the given point.'''
		glPushMatrix()
		glTranslatef(x, y, z)
		glutSolidSphere(0.4, 16, 16)
		glPopMatrix()

	def toggleFog(self):
		'''Pressing the f key chooses between 3 types of fog:  exponential, exponential squared, and linear.'''
		if self.fogMode == GL_EXP:
			self.fogMode = GL_EXP2
			print 'Fog mode is GL_EXP2'
		elif self.fogMode == GL_EXP2:
			self.fogMode = GL_LINEAR
			print 'Fog mode is GL_LINEAR'
		elif self.fogMode == GL_LINEAR:
			self.fogMode = GL_EXP
			print 'Fog mode is GL_EXP'
		glFogi(GL_FOG_MODE, self.fogMode)

if __name__ == '__main__':
	Fog().run()
