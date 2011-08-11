// Demonstrates when to issue lighting and transformation commands to render a model with a light which is moved by a modeling transformation.
// The light position is reset after the modeling transformation is called.
// The eye position does not change.
// A sphere is drawn using a grey material characteristic.
// A single light source illuminates the object.
// Pressing the left mouse button alters the modeling transformation (x rotation) by 30 degrees.

#include <GL/glut.h>
#include <stdlib.h>

static int spin = 0;

// Initialize material property, light source, lighting model, and depth buffer.
void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glShadeModel(GL_SMOOTH);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_DEPTH_TEST);
}

// Light position is reset after the modeling transformation . 
// This places the light at a new position in world coordinates.
// The cube represents the position of the light.
void display(void)
{
	GLfloat position[] = { 0.0, 0.0, 1.5, 1.0 };
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glPushMatrix();
	gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
	glPushMatrix();
	glRotated((GLdouble) spin, 1.0, 0.0, 0.0);
	glLightfv(GL_LIGHT0, GL_POSITION, position);
	glTranslated(0.0, 0.0, 1.5);
	glDisable(GL_LIGHTING);
	glColor3f(0.0, 1.0, 1.0);
	glutWireCube(0.1);
	glEnable(GL_LIGHTING);
	glPopMatrix();
	glutSolidTorus(0.275, 0.85, 8, 15);
	glPopMatrix();
	glFlush();
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(40.0, (GLfloat) w/(GLfloat) h, 1.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void mouse(int button, int state, int x, int y)
{
	switch(button)
	{
		case GLUT_LEFT_BUTTON:
			if(state == GLUT_DOWN)
			{
				spin = (spin + 30) % 360;
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
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
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
