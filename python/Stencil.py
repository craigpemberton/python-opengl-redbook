'''Uses the stencil buffer for masking nonrectangular regions.'''
'''Whenever the window is redrawn, a value of 1 is drawn into a diamond-shaped region in the stencil buffer.'''
'''Elsewhere in the stencil buffer, the value is 0.'''
'''A blue sphere is drawn where the stencil value is 1, and yellow toruses are drawn where the stencil value is not 1.'''

def __init__(self):
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH | GLUT_STENCIL)
	# yellow
	self.yellowMaterial = 1
	glNewList(self.yellowMaterial, GL_COMPILE)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.7, 0.7, 0, 1)) 
	glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
	glMaterialf(GL_FRONT, GL_SHININESS, 64)
	glEndList()
	# blue
	self.blueMaterial
	glNewList(self.blueMaterial, GL_COMPILE)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.1, 0.1, 0.7, 1))
	glMaterialfv(GL_FRONT, GL_SPECULAR, (0.1, 1, 1, 1))
	glMaterialf(GL_FRONT, GL_SHININESS, 45)
	glEndList()
	# lighting
	glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
	glEnable(GL_LIGHT0)
	glEnable(GL_LIGHTING)
	# stencil
	glClearStencil(0x0)
	glEnable(GL_STENCIL_TEST)
	glEnable(GL_DEPTH_TEST)

def display(self):
	'''Draw a sphere in a diamond-shaped section in the middle of a window with 2 toruses.'''
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# Draw blue sphere where the stencil is 1.
	glStencilFunc(GL_EQUAL, 0x1, 0x1)
	glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
	glCallList(BLUEMAT)
	glutSolidSphere(0.5, 15, 15)
	# Draw the toruses where the stencil is not 1.
	glStencilFunc(GL_NOTEQUAL, 0x1, 0x1)
	glPushMatrix()
	glRotatef(45, 0, 0, 1)
	glRotatef(45, 0, 1, 0)
	glCallList(YELLOWMAT)
	glutSolidTorus(0.275, 0.85, 15, 15)
	glPushMatrix()
	glRotatef(90, 1, 0, 0)
	glutSolidTorus(0.275, 0.85, 15, 15)
	glPopMatrix()
	glPopMatrix()

def reshape(self, w, h):
	glViewport(0, 0, (GLsizei) w, (GLsizei) h)
	# Create a diamond shaped stencil area.
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if(w <= h)
		gluOrtho2D(-3, 3, -3*h/w, 3*h/w)
	else
		gluOrtho2D(-3*w/h, 3*w/h, -3, 3)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glClear(GL_STENCIL_BUFFER_BIT)
	glStencilFunc(GL_ALWAYS, 0x1, 0x1)
	glStencilOp(GL_REPLACE, GL_REPLACE, GL_REPLACE)
	glBegin(GL_QUADS)
	glVertex2f(-1, 0)
	glVertex2f(0, 1)
	glVertex2f(1, 0)
	glVertex2f(0, -1)
	glEnd()
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,  w/ h, 3, 7)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glTranslatef(0, 0, -5)
