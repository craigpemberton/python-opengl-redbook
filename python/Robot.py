#!/usr/bin/python

from Window import *

class Robot(Window):
	'''Shows how to composite modeling transformations to draw translated and rotated hierarchical models.'''

	def __init__(self):
		'''Pressing the s and e keys (shoulder and elbow) alters the rotation of the robot arm.'''
		super(Robot, self).__init__("robot.c", "Robot", 500, 500)
		self.shoulder = 0
		self.elbow = 0
		self.keybindings['s'] = self.keys
		self.keybindings['S'] = self.keyS
		self.keybindings['e'] = self.keye
		self.keybindings['E'] = self.keyE

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glPushMatrix()
		glTranslatef(-1, 0, 0)
		glRotatef(self.shoulder, 0, 0, 1)
		glTranslatef(1, 0, 0)
		glPushMatrix()
		glScalef(2, 0.4, 1)
		glutWireCube(1)
		glPopMatrix()
		glTranslatef(1, 0, 0)
		glRotatef(self.elbow, 0, 0, 1)
		glTranslatef(1, 0, 0)
		glPushMatrix()
		glScalef(2, 0.4, 1)
		glutWireCube(1)
		glPopMatrix()
		glPopMatrix()
		glutSwapBuffers()

	def keys(self):
		self.shoulder = (self.shoulder + 5) % 360

	def keyS(self):
		self.shoulder = (self.shoulder - 5) % 360

	def keye(self):
		self.elbow = (self.elbow + 5) % 360

	def keyE(self):
		self.elbow = (self.elbow - 5) % 360

if __name__ == '__main__':
	Robot().run()
