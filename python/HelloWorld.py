#!/usr/bin/python

from Window import *

class HelloWorld(Window):
	'''This is a simple, introductory OpenGL program.'''

	def __init__(self):
		super(HelloWorld, self).__init__("hello.c", "Hello World", 250, 250, 1)

	def display(self):
		'''A wireframe cube is rendered.'''
		glClear(GL_COLOR_BUFFER_BIT) # Clear all pixels.
		# Draw white polygon (rectangle) with corners at (0.25, 0.25, 0) and (0.75, 0.75, 0)
		glColor3f(1, 1, 1)
		glBegin(GL_POLYGON)
		glVertex3f(0.25, 0.25, 0)
		glVertex3f(0.75, 0.25, 0)
		glVertex3f(0.75, 0.75, 0)
		glVertex3f(0.25, 0.75, 0)
		glEnd()
		# Don't wait! Start processing buffered OpenGL routines.
		glFlush()

if __name__ == '__main__':
	HelloWorld().run()
