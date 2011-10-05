'''Draws a NURBS surface in the shape of a symmetrical hill, using both a NURBS curve and pwl (piecewise linear) curve to trim part of the surface.'''

def init(self):
	'''Initialize material property and depth buffer.'''
	self.ctlpoints = [4][4][3]
	self.theNurb
	mat_diffuse = (0.7, 0.7, 0.7, 1)
	mat_specular = (1, 1, 1, 1)
	mat_shininess = (100)
	glClearColor(0, 0, 0, 0)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_AUTO_NORMAL)
	glEnable(GL_NORMALIZE)
	init_surface()
	theNurb = gluNewNurbsRenderer()
	gluNurbsProperty(theNurb, GLU_SAMPLING_TOLERANCE, 25)
	gluNurbsProperty(theNurb, GLU_DISPLAY_MODE, GLU_FILL)
	gluNurbsCallback(theNurb, GLU_ERROR, nurbsError)

def display(self):
	knots		= (0, 0, 0, 0, 1, 1, 1, 1)
	edgePt		= ((0, 0), (1, 0), (1, 1), (0, 1), (0, 0)) # counter clockwise
	curvePt		= ((0.25, 0.5), (0.25, 0.75), (0.75, 0.75), (0.75, 0.5)) # clockwise
	curveKnots	= (0, 0, 0, 0, 1, 1, 1, 1)
	pwlPt		= ((0.75, 0.5), (0.5, 0.25), (0.25, 0.5))  # clockwise
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	glRotatef(330, 1, 0, 0)
	glScalef(0.5, 0.5, 0.5)
	gluBeginSurface(theNurb)
	gluNurbsSurface(theNurb, 8, knots, 8, knots, 4*3, 3, &ctlpoints[0][0][0], 4, 4, GL_MAP2_VERTEX_3)
	gluBeginTrim(theNurb)
	gluPwlCurve(theNurb, 5, &edgePt[0][0], 2, GLU_MAP1_TRIM_2)
	gluEndTrim(theNurb)
	gluBeginTrim(theNurb)
	gluNurbsCurve(theNurb, 8, curveKnots, 2, &curvePt[0][0], 4, GLU_MAP1_TRIM_2)
	gluPwlCurve(theNurb, 3, &pwlPt[0][0], 2, GLU_MAP1_TRIM_2)
	gluEndTrim(theNurb)
	gluEndSurface(theNurb)
	glPopMatrix()
	glFlush()

def initSurface(self):
	''' Initialize the control points of the surface to a small hill.'''
	''' The control points range from -3 to +3 in x, y, and z'''
	for u in range(4):
		for v in range(4):
			self.ctlpoints[u][v][0] = 2*(u - 1.5)
			self.ctlpoints[u][v][1] = 2*(v - 1.5)
			if((u == 1 || u == 2) && (v == 1 || v == 2))
				ctlpoints[u][v][2] = 3
			else
				ctlpoints[u][v][2] = -3

def nurbsError(errorCode)
	const GLubyte *estring
	estring = gluErrorString(errorCode)
	fprint stderr, 'Nurbs Error: %s\n', estring)
	exit(0)
