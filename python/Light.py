#!/usr/bin/python

from Window import *

class Lighting(Window):
	''' Demonstrates the use of the OpenGL lighting model.'''

	def __init__(self):
		''' Initialize material property, light source, lighting model, and depth buffer.'''
		super(Lighting, self).__init__("light.c", "Lighting", 500, 500, 1.5)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
		glMaterialfv(GL_FRONT, GL_SHININESS, (50))
		glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)

	def display(self):
		''' A sphere is drawn using a grey material characteristic and a single light source illuminates it.'''
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glutSolidSphere(1, 20, 16)
		glFlush()

if __name__ == '__main__':
	Lighting().run()
