#!/usr/bin/python

from Window import *

class Quadratic(Window):
	'''Demonstrates the use of some of the gluQuadric* routines.'''
	'''Quadric objects are created with some quadric properties and the callback routine to handle errors.'''
	'''Note that the cylinder has no top or bottom and the circle has a hole in it.'''

	def __init__(self):
		'''Create 4 display lists, each with a different quadric object.'''
		'''Different drawing styles and surface normal specifications are demonstrated.'''
		super(Quadratic, self).__init__('quadratic.c', 'Quadratic', 500, 500)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glMaterialfv(GL_FRONT, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
		glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
		glMaterialfv(GL_FRONT, GL_SHININESS, (50))
		glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.5, 0.5, 0.5, 1))
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)
		self.startList = glGenLists(4)
		quadratic = gluNewQuadric()
		#gluQuadricCallback(quadratic, GLU_ERROR, self.errorCallback) #XXX get error
		gluQuadricDrawStyle(quadratic, GLU_FILL) # smooth shaded
		gluQuadricNormals(quadratic, GLU_SMOOTH)
		glNewList(self.startList, GL_COMPILE)
		gluSphere(quadratic, 0.75, 15, 10)
		glEndList()
		gluQuadricDrawStyle(quadratic, GLU_FILL) # flat shaded
		gluQuadricNormals(quadratic, GLU_FLAT)
		glNewList(self.startList+1, GL_COMPILE)
		gluCylinder(quadratic, 0.5, 0.3, 1, 15, 5)
		glEndList()
		gluQuadricDrawStyle(quadratic, GLU_LINE) # all polygons wireframe
		gluQuadricNormals(quadratic, GLU_NONE)
		glNewList(self.startList+2, GL_COMPILE)
		gluDisk(quadratic, 0.25, 1, 20, 4)
		glEndList()
		gluQuadricDrawStyle(quadratic, GLU_SILHOUETTE) # boundary only
		gluQuadricNormals(quadratic, GLU_NONE)
		glNewList(self.startList+3, GL_COMPILE)
		gluPartialDisk(quadratic, 0, 1, 20, 4, 0, 225)
		glEndList()

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glEnable(GL_LIGHTING)
		glShadeModel(GL_SMOOTH)
		glTranslatef(-1, -1, 0)
		glCallList(self.startList)
		glShadeModel(GL_FLAT)
		glTranslatef(0, 2, 0)
		glPushMatrix()
		glRotatef(300, 1, 0, 0)
		glCallList(self.startList+1)
		glPopMatrix()
		glDisable(GL_LIGHTING)
		glColor3f(0, 1, 1)
		glTranslatef(2, -2, 0)
		glCallList(self.startList+2)
		glColor3f(1, 1, 0)
		glTranslatef(0, 2, 0)
		glCallList(self.startList+3)
		glPopMatrix()
		glFlush()

	def errorCallback(self, errorCode):
		print 'Quadric Error:' , gluErrorString(errorCode)
		exit(-1)

if __name__ == '__main__':
	Quadratic().run()
