#!/usr/bin/python

from Window import *

class PickSquares(Window):
	'''Demonstrate the use of multiple names and picking.'''

	def __init__(self):
		''' Clear color value for every square on the board.'''
		super(PickSquares, self).__init__('picksquare.c', 'Pick Squares', 500, 500)
		self.board = 3*[3*[0]] # Amount of color for each square.
		glutInitWindowSize(100, 100)
		glutMouseFunc(self.pickSquares)

	def display(self):
		'''A 3x3 grid of squares is drawn.'''
		glClear(GL_COLOR_BUFFER_BIT)
		self.drawSquares(GL_RENDER)
		glFlush()

	def drawSquares(self, mode):
		'''Nine squares are drawn.'''
		'''In selection mode, each square is given two names one for the row and the other for the column on the grid.'''
		''' The color of each square is determined by its position on the grid, and the value in the board.'''
		for i in range(3):
			if mode == GL_SELECT:
				glLoadName(i)
			for j in range(3):
				if mode == GL_SELECT:
					glPushName(j)
				glColor3f(i/3.0, j/3.0, self.board[i][j]/3.0)
				glRecti(i, j, i+1, j+1)
				if mode == GL_SELECT:
					glPopName()

	def processHits(self, hits, buff):
		'''Print the contents of the selection array.'''
		print 'hits = ', hits
		ptr = iter(buff)
		ii = 0
		jj = 0
		for hit in range(hits): # for each hit
			print 'number of names for this hit = ', ptr.next()
			print 'z1 is %g', ptr.next()/0x7fffffff
			print 'z2 is %g', ptr.next()/0x7fffffff
			print 'names are ',
			for name in range(names):
				print ptr.next(),
				if name == 0: # Set row and column.
					ii = ptr.get()
				elif j == 1:
					jj = ptr.get()
			print
			self.board[ii][jj] = (self.board[ii][jj] + 1) % 3

	def pickSquares(self, button, state, x, y):
		'''When the left mouse button is pressed, all squares under the cursor position have their color changed.'''
		''' Set up selection mode, name stack, and projection matrix for picking then draw the objects.'''
		BUFSIZE = 512
		selectBuf = BUFSIZE*[0]
		if(button != GLUT_LEFT_BUTTON or state != GLUT_DOWN):
			return
		viewport = glGetIntegerv(GL_VIEWPORT)
		glSelectBuffer(BUFSIZE, selectBuf)
		glRenderMode(GL_SELECT)
		glInitNames()
		glPushName(0)
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		# Create a 5x5 pixel picking region near cursor location.
		gluPickMatrix(x, (viewport[3] - y), 5, 5, viewport)
		gluOrtho2D(0, 3, 0, 3)
		drawSquares(GL_SELECT)
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glFlush()
		hits = glRenderMode(GL_RENDER)
		self.processHits(hits, selectBuf)
		glutPostRedisplay()

if __name__ == '__main__':
	PickSquares().run()
