#!/usr/bin/python

from Window import *

class Mipmap(Window):
	''' Demonstrates using mipmaps for texture maps.'''

	def __init__(self):
		super(Mipmap, self).__init__("mipmap.c", "Mipmap", 500, 500)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_FLAT)
		glTranslatef(0, 0, -3.6)
		self.makeImages()
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glGenTextures(1, self.texName)
		self.texName = glBindTexture(GL_TEXTURE_2D)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_NEAREST)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 32, 32, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.mipmap32)
		glTexImage2D(GL_TEXTURE_2D, 1, GL_RGBA, 16, 16, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.mipmap16)
		glTexImage2D(GL_TEXTURE_2D, 2, GL_RGBA,  8,  8, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.mipmap08)
		glTexImage2D(GL_TEXTURE_2D, 3, GL_RGBA,  4,  4, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.mipmap04)
		glTexImage2D(GL_TEXTURE_2D, 4, GL_RGBA,  2,  2, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.mipmap02)
		glTexImage2D(GL_TEXTURE_2D, 5, GL_RGBA,  1,  1, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.mipmap01)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glEnable(GL_TEXTURE_2D)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glBindTexture(GL_TEXTURE_2D, texName)
		glBegin(GL_QUADS)
		glTexCoord2f(0, 0)
		glVertex3f(-2, -1, 0)
		glTexCoord2f(0, 8)
		glVertex3f(-2, 1, 0)
		glTexCoord2f(8, 8)
		glVertex3f(2000, 1, -6000)
		glTexCoord2f(8, 0)
		glVertex3f(2000, -1, -6000)
		glEnd()
		glFlush()

	def makeImages(self):
		''' To overtly show the effect of mipmaps, each mipmap reduction level has a solidly colored, contrasting texture image.'''
		''' Thus, the quadrilateral is drawn with several different colors.'''
		self.mipmap32 = bytes[32][32]
		self.mipmap16 = bytes[16][16]
		self.mipmap08 = bytes[ 8][ 8]
		self.mipmap04 = bytes[ 4][ 4]
		self.mipmap02 = bytes[ 2][ 2]
		self.mipmap01 = bytes[ 1][ 1]
		for i in range(32):
			for j in range(32):
				self.mipmap32[i][j] = (255, 255,   0, 255)
		for i in range(16):
			for j in range(16):
				self.mipmap16[i][j] = (255,   0, 255, 255)
		for i in range(8):
			for i in range(8):
				self.mipmap08[i][j] = (255,   0,   0, 255)
		for i in range(4):
			for i in range(4):
				self.mipmap04[i][j] = (  0, 255,   0, 255)
		for i in range(2):
			for i in range(2):
				self.mipmap02[i][j] =  (  0,  0, 255, 255)
		for i in range(1):
			for i in range(1):
				self.mipmap01[0][0] = (255, 255, 255, 255)

if __name__ == '__main__':
	Mipmap().run()
