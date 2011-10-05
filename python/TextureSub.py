'''Texture maps a checkerboard image onto two rectangles. Clamps the texture coordinates.'''

def __init__(self):
	self.texName
	glEnable(GL_DEPTH_TEST)
	makeCheckImages()
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glGenTextures(1, &texName)
	glBindTexture(GL_TEXTURE_2D, texName)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, checkImageWidth, checkImageHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, checkImage)
	glutInitWindowSize(250, 250)
	keybindings['s'] = self.keys
	keybindings['r'] = self.keyr

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

def keys(self):
	'''If 's' is pressed, a texture subimage is used to alter the original texture.'''
	glBindTexture(GL_TEXTURE_2D, texName)
	glTexSubImage2D(GL_TEXTURE_2D, 0, 12, 44, subImageWidth, subImageHeight, GL_RGBA, GL_UNSIGNED_BYTE, subImage)

def keyr(self):
	'''If 'r' is pressed, the original texture is restored.'''
	glBindTexture(GL_TEXTURE_2D, texName)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, checkImageWidth, checkImageHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, checkImage)

def makeCheckImages(self):
	'''Create checkerboard textures.'''
	checkImageWidth = 64
	checkImageHeight = 64
	subImageWidth = 16
	subImageHeight = 16
	checkImage = [checkImageHeight][checkImageWidth][4]
	subImage = [subImageHeight][subImageWidth][4]
	for(i = 0 i < checkImageHeight i++)
		for(j = 0 j < checkImageWidth j++)
			c = ( ((i&0x8)==0 ) ^ ((j&0x8)==0) )*255
			checkImage[i][j][0] = (GLubyte) c
			checkImage[i][j][1] = (GLubyte) c
			checkImage[i][j][2] = (GLubyte) c
			checkImage[i][j][3] = (GLubyte) 255
	for(i = 0 i < subImageHeight i++)
		for(j = 0 j < subImageWidth j++)
			c = ( ((i&0x4)==0 ) ^ ((j&0x4)==0) )*255
			subImage[i][j][0] = (GLubyte) c
			subImage[i][j][1] = (GLubyte) 0
			subImage[i][j][2] = (GLubyte) 0
			subImage[i][j][3] = (GLubyte) 255
