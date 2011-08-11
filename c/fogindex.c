// Draws 5 wireframe spheres, each at a different z distance from the eye, in linear fog.

#include <GL/glut.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

// Initialize color map and fog.  Set screen clear color to end of color ramp.
#define NUMCOLORS 32
#define RAMPSTART 16

static void init(void)
{
	int i;
	glEnable(GL_DEPTH_TEST);

	for(i = 0; i < NUMCOLORS; i++)
	{
		GLfloat shade;
		shade = (GLfloat)(NUMCOLORS-i)/(GLfloat) NUMCOLORS;
		glutSetColor(RAMPSTART + i, shade, shade, shade);
	}

	glEnable(GL_FOG);
	glFogi(GL_FOG_MODE, GL_LINEAR);
	glFogi(GL_FOG_INDEX, NUMCOLORS);
	glFogf(GL_FOG_START, 1.0);
	glFogf(GL_FOG_END, 6.0);
	glHint(GL_FOG_HINT, GL_NICEST);
	glClearIndex((GLfloat)(NUMCOLORS+RAMPSTART-1));
}

static void renderSphere(GLfloat x, GLfloat y, GLfloat z)
{
	glPushMatrix();
	glTranslatef(x, y, z);
	glutWireSphere(0.4, 16, 16);
	glPopMatrix();
}

// Draws 5 spheres at different z positions.
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glIndexi(RAMPSTART);
	renderSphere(-2., -0.5, -1.0);
	renderSphere(-1., -0.5, -2.0);
	renderSphere(0., -0.5, -3.0);
	renderSphere(1., -0.5, -4.0);
	renderSphere(2., -0.5, -5.0);
	glFlush();
}

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if(w <= h)
		glOrtho(-2.5, 2.5, -2.5*(GLfloat)h/(GLfloat)w, 2.5*(GLfloat)h/(GLfloat)w, -10.0, 10.0);
	else
		glOrtho(-2.5*(GLfloat)w/(GLfloat)h, 2.5*(GLfloat)w/(GLfloat)h, -2.5, 2.5, -10.0, 10.0);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void keyboard(unsigned char key, int x, int y)
{
	switch(key)
	{
		case 27:
			exit(0);
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
	glutCreateWindow(argv[0]);
	init();
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}
