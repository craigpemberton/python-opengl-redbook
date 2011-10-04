#!/usr/bin/python

from Window import *

class FogIndex(Window):
	'''Draws 5 wireframe spheres, each at a different z distance from the eye, in linear fog.'''

	def __init__(self):
		super(FogIndex, self).__init__("fogindex.c", "Fox Index", 500, 500, 2.5)
		''' Initialize color map and fog.  Set screen clear color to end of color ramp.'''
		glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX | GLUT_DEPTH)
		NUMCOLORS = 32
		RAMPSTART = 16
		glEnable(GL_DEPTH_TEST)
		for i in range(NUMCOLORS):
			shade = (NUMCOLORS - i) / float(NUMCOLORS)
			glutSetColor(RAMPSTART + i, shade, shade, shade)
		glEnable(GL_FOG)
		glFogi(GL_FOG_MODE, GL_LINEAR)
		glFogi(GL_FOG_INDEX, NUMCOLORS)
		glFogf(GL_FOG_START, 1)
		glFogf(GL_FOG_END, 6)
		glHint(GL_FOG_HINT, GL_NICEST)
		glClearIndex(NUMCOLORS+RAMPSTART-1)

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

if __name__ == '__main__':
	FogIndex().run()
