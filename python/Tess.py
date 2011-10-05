'''Demonstrates polygon tessellation.'''
'''Two tesselated objects are drawn a rectangle with a triangular hole and a smooth shaded, self-intersecting star.'''
'''The exterior rectangle is drawn with its vertices in counter-clockwise order, but its interior clockwise.'''
'''combineCallback is needed for the self-intersecting star.'''
'''Removing the TessProperty for the star will make the interior unshaded (WINDING_ODD).'''

def __init__(self):
	self.rect = (	( 50,  50, 0),
			(200,  50, 0),
			(200, 200, 0),
			( 50, 200, 0),)
	self.tri = (	( 75,  75, 0),
			(125, 175, 0),
			(175,  75, 0),)
	self.star = (	(250,  50, 0, 1, 0, 1),
			(325, 200, 0, 1, 1, 0),
			(400,  50, 0, 0, 1, 1),
			(250, 150, 0, 1, 0, 0),
			(400, 150, 0, 0, 1, 0),)
	self.startList = glGenLists(2)
	self.tesselation = gluNewTess()
	gluTessCallback(self.tesselation, GLU_TESS_VERTEX, glVertex3dv)
	gluTessCallback(self.tesselation, GLU_TESS_BEGIN,  self.beginCallback)
	gluTessCallback(self.tesselation, GLU_TESS_END,    self.endCallback)
	gluTessCallback(self.tesselation, GLU_TESS_ERROR,  self.errorCallback)
	# Rectangle with a triangular hole inside.
	glNewList(self.startList, GL_COMPILE)
	glShadeModel(GL_FLAT)
	gluTessBeginPolygon(self.tesselation, None)
	gluTessBeginContour(self.tesselation)
	gluTessVertex(self.tesselation, rect[0], rect[0])
	gluTessVertex(self.tesselation, rect[1], rect[1])
	gluTessVertex(self.tesselation, rect[2], rect[2])
	gluTessVertex(self.tesselation, rect[3], rect[3])
	gluTessEndContour(self.tesselation)
	gluTessBeginContour(self.tesselation)
	gluTessVertex(self.tesselation, tri[0], tri[0])
	gluTessVertex(self.tesselation, tri[1], tri[1])
	gluTessVertex(self.tesselation, tri[2], tri[2])
	gluTessEndContour(self.tesselation)
	gluTessEndPolygon(self.tesselation)
	glEndList()
	gluTessCallback(self.tesselation, GLU_TESS_VERTEX,  vertexCallback)
	gluTessCallback(self.tesselation, GLU_TESS_BEGIN,   self.beginCallback)
	gluTessCallback(self.tesselation, GLU_TESS_END,     self.endCallback)
	gluTessCallback(self.tesselation, GLU_TESS_ERROR,   self.errorCallback)
	gluTessCallback(self.tesselation, GLU_TESS_COMBINE, self.combineCallback)
	# Smooth shaded, self-intersecting star.
	glNewList(startList + 1, GL_COMPILE)
	glShadeModel(GL_SMOOTH)
	gluTessProperty(self.tesselation, GLU_TESS_WINDING_RULE, GLU_TESS_WINDING_POSITIVE)
	gluTessBeginPolygon(self.tesselation, NULL)
	gluTessBeginContour(self.tesselation)
	gluTessVertex(self.tesselation, star[0], star[0])
	gluTessVertex(self.tesselation, star[1], star[1])
	gluTessVertex(self.tesselation, star[2], star[2])
	gluTessVertex(self.tesselation, star[3], star[3])
	gluTessVertex(self.tesselation, star[4], star[4])
	gluTessEndContour(self.tesselation)
	gluTessEndPolygon(self.tesselation)
	glEndList()
	gluDeleteTess(self.tesselation)

def display(self):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 1, 1)
	glCallList(startList)
	glCallList(startList + 1)
	glFlush()

def beginCallback(which):
	glBegin(which)

def error(errorCode):
	raise SystemError('Tessellation Error:', gluErrorString(errorCode))

def endCallback(self):
	glEnd()

def vertexCallback(vertex, color):
	glColor3d(*color)
	glVertex3d(*vertex)

def combineCallback(coords, vertexData, weight, dataOut):
	'''Creates a new vertex when edges intersect.'''
	'''Coordinate location is trivial to calculate,'''
	'''but weight[4] may be used to average color, normal, or texture  coordinate data.'''
	'''In this program, color is weighted.'''
	vertex = coords
	for i in range(3,7):
		vertex[i] = weight[0] * vertex_data[0][i]
			  + weight[1] * vertex_data[1][i]
			  + weight[2] * vertex_data[2][i]
			  + weight[3] * vertex_data[3][i]
	*dataOut = vertex
