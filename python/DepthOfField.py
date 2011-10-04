#!/usr/bin/python

import math

from jitter import *
from Window import *

class DepthOfField(Window):
	'''Use the accumulation buffer to create an out-of-focus depth-of-field effect.'''
	'''The teapots are drawn several times into the accumulation buffer.'''
	'''The viewing volume is jittered, except at the focal point where the viewing volume is at the same position each time.'''
	'''In this case, the gold teapot remains in focus.'''

	def __init__(self):
		super(DepthOfField, self).__init__("dof.c", "Depth of field", 400, 400)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_ACCUM | GLUT_DEPTH)
		glLightfv(GL_LIGHT0, GL_AMBIENT,  (0, 0, 0, 1))
		glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1, 1, 1, 1))
		glLightfv(GL_LIGHT0, GL_POSITION, (0, 3, 3, 0))
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1))
		glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, (0))
		glFrontFace(GL_CW)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_AUTO_NORMAL)
		glEnable(GL_NORMALIZE)
		glEnable(GL_DEPTH_TEST)
		glClearAccum(0, 0, 0, 0)
		self.teapotList = glGenLists(1)
		glNewList(self.teapotList, GL_COMPILE)
		glutSolidTeapot(0.5)
		glEndList()

	def display(self):
		'''Draws 5 teapots into the accumulation buffer several times, each time with a jittered perspective.'''
		'''The focal point is at z = 5, so the gold teapot will stay in focus.'''
		'''The amount of jitter is adjusted by the magnitude of the accPerspective() jitter.'''
		'''In this example the magnitude is 0.33 and the teapots are drawn 8 times.'''
		viewport = glGetIntegerv(GL_VIEWPORT)
		glClear(GL_ACCUM_BUFFER_BIT)

		for jitter in range(8):
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
			self.accPerspective(45, viewport[2]/ viewport[3], 1, 15, 0, 0, 0.33*J8[jitter][0], 0.33*J8[jitter][1], 5)
			self.renderTeapot(-1.1, -0.5, -4.5, 0.17450, 0117500, 0.11750, 0.61424, 0.41360, 0413600, 0.727811, 0.626959, 0.626959, 0.60) # ruby
			self.renderTeapot(-0.5, -0.5, -5.0, 0.24725, 0.19950, 0.74500, 0.75164, 0.60648, 0.22648, 0.628281, 0.555802, 0.366065, 0.40) # gold
			self.renderTeapot( 0.2, -0.5, -5.5, 0.19225, 0.19225, 0.19225, 0.50754, 0.50754, 0.50754, 0.508273, 0.508273, 0.508273, 0.40) # silver
			self.renderTeapot( 1.0, -0.5, -6.0, 0.21500, 0.17450, 0.21500, 0.75680, 0.61424, 0.75680, 0.633000, 0.727811, 0.633000, 0.60) # emerald
			self.renderTeapot( 1.8, -0.5, -6.5, 0.00000, 0.10000, 0.60000, 0.00000, 0.50980, 0.50980, 0.501961, 0.501961, 0.501961, 0.25) # cyan
			glAccum(GL_ACCUM, 0.125)
		glAccum(GL_RETURN, 1)
		glFlush()

	def accFrustum(self, left, right, bottom, top, near, far, pixdx, pixdy, eyedx, eyedy, focus):
		'''The first 6 arguments are identical to the glFrustum() call.'''
		'''pixdx and pixdy are anti-alias jitter in pixels.	Set both equal to 0 for no anti-alias jitter.'''
		'''eyedx and eyedy are depth-of field jitter in pixels.	Set both equal to 0 for no depth of field effects.'''
		'''focus is distance from eye to plane in focus.	focus must be greater than, but not equal to 0.'''
		'''Note that accFrustum() calls glTranslatef().'''
		viewport = glGetIntegerv(GL_VIEWPORT)
		xwsize = right - left
		ywsize = top - bottom
		dx = -(pixdx*xwsize/ viewport[2] + eyedx*near/focus)
		dy = -(pixdy*ywsize/ viewport[3] + eyedy*near/focus)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glFrustum(left + dx, right + dx, bottom + dy, top + dy, near, far)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef(-eyedx, -eyedy, 0)

	def accPerspective(self, fovy, aspect, near, far, pixdx, pixdy, eyedx, eyedy, focus):
		'''The first 4 arguments are identical to the gluPerspective() call.'''
		'''pixdx and pixdy are anti-alias jitter in pixels.	Set both equal to 0 for no anti-alias jitter.'''
		'''eyedx and eyedy are depth-of field jitter in pixels.	Set both equal to 0 for no depth of field effects.'''
		'''focus is distance from eye to plane in focus.	focus must be greater than, but not equal to 0.'''
		'''Note that accPerspective() calls accFrustum().'''
		fov2 = ((fovy*math.pi) / 180) / 2
		top = near / (math.cos(fov2) / math.sin(fov2))
		bottom = -top
		right = top * aspect
		left = -right
		self.accFrustum(left, right, bottom, top, near, far, pixdx, pixdy, eyedx, eyedy, focus)

	def renderTeapot(self, x, y, z, ambr, ambg, ambb, difr, difg, difb, specr, specg, specb, shine):
		glPushMatrix()
		glTranslatef(x, y, z)
		glMaterialfv(GL_FRONT, GL_AMBIENT, (ambr, ambg, ambb, 1))
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (difr, difg, difb, 1))
		glMaterialfv(GL_FRONT, GL_SPECULAR, (specr, specg, specb, 1))
		glMaterialf(GL_FRONT, GL_SHININESS, shine*128)
		glCallList(self.teapotList)
		glPopMatrix()

if __name__ == '__main__':
	DepthOfField().run()
