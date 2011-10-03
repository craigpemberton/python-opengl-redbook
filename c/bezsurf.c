// Renders a wireframe Bezier surface, using two-dimensional evaluators.

#include <stdlib.h>
#include <GL/glut.h>

GLfloat ctrlpoints[4][4][3] =
{
	{{-1.5, -1.5,  4.0},
	 {-0.5, -1.5,  2.0},
	 { 0.5, -1.5, -1.0},
	 { 1.5, -1.5,  2.0}},
	{{-1.5, -0.5,  1.0},
	 {-0.5, -0.5,  3.0},
	 { 0.5, -0.5,  0.0},
	 { 1.5, -0.5, -1.0}},
	{{-1.5,  0.5,  4.0},
	 {-0.5,  0.5,  0.0},
	 { 0.5,  0.5,  3.0},
	 { 1.5,  0.5,  4.0}},
	{{-1.5,  1.5, -2.0},
	 {-0.5,  1.5, -2.0},
	 { 0.5,  1.5,  0.0},
	 { 1.5,  1.5, -1.0}},
};

void display(void)
{
	int i, j;
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0);
	glPushMatrix();
	glRotatef(85.0, 1.0, 1.0, 1.0);

	for(j = 0; j <= 8; j++)
	{
		glBegin(GL_LINE_STRIP);

		for(i = 0; i <= 30; i++)
		{
			glEvalCoord2f((GLfloat)i/30.0, (GLfloat)j/8.0);
		}

		glEnd();
		glBegin(GL_LINE_STRIP);

		for(i = 0; i <= 30; i++)
		{
			glEvalCoord2f((GLfloat)j/8.0, (GLfloat)i/30.0);
		}

		glEnd();
	}

	glPopMatrix();
	glFlush();
}

void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glMap2f(GL_MAP2_VERTEX_3, 0, 1, 3, 4, 0, 1, 12, 4, &ctrlpoints[0][0][0]);
	glEnable(GL_MAP2_VERTEX_3);
	glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0);
	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if(w <= h)
		glOrtho(-4.0, 4.0, -4.0*(GLfloat)h/(GLfloat)w, 4.0*(GLfloat)h/(GLfloat)w, -4.0, 4.0);
	else
		glOrtho(-4.0*(GLfloat)w/(GLfloat)h, 4.0*(GLfloat)w/(GLfloat)h, -4.0, 4.0, -4.0, 4.0);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
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
	glutKeyboardFunc(keyboard);
	glutMainLoop();
	return 0;
}
