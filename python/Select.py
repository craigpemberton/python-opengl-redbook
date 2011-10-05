'''Illustrations the selection mode and name stack, which detects whether objects which collide with a viewing volume.'''
'''First, four triangles and a rectangular box representing a viewing volume are drawn.'''
'''The green and yellow triangles appear to lie within the viewing volume, but the red triangle appears to lie outside it.'''
'''Then the selection mode is entered and drawing to the screen ceases.'''
'''To see if any collisions occur, the four triangles are called.'''
'''The green triangle causes one hit with the name 1, and the yellow triangles cause one hit with the name 3.'''

def __init__(self):
	glEnable(GL_DEPTH_TEST)
	glutInitWindowSize(200, 200)

def display(self):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	self.drawScene()
	self.selectObjects()
	glFlush()

def drawTriangle(self, x1, y1, x2, y2, x3, y3, z):
	'''Draw a triangle with vertices at (x1, y1), (x2, y2) and (x3, y3) at z units away from the origin.'''
	glBegin(GL_TRIANGLES)
	glVertex3f(x1, y1, z)
	glVertex3f(x2, y2, z)
	glVertex3f(x3, y3, z)
	glEnd()

def drawViewVolume(self, x1, x2, y1, y2, z1, z2):
	'''Draw a rectangular box with these outer x, y, and z values.'''
	glColor3f(1, 1, 1)
	glBegin(GL_LINE_LOOP)
	glVertex3f(x1, y1, -z1)
	glVertex3f(x2, y1, -z1)
	glVertex3f(x2, y2, -z1)
	glVertex3f(x1, y2, -z1)
	glEnd()
	glBegin(GL_LINE_LOOP)
	glVertex3f(x1, y1, -z2)
	glVertex3f(x2, y1, -z2)
	glVertex3f(x2, y2, -z2)
	glVertex3f(x1, y2, -z2)
	glEnd()
	glBegin(GL_LINES) # 4 lines
	glVertex3f(x1, y1, -z1)
	glVertex3f(x1, y1, -z2)
	glVertex3f(x1, y2, -z1)
	glVertex3f(x1, y2, -z2)
	glVertex3f(x2, y1, -z1)
	glVertex3f(x2, y1, -z2)
	glVertex3f(x2, y2, -z1)
	glVertex3f(x2, y2, -z2)
	glEnd()

'''Draws 4 triangles and a wire frame which represents the viewing volume.'''
def drawScene(self):
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(40, 4/3, 1, 100)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(7.5, 7.5, 12.5, 2.5, 2.5, -5, 0, 1, 0)
	glColor3f(0, 1, 0) # green triangle
	drawTriangle(2, 2, 3, 2, 2.5, 3, -5)
	glColor3f(1, 0, 0) # red triangle
	drawTriangle(2, 7, 3, 7, 2.5, 8, -5)
	glColor3f(1, 1, 0) # yellow triangles
	drawTriangle(2, 2, 3, 2, 2.5, 3, 0)
	drawTriangle(2, 2, 3, 2, 2.5, 3, -10)
	drawViewVolume(0, 5, 0, 5, 0, 10)

'''Print the contents of the selection array.''' 
def processHits(self, hits, buff):
	print 'hits = ', hits
	ptr = iter(buff)

	for hit in range(hits):
		names = ptr.next()
		print 'number of names for hit = ', names
		print 'z1 is', ptr.next()/0x7fffffff
		print 'z2 is', ptr.next()/0x7fffffff
		print 'the name is ',
		for name in range(names):
			print ptr.next()
		print

def selectObjects(self):
	'''Draw the triangles in selection mode, assigning names to the triangles.'''
	'''The third and fourth triangles share one name, so if both intersect the clipping volume only one hit will be registered.'''
	BUFSIZE = 512
	selectBuf[BUFSIZE]
	glSelectBuffer(BUFSIZE, selectBuf)
	glRenderMode(GL_SELECT)
	glInitNames()
	glPushName(0)
	glPushMatrix()
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, 5, 0, 5, 0, 10)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glLoadName(1)
	drawTriangle(2, 2, 3, 2, 2.5, 3, -5)
	glLoadName(2)
	drawTriangle(2, 7, 3, 7, 2.5, 8, -5)
	glLoadName(3)
	drawTriangle(2, 2, 3, 2, 2.5, 3, 0)
	drawTriangle(2, 2, 3, 2, 2.5, 3, -10)
	glPopMatrix()
	glFlush()
	hits = glRenderMode(GL_RENDER)
	processHits(hits, selectBuf)
