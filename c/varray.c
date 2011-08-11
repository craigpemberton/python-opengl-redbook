// Demonstrates vertex arrays.

#include <GL/glut.h>
#include <stdio.h>

#define POINTER 1
#define INTERLEAVED 2
#define DRAWARRAY 1
#define ARRAYELEMENT  2
#define DRAWELEMENTS 3

int setupMethod = POINTER;
int derefMethod = DRAWARRAY;

void setupPointers(void)
{
	static GLint vertices[] = {25, 25, 100, 325, 175, 25, 175, 325, 250, 25, 325, 325};
	static GLfloat colors[] = {1.0, 0.2, 0.2, 0.2, 0.2, 1.0, 0.8, 1.0, 0.2, 0.75, 0.75, 0.75, 0.35, 0.35, 0.35, 0.5, 0.5, 0.5};
	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_COLOR_ARRAY);
	glVertexPointer(2, GL_INT, 0, vertices);
	glColorPointer(3, GL_FLOAT, 0, colors);
}

void setupInterleave(void)
{
	static GLfloat intertwined[] =
	{
		1.0, 0.2, 1.0, 100.0, 100.0, 0.0,
		1.0, 0.2, 0.2, 0.0, 200.0, 0.0,
		1.0, 1.0, 0.2, 100.0, 300.0, 0.0,
		0.2, 1.0, 0.2, 200.0, 300.0, 0.0,
		0.2, 1.0, 1.0, 300.0, 200.0, 0.0,
		0.2, 0.2, 1.0, 200.0, 100.0, 0.0
	};
	glInterleavedArrays(GL_C3F_V3F, 0, intertwined);
}

void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glShadeModel(GL_SMOOTH);
	setupPointers();
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);

	if(derefMethod == DRAWARRAY)
	{
		glDrawArrays(GL_TRIANGLES, 0, 6);
	}
	else if(derefMethod == ARRAYELEMENT)
	{
		glBegin(GL_TRIANGLES);
		glArrayElement(2);
		glArrayElement(3);
		glArrayElement(5);
		glEnd();
	}
	else if(derefMethod == DRAWELEMENTS)
	{
		GLuint indices[4] = {0, 1, 3, 4};
		glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_INT, indices);
	}

	glFlush();
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, (GLdouble) w, 0.0, (GLdouble) h);
}

void mouse(int button, int state, int x, int y)
{
	switch(button)
	{
		case GLUT_LEFT_BUTTON:
			if(state == GLUT_DOWN)
			{
				if(setupMethod == POINTER)
				{
					setupMethod = INTERLEAVED;
					setupInterleave();
				}
				else if(setupMethod == INTERLEAVED)
				{
					setupMethod = POINTER;
					setupPointers();
				}

				glutPostRedisplay();
			}

			break;

		case GLUT_MIDDLE_BUTTON:
		case GLUT_RIGHT_BUTTON:
			if(state == GLUT_DOWN)
			{
				if(derefMethod == DRAWARRAY)
				{
					derefMethod = ARRAYELEMENT;
				}
				else if(derefMethod == ARRAYELEMENT)
				{
					derefMethod = DRAWELEMENTS;
				}
				else if(derefMethod == DRAWELEMENTS)
				{
					derefMethod = DRAWARRAY;
				}

				glutPostRedisplay();
			}

			break;

		default:
			break;
	}
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
	glutInitWindowSize(350, 350);
	glutInitWindowPosition(100, 100);
	glutCreateWindow(argv[0]);
	init();
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMouseFunc(mouse);
	glutKeyboardFunc(keyboard);
	glutMainLoop();
	return 0;
}
