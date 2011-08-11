#!/usr/bin/python
'''Common code for redbook examples. Original source (c)1993-1997, Silicon Graphics, Inc.'''
from OpenGL.GL	 import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

def noop():
	'''A function that does nothing.'''
	pass

class Window(object):
	'''An abstract GLUT window.'''
	def __init__(self, title="Untitled Window", width=500, height=500, ortho=False):
		'''Constructs a window with the given title and dimensions.'''
		self.ortho  = ortho
		self.width  = width
		self.height = height
		self.keybindings = {chr(27):exit}
		glutInit()
		glutInitWindowSize(self.width, self.height)
		glutCreateWindow(title)
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA) #clobber in child to override
		glClearColor(0, 0, 0, 0)
		glutReshapeFunc(self.reshape)
		glutKeyboardFunc(self.keyboard)
		glutDisplayFunc(self.display)

	def keyboard(self, key, mouseX, mouseY):
		'''Call the code mapped to the pressed key.'''
		assert mouseX >= 0
		assert mouseY >= 0
		self.keybindings.get(key, noop)()
	
	def reshape(self, width, height):
		'''Recalculate the clipping window the GLUT window is resized.'''
		self.width  = width
		self.height = height
		glViewport(0, 0, self.width, self.height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		aspect = float(self.height)/float(self.width)
		if self.ortho:
			if(aspect > 1):
				gluOrtho2D(-1, 1, -aspect, aspect)
			else:
				gluOrtho2D(-1/aspect, 1/aspect, -1, 1.0)
		else:
			gluPerspective(30, 1.0/aspect, 1, 20)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def display(self):
		'''Children implement this to define their rendering behavior.'''
		raise NotImplementedError
	
	@staticmethod
	def run():
		'''Start up the main loop. Actually static right now but may one day want to change.'''
		glutMainLoop()

