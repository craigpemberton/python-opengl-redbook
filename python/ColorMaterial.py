#!/usr/bin/python

from Window import *

class ColorMaterial(Window):
	''' Demonstrates ColorMaterial mode. Pressing the mouse buttons will change the diffuse reflection values.'''

	def __init__(self):
		'''Initialize material property, light source, lighting model, and depth buffer.'''
		super(ColorMaterial, self).__init__("colormat.c", "Color Material", 500, 500, 1.5)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		self.diffuseMaterial = [0.5, 0.5, 0.5, 1]
		glShadeModel(GL_SMOOTH)
		glEnable(GL_DEPTH_TEST)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, self.diffuseMaterial)
		glMaterialfv(GL_FRONT, GL_SPECULAR, ( 1, 1, 1, 1 ))
		glMaterialf(GL_FRONT, GL_SHININESS, 25)
		glLightfv(GL_LIGHT0, GL_POSITION, ( 1, 1, 1, 0 ))
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glColorMaterial(GL_FRONT, GL_DIFFUSE)
		glEnable(GL_COLOR_MATERIAL)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glutSolidSphere(1, 20, 16)
		glFlush()

	def changeMaterial(self, index):
		self.diffuseMaterial[index] += 0.1
		if self.diffuseMaterial[index] > 1:
			self.diffuseMaterial[index] = 0
		glColor4fv(self.diffuseMaterial)

	def mouseLeftClick(self, x, y):
		self.changeMaterial(0)

	def mouseMiddleClick(self, x, y):
		self.changeMaterial(1)

	def mouseRightClick(self, x, y):
		self.changeMaterial(2)

if __name__ == '__main__':
	ColorMaterial().run()
