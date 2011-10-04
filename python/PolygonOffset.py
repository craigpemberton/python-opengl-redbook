#!/usr/bin/python

from Window import *

class PolygonOffset(Window):
	'''Uses polygon offset to draw a shaded polygon and its wireframe counterpart without stitching artifacts.'''

	def __init__(self):
		'''Specify initial properties, create display list with sphere, initialize lighting and depth buffer.'''
		super(PolygonOffset, self).__init__('polyoff.c', 'Polygon Offset', 500, 500)
		self.keybindings['T'] = self.keyT
		self.keybindings['t'] = self.keyt
		self.keybindings['F'] = self.keyF
		self.keybindings['f'] = self.keyf
		self.keybindings['U'] = self.keyU
		self.keybindings['u'] = self.keyu
		self.displayList = glGenLists(1)
		self.spinx = 0
		self.spiny = 0
		self.tdist = 0
		self.polyfactor = 1
		self.polyunits = 1
		glNewList(self.displayList, GL_COMPILE)
		glutSolidSphere(1, 20, 12)
		glEndList()
		glEnable(GL_DEPTH_TEST)
		glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
		glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
		glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))
		glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1))
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)

	def display(self):
		'''Draw two spheres, one diffuse and gray, the other specular and magenta.'''
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glTranslatef(0, 0, self.tdist)
		glRotatef(self.spinx, 1, 0, 0)
		glRotatef(self.spiny, 0, 1, 0)
		glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.8, 0.8, 0.8, 1))
		glMaterialfv(GL_FRONT, GL_SPECULAR, (0, 0, 0, 1))
		glMaterialf(GL_FRONT, GL_SHININESS, 0)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_POLYGON_OFFSET_FILL)
		glPolygonOffset(self.polyfactor, self.polyunits)
		glCallList(self.displayList)
		glDisable(GL_POLYGON_OFFSET_FILL)
		glDisable(GL_LIGHTING)
		glDisable(GL_LIGHT0)
		glColor3f(1, 1, 1)
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
		glCallList(self.displayList)
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
		glPopMatrix()
		glFlush()

	def mouseLeftClick(self):
			self.spinx = (self.spinx + 5) % 360

	def mouseMiddleClick(self):
			self.spiny = (self.spiny + 5) % 360

	def mouseRightClick(self):
			exit()

	def keyT(self):
		if(self.tdist > -5):
			self.tdist -= 0.5

	def keyt(self):
		if self.tdist < 4:
			self.tdist += 0.5

	def keyF(self):
		self.polyfactor += 0.1
		print 'polyfactor is', self.polyfactor

	def keyf(self):
		self.polyfactor -= 0.1
		print 'polyfactor is', self.polyfactor

	def keyU(self):
		self.polyunits += 1
		print 'polyunits is', self.polyunits

	def keyu(self):
		self.polyunits -= 1
		print 'polyunits', self.polyunits
	
if __name__ == '__main__':
	PolygonOffset().run()
