#!/usr/bin/python

from Window import *

class LightScene(Window):
	'''Demonstrates the use of the GL lighting model. A single light source illuminates the objects.'''

	def __init__(self):
		'''Initialize material property and light source.'''
		super(LightScene, self).__init__("scene.c", "Light Scene", 500, 500, 2.5)
		glLightfv(GL_LIGHT0, GL_AMBIENT,  (0, 0, 0, 1))
		glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1, 1, 1, 1))
		glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))
		glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)

	def display(self):
		'''Objects are drawn using a grey material characteristic.'''
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glRotatef(20, 1, 0, 0)
		glPushMatrix()
		glTranslatef(-0.75, 0.5, 0)
		glRotatef(90, 1, 0, 0)
		glutSolidTorus(0.275, 0.85, 15, 15)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-0.75, -0.5, 0)
		glRotatef(270, 1, 0, 0)
		glutSolidCone(1, 2, 15, 15)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(0.75, 0, -1)
		glutSolidSphere(1, 15, 15)
		glPopMatrix()
		glPopMatrix()
		glFlush()

if __name__ == '__main__':
	LightScene().run()
