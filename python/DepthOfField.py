'''Use the accumulation buffer to create an out-of-focus depth-of-field effect.'''
'''The teapots are drawn several times into the accumulation buffer.'''
'''The viewing volume is jittered, except at the focal point where the viewing volume is at the same position each time.'''
'''In this case, the gold teapot remains in focus.'''

import "jitter.h"
#define PI_ 3.14159265358979323846

GLuint teapotList

'''The first 6 arguments are identical to the glFrustum() call.'''
'''pixdx and pixdy are anti-alias jitter in pixels.	Set both equal to 0 for no anti-alias jitter.'''
'''eyedx and eyedy are depth-of field jitter in pixels.	Set both equal to 0 for no depth of field effects.'''
'''focus is distance from eye to plane in focus.	focus must be greater than, but not equal to 0.'''
'''Note that accFrustum() calls glTranslatef().'''
void accFrustum(GLdouble left, GLdouble right, GLdouble bottom,	GLdouble top, GLdouble near, GLdouble far, GLdouble pixdx,
	GLdouble pixdy, GLdouble eyedx, GLdouble eyedy, GLdouble focus)
{
	GLdouble xwsize, ywsize
	GLdouble dx, dy
	GLint viewport[4]
	glGetIntegerv(GL_VIEWPORT, viewport)
	xwsize = right - left
	ywsize = top - bottom
	dx = -(pixdx*xwsize/(GLdouble) viewport[2] + eyedx*near/focus)
	dy = -(pixdy*ywsize/(GLdouble) viewport[3] + eyedy*near/focus)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glFrustum(left + dx, right + dx, bottom + dy, top + dy, near, far)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glTranslatef(-eyedx, -eyedy, 0)
}

'''The first 4 arguments are identical to the gluPerspective() call.'''
'''pixdx and pixdy are anti-alias jitter in pixels.	Set both equal to 0 for no anti-alias jitter.'''
'''eyedx and eyedy are depth-of field jitter in pixels.	Set both equal to 0 for no depth of field effects.'''
'''focus is distance from eye to plane in focus.	focus must be greater than, but not equal to 0.'''
'''Note that accPerspective() calls accFrustum().'''
void accPerspective(GLdouble fovy, GLdouble aspect, GLdouble near, GLdouble far, GLdouble pixdx, GLdouble pixdy,
	GLdouble eyedx, GLdouble eyedy, GLdouble focus)
{
	GLdouble fov2,left,right,bottom,top
	fov2 = ((fovy*PI_) / 180) / 2
	top = near / (cos(fov2) / sin(fov2))
	bottom = -top
	right = top * aspect
	left = -right
	accFrustum(left, right, bottom, top, near, far, pixdx, pixdy, eyedx, eyedy, focus)
}

void init(void)
{
	GLfloat ambient[] = { 0, 0, 0, 1 }
	GLfloat diffuse[] = { 1, 1, 1, 1 }
	GLfloat position[] = { 0, 3, 3, 0 }
	GLfloat lmodel_ambient[] = { 0.2, 0.2, 0.2, 1 }
	GLfloat local_view[] = { 0 }
	glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
	glLightfv(GL_LIGHT0, GL_POSITION, position)
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)
	glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, local_view)
	glFrontFace(GL_CW)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_AUTO_NORMAL)
	glEnable(GL_NORMALIZE)
	glEnable(GL_DEPTH_TEST)
	glClearColor(0, 0, 0, 0)
	glClearAccum(0, 0, 0, 0)
	'''Make the teapot display list.'''
	teapotList = glGenLists(1)
	glNewList(teapotList, GL_COMPILE)
	glutSolidTeapot(0.5)
	glEndList()
}

