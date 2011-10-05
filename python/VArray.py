'''Demonstrates vertex arrays.'''

def __init__(self):
	POINTER 1
	INTERLEAVED 2
	DRAWARRAY 1
	ARRAYELEMENT  2
	DRAWELEMENTS 3
	setupMethod = POINTER
	derefMethod = DRAWARRAY
	vertices = (25, 25, 100, 325, 175, 25, 175, 325, 250, 25, 325, 325)
	colors   = (1, 0.2, 0.2, 0.2, 0.2, 1, 0.8, 1, 0.2, 0.75, 0.75, 0.75, 0.35, 0.35, 0.35, 0.5, 0.5, 0.5)
	glEnableClientState(GL_VERTEX_ARRAY)
	glEnableClientState(GL_COLOR_ARRAY)
	glVertexPointer(2, GL_INT, 0, vertices)
	glColorPointer(3, GL_FLOAT, 0, colors)
	glutInitWindowSize(350, 350)

def display(self):
	glClear(GL_COLOR_BUFFER_BIT)
	if(derefMethod == DRAWARRAY)
		glDrawArrays(GL_TRIANGLES, 0, 6)
	else if(derefMethod == ARRAYELEMENT)
		glBegin(GL_TRIANGLES)
		glArrayElement(2)
		glArrayElement(3)
		glArrayElement(5)
		glEnd()
	else if(derefMethod == DRAWELEMENTS)
		indices[4] = (0, 1, 3, 4)
		glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_INT, indices)
	glFlush()

def mouseLeftClick(self, x, y):
	if   setupMethod == POINTER:
		setupMethod = INTERLEAVED
		setupInterleave()
	elif setupMethod == INTERLEAVED)
		setupMethod = POINTER
		setupPointers()

def mouseRightClick(self, x, y):
	if  derefMethod == DRAWARRAY:
		derefMethod = ARRAYELEMENT
	elif derefMethod == ARRAYELEMENT:
		derefMethod = DRAWELEMENTS
	elif derefMethod == DRAWELEMENTS:
		derefMethod = DRAWARRAY

def setupInterleave(self):
	intertwined = ( 1.0, 0.2, 1.0, 100, 100, 0,
			1.0, 0.2, 0.2,   0, 200, 0,
			1.0, 1.0, 0.2, 100, 300, 0,
			0.2, 1.0, 0.2, 200, 300, 0,
			0.2, 1.0, 1.0, 300, 200, 0,
			0.2, 0.2, 1.0, 200, 100, 0, )
	glInterleavedArrays(GL_C3F_V3F, 0, intertwined)
