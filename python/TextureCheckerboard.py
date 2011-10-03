#!/usr/bin/python

from Window import *
import math

def makeCheckImage():
	'''Create checkerboard texture.'''
	width  = 64
	height = 64
	checkImage = height*[width*[0]]
	for i in range(height):
		for j in range(width):
			c = ( ((i&0x8)==0 ) ^ ((j&0x8)==0) )*0xFF
			checkImage[i][j] = (c<<24)|(c<<16)|(c<<8)|(0xFF)
	return checkImage

class TextureCheckerboard(Window):
	'''Texture maps a checkerboard image onto two rectangles.'''
	#XXX factor out a texture class
	#gluPerspective(60, (GLfloat) w/(GLfloat) h, 1, 30)
	#glTranslatef(0, 0, -3.6)

	def __init__(self):
		super(TextureCheckerboard, self).__init__("checker.c", "Texture Checkerboard", 250, 250, True)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glShadeModel(GL_FLAT)
		glEnable(GL_DEPTH_TEST)
		self.image = makeCheckImage()
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		self.texName = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.texName)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 64, 64, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.image)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glEnable(GL_TEXTURE_2D)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glBindTexture(GL_TEXTURE_2D, self.texName)
		glBegin(GL_QUADS)
		glTexCoord2f(0, 0)
		glVertex3f(-2, -1, 0)
		glTexCoord2f(0, 1)
		glVertex3f(-2, 1, 0)
		glTexCoord2f(1, 1)
		glVertex3f(0, 1, 0)
		glTexCoord2f(1, 0)
		glVertex3f(0, -1, 0)
		glTexCoord2f(0, 0)
		glVertex3f(1, -1, 0)
		glTexCoord2f(0, 1)
		glVertex3f(1, 1, 0)
		glTexCoord2f(1, 1)
		glVertex3f(1+math.sqrt(2), 1, -math.sqrt(2))
		glTexCoord2f(1, 0)
		glVertex3f(1+math.sqrt(2), -1, -math.sqrt(2))
		glEnd()
		glFlush()
		glDisable(GL_TEXTURE_2D)
	
if __name__ == '__main__':
	TextureCheckerboard().run()
