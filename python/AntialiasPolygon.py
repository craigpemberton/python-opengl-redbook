#!/usr/bin/python
'''Antialias with polygon fill routines.'''

from Window import *

class AntialiasPolygon(Window):
	'''Draw filled polygons with antialiased edges using GL_SRC_ALPHA_SATURATE blending. 't' toggles antialiasing.'''

	def __init__(self):
		'''Set up blending options and polygon state.'''
		super(AntialiasPolygon, self).__init__( "aapoly.c", "Antialias Polygon", 200, 200)
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_ALPHA|GLUT_DEPTH)
		self.polySmooth = True
		self.nFaces = 6
		self.nVertexes = 8
		glCullFace(GL_BACK)
		glEnable(GL_CULL_FACE)
		glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)
		self.keybindings['t'] = self.toggle
		
	def toggle(self):
		'''Toggle the bool used by display().'''
		self.polySmooth = not self.polySmooth
		glutPostRedisplay()

	def drawCube(self, x0, x1, y0, y1, z0, z1):
		'''Draw a pretty cube.'''
		colors = (	(0, 0, 0, 1),
				(1, 0, 0, 1),
				(0, 1, 0, 1),
				(1, 1, 0, 1),
				(0, 0, 1, 1),
				(1, 0, 1, 1),
				(0, 1, 1, 1),
				(1, 1, 1, 1))
		indices = (	(4, 5, 6, 7),
				(2, 3, 7, 6),
				(0, 4, 7, 3),
				(0, 1, 5, 4),
				(1, 5, 6, 2),
				(0, 3, 2, 1))
		vertexes = (	(x0, y0, z0),
				(x1, y0, z0),
				(x1, y1, z0),
				(x0, y1, z0),
				(x0, y0, z1),
				(x1, y0, z1),
				(x1, y1, z1),
				(x0, y1, z1))
		glEnableClientState(GL_VERTEX_ARRAY)
		glEnableClientState(GL_COLOR_ARRAY)
		glVertexPointer(3, GL_FLOAT, 0, vertexes)
		glColorPointer(4, GL_FLOAT, 0, colors)
		glDrawElements(GL_QUADS, self.nFaces*4, GL_UNSIGNED_BYTE, indices)
		glDisableClientState(GL_VERTEX_ARRAY)
		glDisableClientState(GL_COLOR_ARRAY)

	def display(self):
		'''Polygons must be drawn from front to back for proper blending.'''
		if(self.polySmooth):
			glClear(GL_COLOR_BUFFER_BIT)
			glEnable(GL_BLEND)
			glEnable(GL_POLYGON_SMOOTH)
			glDisable(GL_DEPTH_TEST)
		else: 
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			glDisable(GL_BLEND)
			glDisable(GL_POLYGON_SMOOTH)
			glEnable(GL_DEPTH_TEST)
		glPushMatrix()
		glTranslatef(0, 0, -8)	 
		glRotatef(30, 1, 0, 0)
		glRotatef(60, 0, 1, 0) 
		self.drawCube(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5)
		glPopMatrix()
		glFlush()


if __name__ == '__main__':
	AntialiasPolygon().run()
