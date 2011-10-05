'''Demonstrates using glBindTexture() by creating and managing two textures.'''

def __init__(self):
	glutInitWindowSize(250, 250)
	glEnable(GL_DEPTH_TEST)
	makeCheckImages()
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glGenTextures(2, texName)
	glBindTexture(GL_TEXTURE_2D, texName[0])
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, checkImageWidth, checkImageHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, checkImage)
	glBindTexture(GL_TEXTURE_2D, texName[1])
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, checkImageWidth, checkImageHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, otherImage)
	glEnable(GL_TEXTURE_2D)

def display(self):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glBindTexture(GL_TEXTURE_2D, texName[0])
	glBegin(GL_QUADS)
	glTexCoord2f(0, 0)
	glVertex3f(-2, -1, 0)
	glTexCoord2f(0, 1)
	glVertex3f(-2, 1, 0)
	glTexCoord2f(1, 1)
	glVertex3f(0, 1, 0)
	glTexCoord2f(1, 0)
	glVertex3f(0, -1, 0)
	glEnd()
	glBindTexture(GL_TEXTURE_2D, texName[1])
	glBegin(GL_QUADS)
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

'''Create a checkerboard texture.'''
#define	checkImageWidth 64
#define	checkImageHeight 64
static GLubyte checkImage[checkImageHeight][checkImageWidth][4]
static GLubyte otherImage[checkImageHeight][checkImageWidth][4]
static texName[2]
def makeCheckImages(self):
	int i, j, c
	for(i = 0 i < checkImageHeight i++)
		for(j = 0 j < checkImageWidth j++)
			c = ( ((i&0x8)==0 ) ^ ((j&0x8)==0) )*255
			checkImage[i][j][0] = (GLubyte) c
			checkImage[i][j][1] = (GLubyte) c
			checkImage[i][j][2] = (GLubyte) c
			checkImage[i][j][3] = (GLubyte) 255
			c = ( ((i&0x10)==0 ) ^ ((j&0x10)==0) )*255
			otherImage[i][j][0] = (GLubyte) c
			otherImage[i][j][1] = (GLubyte) 0
			otherImage[i][j][2] = (GLubyte) 0
			otherImage[i][j][3] = (GLubyte) 255
