#!/usr/bin/python

from Window import *

class BitmapLetter(Window):
	'''Draws the bitmapped letter F on the screen several times to demonstrate the use of glBitmap().'''

	def __init__(self):
		super(BitmapLetter, self).__init__("drawf.c", "Bitmap Letter", 100, 100)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		#glOrtho(0, w, 0, h, -1, 1)
		self.rasters = ( 	0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00,
					0xc0, 0x00, 0xc0, 0x00, 0xff, 0x00,
					0xff, 0x00, 0xc0, 0x00, 0xc0, 0x00,
					0xc0, 0x00, 0xff, 0xc0, 0xff, 0xc0, )

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glRasterPos2i(20, 20)
		glBitmap(10, 12, 0, 0, 11, 0, self.rasters)
		glBitmap(10, 12, 0, 0, 11, 0, self.rasters)
		glBitmap(10, 12, 0, 0, 11, 0, self.rasters)
		glFlush()

if __name__ == '__main__':
	BitmapLetter().run()
