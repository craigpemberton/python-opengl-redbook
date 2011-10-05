'''Demonstrates the winding rule polygon tessellation property.'''
'''Four tessellated objects are drawn, each with very different contours.'''
'''When the 'w' is pressed, the objects are drawn with a different winding rule.'''

def __init__(self):
	self.currentShape = 0
	self.tobj = gluNewTess()
	gluTessCallback(tobj, GLU_TESS_VERTEX, glVertex3dv)
	gluTessCallback(tobj, GLU_TESS_BEGIN, beginCallback)
	gluTessCallback(tobj, GLU_TESS_END, endCallback)
	gluTessCallback(tobj, GLU_TESS_ERROR, errorCallback)
	gluTessCallback(tobj, GLU_TESS_COMBINE, combineCallback)
	self.list = glGenLists(4)
	makeNewLists()
	self.currentWinding = GLU_TESS_WINDING_ODD
	self.keybindings['w'] = toggleWinding

def display(self):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 1, 1)
	glPushMatrix()
	glCallList(list)
	glTranslatef(0, 500, 0)
	glCallList(list+1)
	glTranslatef(500, -500, 0)
	glCallList(list+2)
	glTranslatef(0, 500, 0)
	glCallList(list+3)
	glPopMatrix()
	glFlush()

def makeNewLists(self):
	'''Make four display lists, each with a different tessellated object.'''
	rects = (	(  50, 50, 0),
			( 300, 50, 0),
			(300, 300, 0),
			( 50, 300, 0),
			(100, 100, 0),
			(250, 100, 0),
			(250, 250, 0),
			(100, 250, 0),
			(150, 150, 0),
			(200, 150, 0),
			(200, 200, 0),
			(150, 200, 0),)
	spiral = (	(400, 250, 0),
			(400,  50, 0),
			( 50,  50, 0),
			( 50, 400, 0),
			(350, 400, 0),
			(350, 100, 0),
			(100, 100, 0),
			(100, 350, 0),
			(300, 350, 0),
			(300, 150, 0),
			(150, 150, 0),
			(150, 300, 0),
			(250, 300, 0),
			(250, 200, 0),
			(200, 200, 0),
			(200, 250, 0),)
	quad1 = (	( 50, 150, 0),
			(350, 150, 0),
			(350, 200, 0),
			( 50, 200, 0),)
	quad2 = (	(100, 100, 0),
			(300, 100, 0),
			(300, 350, 0),
			(100, 350, 0),)
	tri = (		(200,  50, 0),
			(250, 300, 0),
			(150, 300, 0),)
	gluTessProperty(self.tobj, GLU_TESS_WINDING_RULE, currentWinding)
	glNewList(self.list, GL_COMPILE)
	gluTessBeginPolygon(self.tobj, NULL)
	gluTessBeginContour(tobj)
	for i in range(4):
		gluTessVertex(tobj, rects[i], rects[i])
	gluTessEndContour(tobj)
	gluTessBeginContour(tobj)
	for i in range(4, 8):
		gluTessVertex(tobj, rects[i], rects[i])
	gluTessEndContour(tobj)
	gluTessBeginContour(tobj)
	for i in range(8, 12):
		gluTessVertex(tobj, rects[i], rects[i])
	gluTessEndContour(tobj)
	gluTessEndPolygon(tobj)
	glEndList()
	glNewList(list+1, GL_COMPILE)
	gluTessBeginPolygon(tobj, NULL)
	gluTessBeginContour(tobj)
	for i in range(4):
		gluTessVertex(tobj, rects[i], rects[i])
	gluTessEndContour(tobj)
	gluTessBeginContour(tobj)
	for i in range(7, 4):
	#for(i = 7 i >= 4 i--)
		gluTessVertex(tobj, rects[i], rects[i])
	gluTessEndContour(tobj)
	gluTessBeginContour(tobj)
	for i in range(11, 8):
	#for(i = 11 i >= 8 i--)
		gluTessVertex(tobj, rects[i], rects[i])
	gluTessEndContour(tobj)
	gluTessEndPolygon(tobj)
	glEndList()
	glNewList(list+2, GL_COMPILE)
	gluTessBeginPolygon(tobj, NULL)
	gluTessBeginContour(tobj)
	for i in range(16):
		gluTessVertex(tobj, spiral[i], spiral[i])
	gluTessEndContour(tobj)
	gluTessEndPolygon(tobj)
	glEndList()
	glNewList(list+3, GL_COMPILE)
	gluTessBeginPolygon(tobj, NULL)
	gluTessBeginContour(tobj)
	for i in range(4):
		gluTessVertex(tobj, quad1[i], quad1[i])
	gluTessEndContour(tobj)
	gluTessBeginContour(tobj)
	for i in range(4):
		gluTessVertex(tobj, quad2[i], quad2[i])
	gluTessEndContour(tobj)
	gluTessBeginContour(tobj)
	for i in range(3):
		gluTessVertex(tobj, tri[i], tri[i])
	gluTessEndContour(tobj)
	gluTessEndPolygon(tobj)
	glEndList()

def beginCallback(GLenum which)
	glBegin(which)

def errorCallback(errorCode)
	raise SystemError('Tessellation Error:', gluErrorString(errorCode))

def endCallback(self):
	glEnd()

def combineCallback(coords, data, weight, dataOut):
	'''Creates a new vertex when edges intersect.'''
	'''Coordinate location is trivial to calculate, '''
	'''but weight[4] may be used to average color, normal, or texture coordinate data.'''
	dataOut[0] = coords

def toggleWinding(self):
	if(currentWinding == GLU_TESS_WINDING_ODD)
		currentWinding = GLU_TESS_WINDING_NONZERO
	elif(currentWinding == GLU_TESS_WINDING_NONZERO)
		currentWinding = GLU_TESS_WINDING_POSITIVE
	elif(currentWinding == GLU_TESS_WINDING_POSITIVE)
		currentWinding = GLU_TESS_WINDING_NEGATIVE
	elif(currentWinding == GLU_TESS_WINDING_NEGATIVE)
		currentWinding = GLU_TESS_WINDING_ABS_GEQ_TWO
	elif(currentWinding == GLU_TESS_WINDING_ABS_GEQ_TWO)
		currentWinding = GLU_TESS_WINDING_ODD
	makeNewLists()
