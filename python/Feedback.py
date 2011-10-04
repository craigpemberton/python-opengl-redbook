#!/usr/bin/python

from Window import *

class Feedback(Window):
	'''Demonstrates the use of OpenGL feedback.'''
	'''First, a lighting environment is set up and a few lines are drawn.'''
	'''Then feedback mode is entered, and the same lines are drawn.'''
	'''The results in the feedback buffer are printed.'''

	def __init__(self):
		'''Initialize lighting.'''
		super(Feedback, self).__init__("feedback.c", "Feedback", 100, 100)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)

	def display(self):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0, 100, 0, 100, 0, 1)
		glClearColor(0, 0, 0, 0)
		glClear(GL_COLOR_BUFFER_BIT)
		self.drawGeometry(GL_RENDER)
		feedBuffer = glFeedbackBuffer(1024, GL_3D_COLOR)
		glRenderMode(GL_FEEDBACK)
		self.drawGeometry(GL_FEEDBACK)
		size = len(glRenderMode(GL_RENDER))
		self.printBuffer(size, feedBuffer)

	def drawGeometry(self, mode):
		'''Draw a few lines and two points, one of which will be clipped.'''
		'''If in feedback mode, a passthrough token is issued between the each primitive.'''
		glBegin(GL_LINE_STRIP)
		glNormal3f( 0,  0, 1)
		glVertex3f(30, 30, 0)
		glVertex3f(50, 60, 0)
		glVertex3f(70, 40, 0)
		glEnd()
		if mode == GL_FEEDBACK:
			glPassThrough(1)
		glBegin(GL_POINTS)
		glVertex3f(-100, -100, -100) # will be clipped
		glEnd()
		if mode == GL_FEEDBACK:
			glPassThrough(2)
		glBegin(GL_POINTS)
		glNormal3f( 0,  0, 1)
		glVertex3f(50, 50, 0)
		glEnd()

	def print3DcolorVertex(self, size, count, buff):
		'''Print contents of one vertex.'''
		print '  '
		for i in range(7):
			print buff[size-(count)]
			count -= 1
		print
		return count

	def printBuffer(self, size, buff):
		'''Write contents of entire buffer. (Parse tokens!)'''
		count = size
		while(count):
			token = buff[size-count]
			count -= 1
			if(token == GL_PASS_THROUGH_TOKEN):
				print("GL_PASS_THROUGH_TOKEN\n")
				print("  %4.2f\n", buff[size-count])
				count -= 1
			elif(token == GL_POINT_TOKEN):
				print("GL_POINT_TOKEN\n")
				count = self.print3DcolorVertex(size, count, buff)
			elif(token == GL_LINE_TOKEN):
				print("GL_LINE_TOKEN\n")
				count = self.print3DcolorVertex(size, count, buff)
				count = self.print3DcolorVertex(size, count, buff)
			elif(token == GL_LINE_RESET_TOKEN):
				print("GL_LINE_RESET_TOKEN\n")
				count = self.print3DcolorVertex(size, count, buff)
				count = self.print3DcolorVertex(size, count, buff)

if __name__ == '__main__':
	Feedback().run()
