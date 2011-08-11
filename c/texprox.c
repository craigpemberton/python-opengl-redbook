// Illustrates the use of texture proxies.
// This program only prints out some messages about whether certain size textures are supported and then exits.

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>

void init(void)
{
	GLint proxyComponents;
	glTexImage2D(GL_PROXY_TEXTURE_2D, 0, GL_RGBA8, 64, 64, 0, GL_RGBA, GL_UNSIGNED_BYTE, NULL);
	glGetTexLevelParameteriv(GL_PROXY_TEXTURE_2D, 0, GL_TEXTURE_COMPONENTS, &proxyComponents);
	printf("proxyComponents are %d\n", proxyComponents);

	if(proxyComponents == GL_RGBA8)
	{
		printf("proxy allocation succeeded\n");
	}
	else
	{
		printf("proxy allocation failed\n");
	}

	glTexImage2D(GL_PROXY_TEXTURE_2D, 0, GL_RGBA16, 2048, 2048, 0, GL_RGBA, GL_UNSIGNED_SHORT, NULL);
	glGetTexLevelParameteriv(GL_PROXY_TEXTURE_2D, 0, GL_TEXTURE_COMPONENTS, &proxyComponents);
	printf("proxyComponents are %d\n", proxyComponents);

	if(proxyComponents == GL_RGBA16)
	{
		printf("proxy allocation succeeded\n");
	}
	else
	{
		printf("proxy allocation failed\n");
	}
}

void display(void)
{
	exit(0);
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow(argv[0]);
	init();
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMainLoop();
	return 0;
}
