'''Texture maps a checkerboard image onto two rectangles. '''
'''Demonstrates the wrapping modes if the texture coordinates fall outside 0 and 1.'''

def __init__(self):
	glutInitWindowSize(250, 250)
	glEnable(GL_DEPTH_TEST)
	makeCheckImage()
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glGenTextures(1, &texName)
	glBindTexture(GL_TEXTURE_2D, texName)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, checkImageWidth, checkImageHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, checkImage)

def display(self):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glEnable(GL_TEXTURE_2D)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	glBindTexture(GL_TEXTURE_2D, texName)
	glBegin(GL_QUADS)
	glTexCoord2f(0, 0)
	glVertex3f(-2, -1, 0)
	glTexCoord2f(0, 3)
	glVertex3f(-2, 1, 0)
	glTexCoord2f(3, 3)
	glVertex3f(0, 1, 0)
	glTexCoord2f(3, 0)
	glVertex3f(0, -1, 0)
	glTexCoord2f(0, 0)
	glVertex3f(1, -1, 0)
	glTexCoord2f(0, 3)
	glVertex3f(1, 1, 0)
	glTexCoord2f(3, 3)
	glVertex3f(2.41421, 1, -1.41421)
	glTexCoord2f(3, 0)
	glVertex3f(2.41421, -1, -1.41421)
	glEnd()
	glFlush()
	glDisable(GL_TEXTURE_2D)

def makeCheckImage(self):
	'''Create a checkerboard texture.'''
	#define	checkImageWidth 64
	#define	checkImageHeight 64
	static GLubyte checkImage[checkImageHeight][checkImageWidth][4]
	static texName
	for(i = 0 i < checkImageHeight i++)
		for(j = 0 j < checkImageWidth j++)
			c = ( ((i&0x8)==0 ) ^ ((j&0x8)==0) )*255
			checkImage[i][j][0] = (GLubyte) c
			checkImage[i][j][1] = (GLubyte) c
			checkImage[i][j][2] = (GLubyte) c
			checkImage[i][j][3] = (GLubyte) 255

'''Pressing the 's' and 'S' keys switch the wrapping between clamping and repeating for the s parameter.'''
'''The 't' and 'T' keys control the wrapping for the t parameter.'''
case 's':
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)

case 'S':
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)

case 't':
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

case 'T':
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

