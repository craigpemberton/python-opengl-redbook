#!/usr/bin/python

from Window import *

class Cube(Window):
	'''Demonstrates the modeling transformation glScalef() and the viewing transformation gluLookAt().'''

	def __init__(self):
		super(Cube, self).__init__("cube.c", "Cube", 500, 500)
		#glFrustum(-1, 1, -1, 1, 1.5, 20)
		glShadeModel(GL_FLAT)

	def display(self):
		'''A wireframe cube is rendered.'''
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glLoadIdentity()
		gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
		glScalef(1, 2, 1)
		glutWireCube(1)
		glFlush()

if __name__ == '__main__':
	Cube().run()
