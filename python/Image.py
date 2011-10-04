#!/usr/bin/python

from Window import *

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

class Image(Window):
	''' Demonstrates drawing pixels and the effect of glDrawPixels(), glCopyPixels(), and glPixelZoom().'''
	''' There is no attempt to prevent you from drawing over the original image.'''

	def __init__(self):
		super(Image, self).__init__("image.c", "Image", 250, 250)
		self.keybindings['z'] = self.zoomIn
		self.keybindings['Z'] = self.zoomOut
		self.keybindings['r'] = self.zoomReset
		self.zoomFactor = 1
		self.checkImage = makeCheckImage()
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glRasterPos2i(0, 0)
		glDrawPixels(64, 64, GL_RGB, GL_UNSIGNED_BYTE, self.checkImage)
		glFlush()

	def zoomReset(self):
		''' If you press the 'r' key, the original image and zoom factors are reset.'''
		self.zoomFactor = 1
		glutPostRedisplay()
		print "zoomFactor reset to 1"

	def zoomIn(self):
		''' If you press the 'z' or 'Z' keys, you change the zoom factors.'''
		self.zoomFactor += 0.5
		if(self.zoomFactor >= 3):
			self.zoomFactor = 3
		print "zoomFactor is now", self.zoomFactor

	def zoomOut(self):
		''' If you press the 'z' or 'Z' keys, you change the zoom factors.'''
		self.zoomFactor -= 0.5
		if(self.zoomFactor <= 0.5):
			self.zoomFactor = 0.5
		print "zoomFactor is now", self.zoomFactor

	def motion(self, x, y):
		''' Moving the mouse while pressing the mouse button will copy the image in the lower-left corner of the window'''
		''' to the mouse position, using the current pixel zoom factors.'''
		screeny = height - y
		glRasterPos2i(x, screeny)
		glPixelZoom(zoomFactor, zoomFactor)
		glCopyPixels(0, 0, checkImageWidth, checkImageHeight, GL_COLOR)
		glPixelZoom(1, 1)
		glFlush()

if __name__ == '__main__':
	Image().run()
