#!/usr/bin/python

from graphics import *

class AntialiasIndex(Window):
	'''Draw two anti-aliased lines in color index mode. 'r' rotates the lines in opposite directions.'''
	def __init__(self):
		''' Initialize antialiasing for color index mode. A green color ramp starts at ramp1Start, a blue one at ramp2Start. \
		The ramps must be multiples of 16.'''
		super(AntialiasIndex, self).__init__("Antialias Index", 200, 200, True)
		self.source = "aaindex.c"
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_INDEX)
		self.rampSize   = 16
		self.ramp1Start = 32
		self.ramp2Start = 48
		self.angle = 0.0
		self.keybindings['r'] = self.rotate
		for index in range(self.rampSize):
			shade = float(index)/self.rampSize
			glutSetColor(self.ramp1Start+index, 0, shade, 0)
			glutSetColor(self.ramp2Start+index, 0, 0, shade)
		glEnable(GL_LINE_SMOOTH)
		glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
		glLineWidth(1.5)
		glClearIndex(self.ramp1Start)

	def rotate(self):
		'''Increment the rotation angle by 20 degrees.'''
		self.angle += 20
		if self.angle > 360:
			self.angle = 0.0
		glutPostRedisplay()

	def display(self):
		'''Draw two diagonal lines, forming an X.'''
		glClear(GL_COLOR_BUFFER_BIT)
		glIndexi(self.ramp1Start)
		glPushMatrix()
		glRotatef(-self.angle, 0, 0, 0.1)
		glBegin(GL_LINES)
		glVertex2f(-0.5,  0.5)
		glVertex2f( 0.5, -0.5)
		glEnd()
		glPopMatrix()
		glIndexi(self.ramp2Start)
		glPushMatrix()
		glRotatef(self.angle, 0.0, 0.0, 0.1)
		glBegin(GL_LINES)
		glVertex2f( 0.5,  0.5)
		glVertex2f(-0.5, -0.5)
		glEnd()
		glPopMatrix()
		glFlush()

if __name__ == '__main__':
	AntialiasIndex().run()
