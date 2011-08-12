#!/usr/bin/python

# XXX Reshape code....
# glOrtho(-1.5, 1.5, -1.5*(GLfloat)h/(GLfloat)w, 1.5*(GLfloat)h/(GLfloat)w, -10, 10)
# glOrtho(-1.5*(GLfloat)w/(GLfloat)h, 1.5*(GLfloat)w/(GLfloat)h, -1.5, 1.5, -10, 10)

from Window import *

class Alpha3D(Window):
	'''Intermix opaque and alpha blended polygons in the same scene by using glDepthMask..'''

	def __init__(self):
		'''Constructor'''
		super(Alpha3D, self).__init__("alpha3D.c", "Three Dimensional Alpha", 500, 500, 1.5)
		glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 0.15))
		glMaterialfv(GL_FRONT, GL_SHININESS, (100))
		glLightfv(GL_LIGHT0, GL_POSITION, (0.5, 0.5, 1, 0))
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)
		self.zMax		=  8
		self.zMin		= -8
		self.zIncrement		= 0.4
		self.zSolid		= self.zMax
		self.zTransparent	= self.zMin
		self.sphereList		= glGenLists(1)
		self.cubeList		= glGenLists(1)
		glNewList(self.sphereList, GL_COMPILE)
		glutSolidSphere(0.4, 16, 16)
		glEndList()
		glNewList(self.cubeList, GL_COMPILE)
		glutSolidCube(0.6)
		glEndList()
		self.keybindings['a'] = self.animate
		self.keybindings['r'] = self.reset

	def display(self):
		'''Render the polyhedra.'''
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glTranslatef(-0.15, -0.15, self.zSolid)
		glMaterialfv(GL_FRONT, GL_EMISSION, (0, 0, 0, 1)) # zero
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.75, 0.75, 0, 1)) # solid
		glCallList(self.sphereList)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(0.15, 0.15, self.zTransparent)
		glRotatef(15, 1, 1, 0)
		glRotatef(30, 0, 1, 0)
		glMaterialfv(GL_FRONT, GL_EMISSION, (0, 0.3, 0.3, 0.6)) # emission
		glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0.8, 0.8, 0.6)) # transparent
		glEnable(GL_BLEND)
		glDepthMask(GL_FALSE)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE)
		glCallList(self.cubeList)
		glDepthMask(GL_TRUE)
		glDisable(GL_BLEND)
		glPopMatrix()
		glutSwapBuffers()

	def reset(self):
		'''Press the 'r' key to reset the scene.'''
		self.zSolid		= self.zMax
		self.zTransparentZ	= self.zMin

	def animateLoop(self):
		'''Loop until objects are off screen.'''
		if (self.zSolid > self.zMin and self.zTransparent < self.zMax):
			self.zSolid		-= self.zIncrement
			self.zTransparentZ	+= self.zIncrement
			glutPostRedisplay()
		else:
			glutIdleFunc(None)

	def animate(self):
		'''Press the 'a' key to animate moving the transparent object through the opaque object.'''
		self.reset()
		glutIdleFunc(self.animateLoop)

if __name__ == '__main__':
	Alpha3D().run()
