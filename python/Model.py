#!/usr/bin/python

from Window import *

class ModelingTransformations(Window):
	'''Demonstrates modeling transformations'''

	def __init__(self):
		super(ModelingTransformations, self).__init__("model.c", "Modeling Transformations", 500, 500)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glLoadIdentity()
		glColor3f(1, 1, 1)
		self.drawTriangle()
		glEnable(GL_LINE_STIPPLE)
		glLineStipple(1, 0xF0F0)
		glLoadIdentity()
		glTranslatef(-20, 0, 0)
		self.drawTriangle()
		glLineStipple(1, 0xF00F)
		glLoadIdentity()
		glScalef(1.5, 0.5, 1)
		self.drawTriangle()
		glLineStipple(1, 0x8888)
		glLoadIdentity()
		glRotatef(90, 0, 0, 1)
		self.drawTriangle()
		glDisable(GL_LINE_STIPPLE)
		glFlush()

	def drawTriangle(self):
		glBegin(GL_LINE_LOOP)
		glVertex2f(0, 25)
		glVertex2f(25, -25)
		glVertex2f(-25, -25)
		glEnd()

if __name__ == '__main__':
	ModelingTransformations().run()
