#!/usr/bin/python

from Window import *

class DoubleBuffering(Window):
	'''A simple double buffering example.'''

	def __init__(self):
		super(DoubleBuffering, self).__init__("double.c", "Double Buffering", 250, 250, 50)
		glShadeModel(GL_FLAT)
		self.spin = 0

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glPushMatrix()
		glRotatef(self.spin, 0, 0, 1)
		glColor3f(1, 1, 1)
		glRectf(-25, -25, 25, 25)
		glPopMatrix()
		glutSwapBuffers()

	def spinDisplay(self):
		self.spin += 2
		if(self.spin > 360):
			self.spin -= 360
		glutPostRedisplay()

	def mouseLeftClick(self, x, y):
		'''Pressing the left mouse button rotates the rectangle.'''
		glutIdleFunc(self.spinDisplay)

	def mouseRightClick(self, x, y):
		'''Pressing the right mouse button stops the rotation.'''
		glutIdleFunc(noop)

if __name__ == '__main__':
	DoubleBuffering().run()
