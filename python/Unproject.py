'''When the left mouse button is pressed, read the mouse position and determine two 3D points from which it was transformed.'''
'''Very little is displayed.'''

def display(self):
	glClear(GL_COLOR_BUFFER_BIT)
	glFlush()

def mouseLeftClick(self, x, y):
	viewport 	 = glGetIntegerv(GL_VIEWPORT)
	matrixModelView  = glGetDoublev(GL_MODELVIEW_MATRIX)
	matrixProjection = glGetDoublev(GL_PROJECTION_MATRIX)
	print 'Coordinates at cursor are', x, viewport[3] - y - 1
	print 'World coords at z=0 are', gluUnProject(x, realy, 0, matrixModelView, matrixProjection, viewport)
	print 'World coords at z=1 are', gluUnProject(x, realy, 1, matrixModelView, matrixProjection, viewport)
