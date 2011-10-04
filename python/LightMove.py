#!/usr/bin/python

from Window import *

class LightMove(Window):
	''' Demonstrates when to issue lighting and transformation commands to render a model with a light which is moved by a modeling transformation.'''
	''' The light position is reset after the modeling transformation is called.'''
	''' The eye position does not change.'''
	''' A sphere is drawn using a grey material characteristic.'''
	''' A single light source illuminates the object.'''

	def __init__(self):
		''' Initialize material property, light source, lighting model, and depth buffer.'''
		super(LightMove, self).__init__("movelight.c", "Light Move", 500, 500)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)
		self.spin = 0

	def display(self):
		''' Light position is reset after the modeling transformation.'''
		''' This places the light at a new position in world coordinates.'''
		''' The cube represents the position of the light.'''
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
		glPushMatrix()
		glRotated(self.spin, 1, 0, 0)
		glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 1.5, 1))
		glTranslated(0, 0, 1.5)
		glDisable(GL_LIGHTING)
		glColor3f(0, 1, 1)
		glutWireCube(0.1)
		glEnable(GL_LIGHTING)
		glPopMatrix()
		glutSolidTorus(0.275, 0.85, 8, 15)
		glPopMatrix()
		glFlush()

	def mouseLeftClick(self, x, y):
		''' Pressing the left mouse button alters the modeling transformation (x rotation) by 30 degrees.'''
		self.spin = (self.spin + 30) % 360

if __name__ == '__main__':
	LightMove().run()
