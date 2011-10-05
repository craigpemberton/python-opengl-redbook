#!/usr/bin/python

from Window import *

class DisplayList(Window):
	''' Demonstrates how to make and execute a display list.'''
	''' Attributes such as current color and matrix are changed.'''

	def __init__(self):
		super(DisplayList, self).__init__("list.c", "Display List", 650, 50)
		self.list = glGenLists(1)
		glNewList(self.list, GL_COMPILE)
		glColor3f(1, 0, 0)
		glBegin(GL_TRIANGLES)
		glVertex2f(0, 0)
		glVertex2f(1, 0)
		glVertex2f(0, 1)
		glEnd()
		glTranslatef(1.5, 0, 0)
		glEndList()
		glShadeModel(GL_FLAT)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(0, 1, 0)
		for i in range(10): # Draw 10 triangles.
			glCallList(self.list)
		self.drawLine() # Is this line green? NO! Where is the line drawn?
		glFlush()

	def drawLine(self):
		glBegin(GL_LINES)
		glVertex2f(0, 0.5)
		glVertex2f(15, 0.5)
		glEnd()

if __name__ == '__main__':
	DisplayList().run()
