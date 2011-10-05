'''Draws a NURBS surface in the shape of a symmetrical hill.'''
'''Some of the control points are hidden by the surface itself.'''

def __init__(self):
	'''Initialize material property and depth buffer.'''
	glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
	glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
	glMaterialfv(GL_FRONT, GL_SHININESS, (100))
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_AUTO_NORMAL)
	glEnable(GL_NORMALIZE)
	self.ctlpoints = initSurface()
	self.nurb = gluNewNurbsRenderer()
	gluNurbsProperty(self.nurb, GLU_SAMPLING_TOLERANCE, 25)
	gluNurbsProperty(self.nurb, GLU_DISPLAY_MODE, GLU_FILL)
	gluNurbsCallback(self.nurb, GLU_ERROR, self.nurbsError)
	self.showPoints = 0
	self.keybindings['c'] = self.toggleShowPoints

def display(self):
	knots[8] = (0, 0, 0, 0, 1, 1, 1, 1
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	glRotatef(330, 1, 0, 0)
	glScalef(0.5, 0.5, 0.5)
	gluBeginSurface(self.nurb)
	gluNurbsSurface(self.nurb, 8, knots, 8, knots, 4*3, 3, &ctlpoints[0][0][0], 4, 4, GL_MAP2_VERTEX_3)
	gluEndSurface(self.nrb)
	if(self.showPoints):
		glPointSize(5)
		glDisable(GL_LIGHTING)
		glColor3f(1, 1, 0)
		glBegin(GL_POINTS)
		for i in range(4):
			for j in range(4):
				glVertex3f(*self.ctlpoints[i][j])
		glEnd()
		glEnable(GL_LIGHTING)	
	glPopMatrix()
	glFlush()

def initSurface(self):
	'''Initialize the control points of the surface to a small hill.'''
	'''The control points range from -3 to +3 in x, y, and z.'''
	ctlpoints[4][4][3]
	for u in range(4):
		for v in range(4):
			ctlpoints[u][v][0] = 2 * (u - 1.5)
			ctlpoints[u][v][1] = 2 * (v - 1.5)
			if u in (1,2) and v in (1,2):
				ctlpoints[u][v][2] =  3
			elif:
				ctlpoints[u][v][2] = -3
	return ctlpoints

def nurbsError(errorCode):
	raise SystemError('Nurbs Error:', gluErrorString(errorCode))

def toggleShowPoints():
	'''The 'c' keyboard key allows you to toggle the visibility of the control points themselves.'''
	self.showPoints = not self.showPoints
