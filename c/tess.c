// Demonstrates polygon tessellation.
// Two tesselated objects are drawn; a rectangle with a triangular hole and a smooth shaded, self-intersecting star.
// The exterior rectangle is drawn with its vertices in counter-clockwise order, but its interior clockwise.
// combineCallback is needed for the self-intersecting star.
// Removing the TessProperty for the star will make the interior unshaded (WINDING_ODD).

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>

#ifndef CALLBACK
#define CALLBACK
#endif

GLuint startList;

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0);
	glCallList(startList);
	glCallList(startList + 1);
	glFlush();
}

void CALLBACK beginCallback(GLenum which)
{
	glBegin(which);
}

void CALLBACK errorCallback(GLenum errorCode)
{
	const GLubyte *estring;
	estring = gluErrorString(errorCode);
	fprintf(stderr, "Tessellation Error: %s\n", estring);
	exit(0);
}

void CALLBACK endCallback(void)
{
	glEnd();
}

void CALLBACK vertexCallback(GLvoid *vertex)
{
	const GLdouble *pointer;
	pointer = (GLdouble *) vertex;
	glColor3dv(pointer+3);
	glVertex3dv(vertex);
}

// Creates a new vertex when edges intersect.
// Coordinate location is trivial to calculate,
// but weight[4] may be used to average color, normal, or texture  coordinate data.
// In this program, color is weighted.
void CALLBACK combineCallback(GLdouble coords[3], GLdouble *vertex_data[4], GLfloat weight[4], GLdouble **dataOut)
{
	GLdouble *vertex;
	int i;
	vertex = (GLdouble *) malloc(6 * sizeof(GLdouble));
	vertex[0] = coords[0];
	vertex[1] = coords[1];
	vertex[2] = coords[2];

	for(i = 3; i < 7; i++)
		vertex[i] =	  weight[0] * vertex_data[0][i]
				+ weight[1] * vertex_data[1][i]
				+ weight[2] * vertex_data[2][i]
				+ weight[3] * vertex_data[3][i];
	*dataOut = vertex;
}

void init(void)
{
	GLUtesselator *tobj;
	GLdouble rect[4][3] = {	{ 50.0,  50.0, 0.0},
				{200.0,  50.0, 0.0},
				{200.0, 200.0, 0.0},
				{ 50.0, 200.0, 0.0} };
	GLdouble tri[3][3] = {	{ 75.0,  75.0, 0.0},
				{125.0, 175.0, 0.0},
				{175.0,  75.0, 0.0} };
	GLdouble star[5][6] = {	{250.0,  50.0, 0.0, 1.0, 0.0, 1.0},
				{325.0, 200.0, 0.0, 1.0, 1.0, 0.0},
				{400.0,  50.0, 0.0, 0.0, 1.0, 1.0},
				{250.0, 150.0, 0.0, 1.0, 0.0, 0.0},
				{400.0, 150.0, 0.0, 0.0, 1.0, 0.0} };
	glClearColor(0.0, 0.0, 0.0, 0.0);
	startList = glGenLists(2);
	tobj = gluNewTess();
	gluTessCallback(tobj, GLU_TESS_VERTEX, glVertex3dv);
	gluTessCallback(tobj, GLU_TESS_BEGIN, beginCallback);
	gluTessCallback(tobj, GLU_TESS_END, endCallback);
	gluTessCallback(tobj, GLU_TESS_ERROR, errorCallback);
	// Rectangle with a triangular hole inside.
	glNewList(startList, GL_COMPILE);
	glShadeModel(GL_FLAT);
	gluTessBeginPolygon(tobj, NULL);
	gluTessBeginContour(tobj);
	gluTessVertex(tobj, rect[0], rect[0]);
	gluTessVertex(tobj, rect[1], rect[1]);
	gluTessVertex(tobj, rect[2], rect[2]);
	gluTessVertex(tobj, rect[3], rect[3]);
	gluTessEndContour(tobj);
	gluTessBeginContour(tobj);
	gluTessVertex(tobj, tri[0], tri[0]);
	gluTessVertex(tobj, tri[1], tri[1]);
	gluTessVertex(tobj, tri[2], tri[2]);
	gluTessEndContour(tobj);
	gluTessEndPolygon(tobj);
	glEndList();
	gluTessCallback(tobj, GLU_TESS_VERTEX, vertexCallback);
	gluTessCallback(tobj, GLU_TESS_BEGIN, beginCallback);
	gluTessCallback(tobj, GLU_TESS_END, endCallback);
	gluTessCallback(tobj, GLU_TESS_ERROR, errorCallback);
	gluTessCallback(tobj, GLU_TESS_COMBINE, combineCallback);
	// Smooth shaded, self-intersecting star.
	glNewList(startList + 1, GL_COMPILE);
	glShadeModel(GL_SMOOTH);
	gluTessProperty(tobj, GLU_TESS_WINDING_RULE, GLU_TESS_WINDING_POSITIVE);
	gluTessBeginPolygon(tobj, NULL);
	gluTessBeginContour(tobj);
	gluTessVertex(tobj, star[0], star[0]);
	gluTessVertex(tobj, star[1], star[1]);
	gluTessVertex(tobj, star[2], star[2]);
	gluTessVertex(tobj, star[3], star[3]);
	gluTessVertex(tobj, star[4], star[4]);
	gluTessEndContour(tobj);
	gluTessEndPolygon(tobj);
	glEndList();
	gluDeleteTess(tobj);
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, (GLdouble) w, 0.0, (GLdouble) h);
}

void keyboard(unsigned char key, int x, int y)
{
	switch(key)
	{
		case 27:
			exit(0);
			break;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutCreateWindow(argv[0]);
	init();
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);
	glutMainLoop();
	return 0;
}
