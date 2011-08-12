#!/usr/bin/python

from Window import *

class Alpha(Window):
	'''Draws several overlapping filled polygons to demonstrate the effect order has on alpha blending results.'''

	def __init__(self):
		'''Initialize alpha blending function.'''
		super(Alpha, self).__init__("alpha.c", "Alpha", 200, 200, True)
		self.leftFirst = True
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glShadeModel(GL_FLAT)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		self.keybindings['t'] = self.toggle

	def toggle(self):
		'''Use the 't' key to toggle the order of drawing polygons.'''
		self.leftFirst = not self.leftFirst
		glutPostRedisplay()

	def drawLeftTriangle(self):
		'''Draw yellow triangle on left hand side of screen.'''
		glBegin(GL_TRIANGLES)
		glColor4f(1.0, 1.0, 0.0, 0.75)
		glVertex3f(0.1, 0.9, 0.0)
		glVertex3f(0.1, 0.1, 0.0)
		glVertex3f(0.7, 0.5, 0.0)
		glEnd()

	def drawRightTriangle(self):
		'''Draw cyan triangle on right hand side of screen.'''
		glBegin(GL_TRIANGLES)
		glColor4f(0.0, 1.0, 1.0, 0.75)
		glVertex3f(0.9, 0.9, 0.0)
		glVertex3f(0.3, 0.5, 0.0)
		glVertex3f(0.9, 0.1, 0.0)
		glEnd()

	def display(self):
		'''Draw the two triangles in the order set by the toggle key.'''
		glClear(GL_COLOR_BUFFER_BIT)
		if self.leftFirst:
			self.drawLeftTriangle()
			self.drawRightTriangle()
		else:
			self.drawRightTriangle()
			self.drawLeftTriangle()
		glFlush()

if __name__ == '__main__':
	Alpha().run()
