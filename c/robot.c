// Shows how to composite modeling transformations to draw translated and rotated hierarchical models.
// Pressing the s and e keys (shoulder and elbow) alters the rotation of the robot arm.

#include <GL/glut.h>
#include <stdlib.h>

static int shoulder = 0, elbow = 0;

void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glShadeModel(GL_FLAT);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glPushMatrix();
	glTranslatef(-1.0, 0.0, 0.0);
	glRotatef((GLfloat) shoulder, 0.0, 0.0, 1.0);
	glTranslatef(1.0, 0.0, 0.0);
	glPushMatrix();
	glScalef(2.0, 0.4, 1.0);
	glutWireCube(1.0);
	glPopMatrix();
	glTranslatef(1.0, 0.0, 0.0);
	glRotatef((GLfloat) elbow, 0.0, 0.0, 1.0);
	glTranslatef(1.0, 0.0, 0.0);
	glPushMatrix();
	glScalef(2.0, 0.4, 1.0);
	glutWireCube(1.0);
	glPopMatrix();
	glPopMatrix();
	glutSwapBuffers();
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(65.0, (GLfloat) w/(GLfloat) h, 1.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(0.0, 0.0, -5.0);
}

void keyboard(unsigned char key, int x, int y)
{
	switch(key)
	{
		case 's':
			shoulder = (shoulder + 5) % 360;
			glutPostRedisplay();
			break;

		case 'S':
			shoulder = (shoulder - 5) % 360;
			glutPostRedisplay();
			break;

		case 'e':
			elbow = (elbow + 5) % 360;
			glutPostRedisplay();
			break;

		case 'E':
			elbow = (elbow - 5) % 360;
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
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow(argv[0]);
	init();
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);
	glutMainLoop();
	return 0;
}
