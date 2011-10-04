#!/usr/bin/python

from Window import *

class Planet(Window):
	'''Uses composite modeling transformations to draw translated and rotated models.'''

	def __init__(self):
		'''Pressing the d and y keys (day and year) alters the rotation of the planet around the sun.'''
		super(Planet, self).__init__("planet.c", "Planet", 500, 500)
		self.year = 0
		self.day = 0
		self.keybindings['d'] = self.dayInc
		self.keybindings['D'] = self.dayDec
		self.keybindings['y'] = self.yearInc
		self.keybindings['Y'] = self.yearDec

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glPushMatrix()
		glutWireSphere(1, 20, 16)  # sun
		glRotatef(self.year, 0, 1, 0)
		glTranslatef(2, 0, 0)
		glRotatef(self.day, 0, 1, 0)
		glutWireSphere(0.2, 10, 8) # planet
		glPopMatrix()
		glutSwapBuffers()

	def dayInc(self): #'d'
		self.day = (self.day + 10) % 360

	def dayDec(self): #'D'
		self.day = (self.day - 10) % 360

	def yearInc(self): #'y'
		self.year = (self.year + 5) % 360

	def yearDec(self): #'Y'
		self.year = (self.year - 5) % 360

if __name__ == '__main__':
	Planet().run()
