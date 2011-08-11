// This is a simple, introductory OpenGL program.

#include <GL/glut.h>

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT); // Clear all pixels.
	// draw white polygon (rectangle) with corners at (0.25, 0.25, 0.0) and (0.75, 0.75, 0.0)
	glColor3f(1.0, 1.0, 1.0);
	glBegin(GL_POLYGON);
	glVertex3f(0.25, 0.25, 0.0);
	glVertex3f(0.75, 0.25, 0.0);
	glVertex3f(0.75, 0.75, 0.0);
	glVertex3f(0.25, 0.75, 0.0);
	glEnd();
	// Don't wait! Start processing buffered OpenGL routines.
	glFlush();
}

void init(void)
{
	// Select the clearing color.
	glClearColor(0.0, 0.0, 0.0, 0.0);
	// Initialize the viewing values.
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0);
}

// Declare the initial window size, position, and display mode (single buffer and RGBA).
// Open the window with "hello" in its title bar. 
// Call the initialization routines.
// Register the callback function to display graphics.
// Enter the main loop and process events.
int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(250, 250);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("hello");
	init();
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}
