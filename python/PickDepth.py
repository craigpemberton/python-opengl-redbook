#!/usr/bin/python

from Window import *

class PickDepth(Window):
	'''Picking demonstration.'''
	'''In rendering mode, three overlapping rectangles are drawn.'''
	'''When the left mouse button is pressed, selection mode is entered with the picking matrix.'''
	'''Rectangles which are drawn under the cursor position are "picked."'''
	'''Pay special attention to the depth value range which is returned.'''

	def __init__(self):
		super(PickDepth, self).__init__("pickdepth.c", "Pick Depth", 200, 200)
		glEnable(GL_DEPTH_TEST)
		glDepthRange(0, 1) # The default z mapping.
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glutMouseFunc(self.pickRectangles)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.drawRectangles(GL_RENDER)
		glFlush()

	def drawRectangles(self, mode):
		'''Three rectangles are drawn.'''
		'''In selection mode, each rectangle is given the same name.'''
		'''Each rectangle is drawn with a different z value.'''
		if mode == GL_SELECT:
			glLoadName(1)
		glBegin(GL_QUADS)
		glColor3f(1, 1, 0)
		glVertex3i(2, 0, 0)
		glVertex3i(2, 6, 0)
		glVertex3i(6, 6, 0)
		glVertex3i(6, 0, 0)
		glEnd()
		if mode == GL_SELECT:
			glLoadName(2)
		glBegin(GL_QUADS)
		glColor3f(0, 1, 1)
		glVertex3i(3, 2, -1)
		glVertex3i(3, 8, -1)
		glVertex3i(8, 8, -1)
		glVertex3i(8, 2, -1)
		glEnd()
		if mode == GL_SELECT:
			glLoadName(3)
		glBegin(GL_QUADS)
		glColor3f(1, 0, 1)
		glVertex3i(0, 2, -2)
		glVertex3i(0, 7, -2)
		glVertex3i(5, 7, -2)
		glVertex3i(5, 2, -2)
		glEnd()

	def processHits(self, hits, buff):
		'''Print the contents of the selection array.'''
		ptr = iter(buff)
		help(ptr)
		print 'hits', hits
		for hit in range(hits): #for each hit
			print 'number of names for hit = ', ptr.next()
			print 'z1 is', ptr.next()/0x7fffffff
			print 'z2 is', ptr.next()/0x7fffffff
			print 'the name is ',
			for name in range(names):
				print ptr.next(),
			print

	def pickRectangles(self, button, state, x, y):
		'''Set up selection mode, name stack, and projection matrix for picking then draw the objects.'''
		BUFSIZE = 512
		selectBuf = [0]*BUFSIZE
		if(button != GLUT_LEFT_BUTTON or state != GLUT_DOWN):
			return
		viewport = glGetIntegerv(GL_VIEWPORT)
		selectBuf = glSelectBuffer(BUFSIZE, selectBuf)
		glRenderMode(GL_SELECT)
		glInitNames()
		glPushName(0)
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		# Create a 5x5 pixel picking region near cursor location.
		gluPickMatrix(x, (viewport[3] - y), 5, 5, viewport)
		glOrtho(0, 8, 0, 8, -0.5, 2.5)
		self.drawRectangles(GL_SELECT)
		glPopMatrix()
		glFlush()
		hits = glRenderMode(GL_RENDER)
		self.processHits(hits, selectBuf)

if __name__ == '__main__':
	PickDepth().run()
