// Draws anti-aliased lines in color index mode.
// It draws two diagonal lines to form an X.
// When 'r' is typed, the lines are rotated in opposite directions.

#include <GL/glut.h>
#include "stdlib.h"

#define RAMPSIZE 16
#define RAMP1START 32
#define RAMP2START 48

static float rotAngle = 0.;

// Initialize antialiasing for color index mode, including loading a green color ramp starting  at RAMP1START,
// and a blue color ramp starting at RAMP2START. The ramps must be a multiple of 16.
void init(void)
{
	int i;
	for(i = 0; i < RAMPSIZE; i++)
	{
		GLfloat shade;
		shade = (GLfloat) i/(GLfloat) RAMPSIZE;
		glutSetColor(RAMP1START+(GLint)i, 0., shade, 0.);
		glutSetColor(RAMP2START+(GLint)i, 0., 0., shade);
	}
	glEnable(GL_LINE_SMOOTH);
	glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE);
	glLineWidth(1.5);
	glClearIndex((GLfloat) RAMP1START);
}

// Draw 2 diagonal lines to form an X
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glIndexi(RAMP1START);
	glPushMatrix();
	glRotatef(-rotAngle, 0.0, 0.0, 0.1);
	glBegin(GL_LINES);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();
	glPopMatrix();
	glIndexi(RAMP2START);
	glPushMatrix();
	glRotatef(rotAngle, 0.0, 0.0, 0.1);
	glBegin(GL_LINES);
	glVertex2f(0.5, 0.5);
	glVertex2f(-0.5, -0.5);
	glEnd();
	glPopMatrix();
	glFlush();
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	if(w <= h)
		gluOrtho2D(-1.0, 1.0, -1.0*(GLfloat)h/(GLfloat)w, 1.0*(GLfloat)h/(GLfloat)w);
	else
		gluOrtho2D(-1.0*(GLfloat)w/(GLfloat)h, 1.0*(GLfloat)w/(GLfloat)h, -1.0, 1.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void keyboard(unsigned char key, int x, int y)
{
	switch(key)
	{
		case 'r':
		case 'R':
			rotAngle += 20.;

			if(rotAngle >= 360.)
			{
				rotAngle = 0.;
			}

			glutPostRedisplay();
			break;

		case 27:  // escape key
			exit(0);
			break;

		default:
			break;
	}
}

// Open window with initial window size, title bar, color index display mode, and handle input events.
int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	//Be aware, my setup does not support color indexing. This code may regress since I cannot test it.
	//glutInitDisplayMode (GLUT_SINGLE | GLUT_INDEX);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGBA);
	glutInitWindowSize(200, 200);
	glutCreateWindow(argv[0]);
	init();
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}