void renderTeapot(GLfloat x, GLfloat y, GLfloat z, GLfloat ambr, GLfloat ambg, GLfloat ambb, GLfloat difr, GLfloat difg,
	GLfloat difb, GLfloat specr, GLfloat specg, GLfloat specb, GLfloat shine)
{
	GLfloat mat[4]
	glPushMatrix()
	glTranslatef(x, y, z)
	mat[0] = ambr
	mat[1] = ambg
	mat[2] = ambb
	mat[3] = 1
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat)
	mat[0] = difr
	mat[1] = difg
	mat[2] = difb
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat)
	mat[0] = specr
	mat[1] = specg
	mat[2] = specb
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat)
	glMaterialf(GL_FRONT, GL_SHININESS, shine*128)
	glCallList(teapotList)
	glPopMatrix()
}

'''Draws 5 teapots into the accumulation buffer several times, each time with a jittered perspective.'''
'''The focal point is at z = 5, so the gold teapot will stay in focus.'''
'''The amount of jitter is adjusted by the magnitude of the accPerspective() jitter.'''
'''In this example the magnitude is 0.33 and the teapots are drawn 8 times.'''
void display(void)
{
	int jitter
	GLint viewport[4]
	glGetIntegerv(GL_VIEWPORT, viewport)
	glClear(GL_ACCUM_BUFFER_BIT)

	for(jitter = 0 jitter < 8 jitter++)
	{
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		accPerspective(45, (GLdouble) viewport[2]/(GLdouble) viewport[3], 1, 15, 0, 0, 0.33*j8[jitter].x, 0.33*j8[jitter].y, 5)
		'''ruby, gold, silver, emerald, and cyan teapots'''
		renderTeapot(-1.1, -0.5, -4.5, 0.1745, 01175, 01175, 0.61424, 04136, 04136, 0.727811, 0.626959, 0.626959, 0.6)
		renderTeapot(-0.5, -0.5, -5, 0.24725, 0.1995, 0745, 0.75164, 0.60648, 0.22648, 0.628281, 0.555802, 0.366065, 0.4)
		renderTeapot(0.2, -0.5, -5.5, 0.19225, 0.19225, 0.19225, 0.50754, 0.50754, 0.50754, 0.508273, 0.508273, 0.508273, 0.4)
		renderTeapot(1, -0.5, -6, 0215, 0.1745, 0215, 07568, 0.61424, 07568, 0.633, 0.727811, 0.633, 0.6)
		renderTeapot(1.8, -0.5, -6.5, 0, 0.1, 06, 0, 0.50980392, 0.50980392, 0.50196078, 0.50196078, 0.50196078, .25)
		glAccum(GL_ACCUM, 0.125)
	}

	glAccum(GL_RETURN, 1)
	glFlush()
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h)
}

void keyboard(unsigned char key, int x, int y)
{
	switch(key)
	{
		case 27:
			exit(0)
			break
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_ACCUM | GLUT_DEPTH)
	glutInitWindowSize(400, 400)
	glutInitWindowPosition(100, 100)
	glutCreateWindow(argv[0])
	init()
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutKeyboardFunc(keyboard)
	glutMainLoop()
	return 0
}
#!/usr/bin/python

from Window import *

class ClippingPlanes(Window):
	'''Demonstrates arbitrary clipping planes.'''

	def __init__(self):
		'''Initialize alpha blending function.'''
		super(ClippingPlanes, self).__init__("clip.c", "Clipping Planes", 500, 500)
		#gluPerspective(60, w/h, 1, 20)
		glShadeModel(GL_FLAT)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glPushMatrix()
		glTranslatef(0, 0, -5)
		# Clip lower half (y<0).
		glClipPlane(GL_CLIP_PLANE0, (0, 1, 0, 0))
		glEnable(GL_CLIP_PLANE0)
		# Clip left half (x<0).
		glClipPlane(GL_CLIP_PLANE1, (1, 0, 0, 0))
		glEnable(GL_CLIP_PLANE1)
		glRotatef(90, 1, 0, 0)
		glutWireSphere(1, 20, 16)
		glPopMatrix()
		glFlush()

if __name__ == '__main__':
	ClippingPlanes().run()
