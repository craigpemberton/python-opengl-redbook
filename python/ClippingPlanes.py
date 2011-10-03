#!/usr/bin/python

from Window import *

class ClippingPlanes(Window):
	'''Demonstrates arbitrary clipping planes.'''

	def __init__(self):
		'''Initialize alpha blending function.'''
		super(ClippingPlanes, self).__init__("clip.c", "Clipping Planes", 500, 500)
		#gluPerspective(60, w/h, 1, 20)
		glShadeModel(GL_FLAT)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glPushMatrix()
		glTranslatef(0, 0, -5)
		# Clip lower half (y<0).
		glClipPlane(GL_CLIP_PLANE0, (0, 1, 0, 0))
		glEnable(GL_CLIP_PLANE0)
		# Clip left half (x<0).
		glClipPlane(GL_CLIP_PLANE1, (1, 0, 0, 0))
		glEnable(GL_CLIP_PLANE1)
		glRotatef(90, 1, 0, 0)
		glutWireSphere(1, 20, 16)
		glPopMatrix()
		glFlush()

if __name__ == '__main__':
	ClippingPlanes().run()
