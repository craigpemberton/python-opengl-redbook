// Demonstrates some characters of a stroke font.
// The characters are represented by display lists, named with the corresponding ASCII codes.
// Use of glCallLists() is demonstrated.

#include <GL/glut.h>
#include <stdlib.h>
#include <string.h>

#define PT 1
#define STROKE 2
#define END 3

typedef struct charpoint
{
	GLfloat   x, y;
	int    type;
} CP;

CP Adata[] =
{
	{ 0, 0, PT}, {0, 9, PT}, {1, 10, PT}, {4, 10, PT},
	{5, 9, PT}, {5, 0, STROKE}, {0, 5, PT}, {5, 5, END}
};

CP Edata[] =
{
	{5, 0, PT}, {0, 0, PT}, {0, 10, PT}, {5, 10, STROKE},
	{0, 5, PT}, {4, 5, END}
};

CP Pdata[] =
{
	{0, 0, PT}, {0, 10, PT},  {4, 10, PT}, {5, 9, PT}, {5, 6, PT},
	{4, 5, PT}, {0, 5, END}
};

CP Rdata[] =
{
	{0, 0, PT}, {0, 10, PT},  {4, 10, PT}, {5, 9, PT}, {5, 6, PT},
	{4, 5, PT}, {0, 5, STROKE}, {3, 5, PT}, {5, 0, END}
};

CP Sdata[] =
{
	{0, 1, PT}, {1, 0, PT}, {4, 0, PT}, {5, 1, PT}, {5, 4, PT},
	{4, 5, PT}, {1, 5, PT}, {0, 6, PT}, {0, 9, PT}, {1, 10, PT},
	{4, 10, PT}, {5, 9, END}
};

// Interprets the instructions from the array for that letter and renders the letter with line segments.
static void drawLetter(CP *l)
{
	glBegin(GL_LINE_STRIP);

	while(1)
	{
		switch(l->type)
		{
			case PT:
				glVertex2fv(&l->x);
				break;

			case STROKE:
				glVertex2fv(&l->x);
				glEnd();
				glBegin(GL_LINE_STRIP);
				break;

			case END:
				glVertex2fv(&l->x);
				glEnd();
				glTranslatef(8.0, 0.0, 0.0);
				return;
		}

		l++;
	}
}

// Create a display list for each of 6 characters.
static void init(void)
{
	GLuint base;
	glShadeModel(GL_FLAT);
	base = glGenLists(128);
	glListBase(base);
	glNewList(base+'A', GL_COMPILE);
	drawLetter(Adata);
	glEndList();
	glNewList(base+'E', GL_COMPILE);
	drawLetter(Edata);
	glEndList();
	glNewList(base+'P', GL_COMPILE);
	drawLetter(Pdata);
	glEndList();
	glNewList(base+'R', GL_COMPILE);
	drawLetter(Rdata);
	glEndList();
	glNewList(base+'S', GL_COMPILE);
	drawLetter(Sdata);
	glEndList();
	glNewList(base+' ', GL_COMPILE);
	glTranslatef(8.0, 0.0, 0.0);
	glEndList();
}

char *test1 = "A SPARE SERAPE APPEARS AS";
char *test2 = "APES PREPARE RARE PEPPERS";

static void printStrokedString(char *s)
{
	GLsizei len = strlen(s);
	glCallLists(len, GL_BYTE, (GLbyte *)s);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0);
	glPushMatrix();
	glScalef(2.0, 2.0, 2.0);
	glTranslatef(10.0, 30.0, 0.0);
	printStrokedString(test1);
	glPopMatrix();
	glPushMatrix();
	glScalef(2.0, 2.0, 2.0);
	glTranslatef(10.0, 13.0, 0.0);
	printStrokedString(test2);
	glPopMatrix();
	glFlush();
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
		case ' ':
			glutPostRedisplay();
			break;

		case 27:
			exit(0);
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(440, 120);
	glutCreateWindow("stroke");
	init();
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}
