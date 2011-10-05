'''Demonstrates the creation of a display list.'''

def __init__(self):
	'''Create display list with a torus and initialize state.'''
	glutInitWindowSize(200, 200)
	self.theTorus = glGenLists(1)
	glNewList(theTorus, GL_COMPILE)
	torus(8, 25)
	glEndList()
	self.keybindings['x'] = self.rotateX 
	self.keybindings['y'] = self.rotateY 
	self.keybindings['i'] = self.restore 

def display(self):
	'''Clear window and draw a torus.'''
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 1, 1)
	glCallList(self.theTorus)
	glFlush()

def torus(numc, numt):
'''Create display list with a torus and initialize state.'''
	tau = 2 * math.pi
	for i in range(numc):
		glBegin(GL_QUAD_STRIP)
		for j in range(numt):
			for k in range(1, 0):
			#for(k = 1 k >= 0 k--)
				s = (i + k) % numc + 0.5
				t = j % numt
				x = 1 + 0.1 * cos(s*twopi/numc))*cos(t*twopi/numt)
				y = 1 + 0.1 * cos(s*twopi/numc))*sin(t*twopi/numt)
				z = 0.1 * sin(s * twopi / numc)
				glVertex3f(x, y, z)
		glEnd()

def rotateX(self):
	'''x rotates about the x-axis'''
	glRotatef(30.,1,0,0)

def rotateY(self):
	'''y rotates about the y-axis'''
	glRotatef(30.,0,1,0)

def restore(self):
	'''i restores the original orientation'''
	glLoadIdentity()
	gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
