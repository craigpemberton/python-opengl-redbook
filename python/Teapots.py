'''Demonstrates lots of material properties. A single light source illuminates the objects.'''

def __init__(self):
	'''Initialize depth buffer, projection matrix, light source, and lighting model. Do not specify a material property here.'''
	glutInitWindowSize(500, 600)
	glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
	glLightfv(GL_LIGHT0, GL_POSITION, (0, 3, 3, 0))
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1))
	glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, (0))
	glFrontFace(GL_CW)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_AUTO_NORMAL)
	glEnable(GL_NORMALIZE)
	glEnable(GL_DEPTH_TEST)
	# Be efficient by making a teapot display list.
	self.teapotList = glGenLists(1)
	glNewList(self.teapotList, GL_COMPILE)
	glutSolidTeapot(1)
	glEndList()

def display(self):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	renderTeapot( 2, 17, 0.0215, 0.1745, 0.0215, 0.0757, 0.6142, 0.0757, 0.6330, 0.7278, 0.6330, 0.6000) # emerald
	renderTeapot( 2, 14, 0.1350, 0.2225, 0.1575, 0.5400, 0.8900, 0.6300, 0.3162, 0.3162, 0.3162, 0.1000) # jade
	renderTeapot( 2, 11, 0.0538, 0.0500, 0.0663, 0.1828, 0.1700, 0.2253, 0.3327, 0.3286, 0.3464, 0.3000) # obsidian
	renderTeapot( 2,  8, 0.2500, 0.2073, 0.2073, 1.0000, 0.8290, 0.8290, 0.2966, 0.2966, 0.2966, 0.0880) # pearl
	renderTeapot( 2,  5, 0.1745, 011750, 0.0118, 0.6142, 0.0414, 0.0414, 0.7278, 0.6270, 0.6270, 0.6000) # ruby
	renderTeapot( 2,  2, 0.1000, 0.1873, 0.1745, 0.3960, 0.7415, 0.6910, 0.2973, 0.3083, 0.3067, 0.1000) # turquoise
	renderTeapot( 6, 17, 0.3294, 0.2235, 0.0275, 0.7804, 0.5686, 0.1137, 0.9926, 0.9412, 0.8078, 0.2179) # brass
	renderTeapot( 6, 14, 0.2125, 0.1275, 0.0540, 0.7140, 0.4284, 0.1814, 0.3935, 0.2719, 0.1667, 0.2000) # bronze
	renderTeapot( 6, 11, 0.2500, 0.2500, 0.2500, 0.4000, 0.4000, 0.4000, 0.7746, 0.7746, 0.7746, 0.6000) # chrome
	renderTeapot( 6,  8, 0.1913, 0.0735, 0.0225, 0.7038, 0.2705, 0.0828, 0.2568, 0.1376, 0.0860, 0.1000) # copper 
	renderTeapot( 6,  5, 0.2473, 0.1995, 0.7450, 0.7516, 0.6065, 0.2265, 0.6283, 0.5558, 0.3661, 0.4000) # gold 
	renderTeapot( 6,  2, 0.1923, 0.1923, 0.1923, 0.5075, 0.5075, 0.5075, 0.5084, 0.5083, 0.5083, 0.4000) # silver 
	renderTeapot(10, 17, 0.0000, 0.0000, 0.0000, 0.0100, 0.0100, 0.0100, 0.5000, 0.5000, 0.5000, 0.2500) # plastic black 
	renderTeapot(10, 14, 0.0000, 0.1000, 0.6000, 0.0000, 0.5098, 0.5098, 0.5020, 0.5020, 0.5020, 0.2500) # plastic cyan
	renderTeapot(10, 11, 0.0000, 0.0000, 0.0000, 0.1000, 0.3500, 0.1000, 0.4500, 0.5500, 0.4500, 0.2500) # plastic green
	renderTeapot(10,  8, 0.0000, 0.0000, 0.0000, 0.5000, 0.0000, 0.0000, 0.7000, 0.6000, 0.6000, 0.2500) # plastic red
	renderTeapot(10,  5, 0.0000, 0.0000, 0.0000, 0.5500, 0.5500, 0.5500, 0.7000, 0.7000, 0.7000, 0.2500) # plastic white
	renderTeapot(10,  2, 0.0000, 0.0000, 0.0000, 0.5000, 0.5000, 0.0000, 0.6000, 0.6000, 0.5000, 0.2500) # plastic yellow
	renderTeapot(14, 17, 0.0200, 0.0200, 0.2000, 0.1000, 0.0100, 0.0100, 0.4000, 0.4000, 0.4000, 0.7813) # rubber black
	renderTeapot(14, 14, 0.0000, 0.0500, 0.5000, 0.4000, 0.5000, 0.5000, 0.0400, 0.7000, 0.7000, 0.7813) # rubber cyan
	renderTeapot(14, 11, 0.0000, 0.0500, 0.0000, 0.4000, 0.5000, 0.4000, 0.0400, 0.7000, 0.0400, 0.7813) # rubber green
	renderTeapot(14,  8, 0.0500, 0.0000, 0.0000, 0.5000, 0.4000, 0.4000, 0.7000, 0.0400, 0.0400, 0.7813) # rubber red
	renderTeapot(14,  5, 0.0500, 0.0500, 0.0500, 0.5000, 0.5000, 0.5000, 0.7000, 0.7000, 0.7000, 0.7813) # rubber white
	renderTeapot(14,  2, 0.0500, 0.0500, 0.0000, 0.5000, 0.5000, 0.4000, 0.7000, 0.7000, 0.0400, 0.7813) # rubber yellow
	glFlush()

def renderTeapot(x, y, ambr, ambg, ambb, difr, difg, difb, specr, specg, specb, shine):
	'''Moves into position and draws a teapot.'''
	glPushMatrix()
	glTranslatef(x, y, 0)
	glMaterialfv(GL_FRONT, GL_AMBIENT, (ambr, ambg, ambb, 1))
	glMaterialfv(GL_FRONT, GL_DIFFUSE, (difr, difg, difb, 1))
	glMaterialfv(GL_FRONT, GL_SPECULAR, (specr, specg, specb, 1))
	glMaterialf(GL_FRONT, GL_SHININESS, shine * 128)
	glCallList(teapotList)
	glPopMatrix()
