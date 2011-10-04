#!/usr/bin/python

from Window import *

class Lines(Window):
	'''Demonstrates geometric primitives and their attributes.'''

	def __init__(self):
		super(Lines, self).__init__("lines.c", "Lines", 400, 150)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		# Select white for all lines.
		glColor3f(1, 1, 1)
		# In 1st row, 3 lines, each with a different stipple.
		glEnable(GL_LINE_STIPPLE)
		glLineStipple(1, 0x0101) # dotted 
		self.drawOneLine(50, 125, 150, 125)
		glLineStipple(1, 0x00FF) # dashed
		self.drawOneLine(150, 125, 250, 125)
		glLineStipple(1, 0x1C47) # dash dot dash
		self.drawOneLine(250, 125, 350, 125)
		# In 2nd row, 3 wide lines, each with different stipple.
		glLineWidth(5)
		glLineStipple(1, 0x0101) # dotted
		self.drawOneLine(50, 100, 150, 100)
		glLineStipple(1, 0x00FF) # dashed
		self.drawOneLine(150, 100, 250, 100)
		glLineStipple(1, 0x1C47) # dash dot dash
		self.drawOneLine(250, 100, 350, 100)
		glLineWidth(1)
		# In 3rd row, 6 lines, with dash dot dash stipple as part of a single connected line strip.
		glLineStipple(1, 0x1C47) # dash dot dash
		glBegin(GL_LINE_STRIP)
		for i in range(1,8):
			glVertex2f(i * 50, 75)
		glEnd()
		# In 4th row, 6 independent lines with same stipple.
		for i in range(1, 7):
			self.drawOneLine(i*50, 50, (i+1)*50, 50)
		# In 5th row, 1 line, with dash dot dash stipple and a stipple repeat factor of 5.
		glLineStipple(5, 0x1C47) # dash dot dash
		self.drawOneLine(50, 25, 350, 25)
		glDisable(GL_LINE_STIPPLE)
		glFlush()

	def drawOneLine(self, x1, y1, x2, y2):
		glBegin(GL_LINES)
		glVertex2f(x1, y1)
		glVertex2f(x2, y2)
		glEnd()

if __name__ == '__main__':
	Lines().run()
