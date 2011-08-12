'''Texture maps a checkerboard image onto two rectangles.'''

	def init(self):
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
		glutInitWindowSize(250, 250)
		glShadeModel(GL_FLAT)
		glEnable(GL_DEPTH_TEST)
		makeCheckImage()
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glGenTextures(1, texName)
		glBindTexture(GL_TEXTURE_2D, texName)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, checkImageWidth, checkImageHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, checkImage)
		self.textureSize = 64

	def makeCheckImage(self):
	'''Create checkerboard texture.'''
		checkImage = [self.textureSize][self.textureSize]
		for i in range(self.textureSize):
			for j in range(self.textureSize):
				c = ((((i&0x8)==0)^((j&0x8))==0))*255
				checkImage[i][j] = (c, c, c, 255)
		return checkImage

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glEnable(GL_TEXTURE_2D)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glBindTexture(GL_TEXTURE_2D, texName)
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
		glVertex3f(2.41421, 1, -1.41421)
		glTexCoord2f(1, 0)
		glVertex3f(2.41421, -1, -1.41421)
		glEnd()
		glFlush()
		glDisable(GL_TEXTURE_2D)

	def reshape(self, int w, int h):
		glViewport(0, 0, w, h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(60, w/h, 1, 30)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef(0, 0, -3.6)

