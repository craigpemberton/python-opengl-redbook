'''Draws a texture mapped teapot with automatically generated texture coordinates.'''
'''The texture is rendered as stripes on the teapot.'''
'''Initially, the object is drawn with texture coordinates based upon the object coordinates of the vertex and distance from the plane x = 0.'''

def __init__(self):
	''' Planes for texture coordinate generation.'''
	glutInitWindowSize(256, 256)
	texName
	xequalzero = (1, 0, 0, 0)
	slanted = (1, 1, 1, 0)
	currentCoeff
	currentPlane
	currentGenMode
	glEnable(GL_DEPTH_TEST)
	glShadeModel(GL_SMOOTH)
	makeStripeImage()
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glGenTextures(1, &texName)
	glBindTexture(GL_TEXTURE_1D, texName)
	glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexImage1D(GL_TEXTURE_1D, 0, GL_RGBA, stripeImageWidth, 0, GL_RGBA, GL_UNSIGNED_BYTE, stripeImage)
	glTexImage1D(GL_TEXTURE_1D, 0, 4, stripeImageWidth, 0, GL_RGBA, GL_UNSIGNED_BYTE, stripeImage)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	currentCoeff = xequalzero
	currentGenMode = GL_OBJECT_LINEAR
	currentPlane = GL_OBJECT_PLANE
	glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, currentGenMode)
	glTexGenfv(GL_S, currentPlane, currentCoeff)
	glEnable(GL_TEXTURE_GEN_S)
	glEnable(GL_TEXTURE_1D)
	glEnable(GL_CULL_FACE)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_AUTO_NORMAL)
	glEnable(GL_NORMALIZE)
	glFrontFace(GL_CW)
	glCullFace(GL_BACK)
	glMaterialf(GL_FRONT, GL_SHININESS, 64)
	self.keybindings['e'] = self.keye
	self.keybindings['o'] = self.keyo
	self.keybindings['s'] = self.keys
	self.keybindings['x'] = self.keyx

def display(self):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	glRotatef(45, 0, 0, 1)
	glBindTexture(GL_TEXTURE_1D, texName)
	glutSolidTeapot(2)
	glPopMatrix()
	glFlush()

def makeStripeImage(self):
	stripeImageWidth = 32
	stripeImage = [4*stripeImageWidth]
	for j in range(stripeImageWidth):
		stripeImage[4*j+0] = (GLubyte)((j<=4) ? 255 : 0)
		stripeImage[4*j+1] = (GLubyte)((j>4) ? 255 : 0)
		stripeImage[4*j+2] = (GLubyte) 0
		stripeImage[4*j+3] = (GLubyte) 255
	
def keye(self):
	'''Pressing the 'e' key changes the coordinate generation to eye coordinates of the vertex.'''
	currentGenMode = GL_EYE_LINEAR
	currentPlane = GL_EYE_PLANE
	glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, currentGenMode)
	glTexGenfv(GL_S, currentPlane, currentCoeff)

def keyo(self):
	'''Pressing the 'o' key switches it back to the object coordinates.'''
	currentGenMode = GL_OBJECT_LINEAR
	currentPlane = GL_OBJECT_PLANE
	glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, currentGenMode)
	glTexGenfv(GL_S, currentPlane, currentCoeff)

def keys(self):
	'''Pressing the 's' key changes the plane to a slanted one (x + y + z = 0).'''
	currentCoeff = slanted
	glTexGenfv(GL_S, currentPlane, currentCoeff)

def keyx(self):
	'''Pressing the 'x' key switches it back to x = 0.'''
	currentCoeff = xequalzero
	glTexGenfv(GL_S, currentPlane, currentCoeff)
