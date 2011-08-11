#!/usr/bin/python
'''Derived from redbook/aargb.c'''

from graphics import *

class AntialiasRGB(Window):
	'''Draw two anti-aliased lines in color rgb mode. 'r' rotates the lines in opposite directions.'''
	def __init__(self):
		'''Initialize antialiasing for RGBA mode, including alpha blending, hint, and line width. '''
		'''Print out implementation  specific info on line width granularity and width.'''
		super(AntialiasRGB, self).__init__("Antialias RGB", 200, 200, True)
		self.angle = 0.0
		self.keybindings['r'] = self.rotate
		print "GL_LINE_WIDTH_GRANULARITY value is ", glGetDoublev(GL_LINE_WIDTH_GRANULARITY)
		print "GL_LINE_WIDTH_RANGE values are ", glGetDoublev(GL_LINE_WIDTH_RANGE) #This should have 2 values?
		glEnable(GL_LINE_SMOOTH)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
		glLineWidth(1.5)


	def rotate(self):
		'''Increment the rotation angle by 20 degrees.'''
		self.angle += 20
		if self.angle > 360:
			self.angle = 0.0
		glutPostRedisplay()

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(0, 1, 0)
		glPushMatrix()
		glRotatef(-self.angle, 0, 0, 0.1)
		glBegin(GL_LINES)
		glVertex2f(-0.5,  0.5)
		glVertex2f( 0.5, -0.5)
		glEnd()
		glPopMatrix()
		glColor3f(0, 0, 1)
		glPushMatrix()
		glRotatef(self.angle, 0, 0, 0.1)
		glBegin(GL_LINES)
		glVertex2f( 0.5,  0.5)
		glVertex2f(-0.5, -0.5)
		glEnd()
		glPopMatrix()
		glFlush()		

if __name__ == '__main__':
	AntialiasRGB().run()
