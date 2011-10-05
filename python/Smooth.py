'''Demonstrates smooth shading. A smooth shaded polygon is drawn in a 2D projection.'''

def __init__(self):
	glutInitWindowSize(500, 500)

def display(self):
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glColor3f(1, 0, 0)
	glVertex2f(5, 5)
	glColor3f(0, 1, 0)
	glVertex2f(25, 5)
	glColor3f(0, 0, 1)
	glVertex2f(5, 25)
	glEnd()
	glFlush()
