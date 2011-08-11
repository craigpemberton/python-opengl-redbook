//Draws a texture mapped teapot with automatically generated texture coordinates.
// The texture is rendered as stripes on the teapot.
// Initially, the object is drawn with texture coordinates based upon the object coordinates of the vertex and distance from the plane x = 0.
// Pressing 'e' changes the coordinate generation to eye coordinates of the vertex.
// Pressing the 'o' key switches it back to the object coordinates.
// Pressing the 's' key changes the plane to a slanted one (x + y + z = 0).
// Pressing the 'x' key switches it back to x = 0.

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>

#define	stripeImageWidth 32
GLubyte stripeImage[4*stripeImageWidth];

static GLuint texName;

void makeStripeImage(void)
{
	int j;

	for(j = 0; j < stripeImageWidth; j++)
	{
		stripeImage[4*j] = (GLubyte)((j<=4) ? 255 : 0);
		stripeImage[4*j+1] = (GLubyte)((j>4) ? 255 : 0);
		stripeImage[4*j+2] = (GLubyte) 0;
		stripeImage[4*j+3] = (GLubyte) 255;
	}
}

//  Planes for texture coordinate generation.
static GLfloat xequalzero[] = {1.0, 0.0, 0.0, 0.0};
static GLfloat slanted[] = {1.0, 1.0, 1.0, 0.0};
static GLfloat* currentCoeff;
static GLenum currentPlane;
static GLint currentGenMode;

void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_SMOOTH);
	makeStripeImage();
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	glGenTextures(1, &texName);
	glBindTexture(GL_TEXTURE_1D, texName);
	glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexImage1D(GL_TEXTURE_1D, 0, GL_RGBA, stripeImageWidth, 0, GL_RGBA, GL_UNSIGNED_BYTE, stripeImage);
	glTexImage1D(GL_TEXTURE_1D, 0, 4, stripeImageWidth, 0, GL_RGBA, GL_UNSIGNED_BYTE, stripeImage);
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
	currentCoeff = xequalzero;
	currentGenMode = GL_OBJECT_LINEAR;
	currentPlane = GL_OBJECT_PLANE;
	glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, currentGenMode);
	glTexGenfv(GL_S, currentPlane, currentCoeff);
	glEnable(GL_TEXTURE_GEN_S);
	glEnable(GL_TEXTURE_1D);
	glEnable(GL_CULL_FACE);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_AUTO_NORMAL);
	glEnable(GL_NORMALIZE);
	glFrontFace(GL_CW);
	glCullFace(GL_BACK);
	glMaterialf(GL_FRONT, GL_SHININESS, 64.0);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glPushMatrix();
	glRotatef(45.0, 0.0, 0.0, 1.0);
	glBindTexture(GL_TEXTURE_1D, texName);
	glutSolidTeapot(2.0);
	glPopMatrix();
	glFlush();
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if(w <= h)
		glOrtho(-3.5, 3.5, -3.5*(GLfloat)h/(GLfloat)w, 3.5*(GLfloat)h/(GLfloat)w, -3.5, 3.5);
	else
		glOrtho(-3.5*(GLfloat)w/(GLfloat)h, 3.5*(GLfloat)w/(GLfloat)h, -3.5, 3.5, -3.5, 3.5);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void keyboard(unsigned char key, int x, int y)
{
	switch(key)
	{
		case 'e':
		case 'E':
			currentGenMode = GL_EYE_LINEAR;
			currentPlane = GL_EYE_PLANE;
			glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, currentGenMode);
			glTexGenfv(GL_S, currentPlane, currentCoeff);
			glutPostRedisplay();
			break;

		case 'o':
		case 'O':
			currentGenMode = GL_OBJECT_LINEAR;
			currentPlane = GL_OBJECT_PLANE;
			glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, currentGenMode);
			glTexGenfv(GL_S, currentPlane, currentCoeff);
			glutPostRedisplay();
			break;

		case 's':
		case 'S':
			currentCoeff = slanted;
			glTexGenfv(GL_S, currentPlane, currentCoeff);
			glutPostRedisplay();
			break;

		case 'x':
		case 'X':
			currentCoeff = xequalzero;
			glTexGenfv(GL_S, currentPlane, currentCoeff);
			glutPostRedisplay();
			break;

		case 27:
			exit(0);
			break;

		default:
			break;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(256, 256);
	glutInitWindowPosition(100, 100);
	glutCreateWindow(argv[0]);
	init();
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);
	glutMainLoop();
	return 0;
}
