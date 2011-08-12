#!/usr/bin/python
'''Abstract GLUT window that takes care of all the busy work.'''

from OpenGL.GL	 import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

def noop():
	'''A function that does nothing.'''
	pass

class Window(object):
	'''An abstract GLUT window.'''
	def __init__(self, source=None, title="Untitled Window", width=500, height=500, ortho=None):
		'''Constructs a window with the given title and dimensions. Source is the original redbook file.'''
		self.source = source
		self.ortho  = ortho
		self.width  = width
		self.height = height
		self.keybindings = {chr(27):exit}
		glutInit()
		glutInitWindowSize(self.width, self.height)
		glutCreateWindow(title)
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA) #XXX clobber in child to override
		glClearColor(0, 0, 0, 0)
		glutReshapeFunc(self.reshape)
		glutKeyboardFunc(self.keyboard)
		glutDisplayFunc(self.display)

	def keyboard(self, key, mouseX, mouseY):
		'''Call the code mapped to the pressed key.'''
		self.keybindings.get(key, noop)()
		glutPostRedisplay()
	
	def reshape(self, width, height):
		'''Recalculate the clipping window the GLUT window is resized.'''
		self.width  = width
		self.height = height
		glViewport(0, 0, self.width, self.height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		aspect = float(self.height)/float(self.width)
		# ortho is the scaling factor for the orthogonal projection
		if self.ortho:
			if(aspect > 1):
				gluOrtho2D(-self.ortho, self.ortho, -aspect, aspect)
			else:
				gluOrtho2D(-1/aspect, 1/aspect, -self.ortho, self.ortho)
		else:
			gluPerspective(30, 1.0/aspect, 1, 20)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def display(self):
		'''Children implement this to define their rendering behavior.'''
		raise NotImplementedError
	
	@staticmethod
	def run():
		'''Start up the main loop.'''
		glutMainLoop()

