'''Demonstrates some characters of a stroke font.'''
'''The characters are represented by display lists, named with the corresponding ASCII codes.'''
'''Use of glCallLists() is demonstrated.'''

class LetterItem(Object):
	'''Omg seriously polymorphism hello.'''
	def __init__(x, y):
		self.x = x
		self.y = y
	def render(self):
		raise NotImplementedError

class Point(LetterItem):
	def __init__(x, y):
		super(LetterItem, self).__init__(x, y)

	def render(self):
		glVertex2f(self.x, self.y)

class Stroke(LetterItem):
	def __init__(x, y):
		super(LetterItem, self).__init__(x, y)

	def render(self):
		glVertex2f(self.x, self.y)
		glEnd()
		glBegin(GL_LINE_STRIP)

class End(LetterItem):
	def __init__(x, y):
		super(LetterItem, self).__init__(x, y)

	def render(self):
		glVertex2f(self.x, self.y)
		glEnd()
		glTranslatef(8, 0, 0)

letterA = (Point(0, 0), Point(0, 9), Point(1, 10), Point(4, 10), Point(5, 9), Stroke(5, 0), Point(0, 5), End(5, 5))
letterE = (Point(5, 0), Point(0, 0), Point(0, 10), Stroke(5, 10), Point(0, 5), End(4, 5))
letterP = (Point(0, 0), Point(0, 10), Point(4, 10), Point(5, 9), Point(5, 6), Point(4, 5), End(0, 5))
letterR = (Point(0, 0), Point(0, 10), Point(4, 10), Point(5, 9), Point(5, 6), Point(4, 5), Stroke(0, 5), Point(3, 5), End(5, 0))
letterS = (Point(0, 1), Point(1, 0), Point(4, 0), Point(5, 1), Point(5, 4), Point(4, 5), Point(1, 5), Point(0, 6), Point(0, 9), Point(1, 10), Point(4, 10), End(5, 9))

def __init__(self):
	'''Create a display list for each of 6 characters.'''
	glutInitWindowSize(440, 120)
	glShadeModel(GL_FLAT)
	base = glGenLists(128)
	glListBase(base)
	glNewList(base+'A', GL_COMPILE)
	drawLetter(Adata)
	glEndList()
	glNewList(base+'E', GL_COMPILE)
	drawLetter(Edata)
	glEndList()
	glNewList(base+'P', GL_COMPILE)
	drawLetter(Pdata)
	glEndList()
	glNewList(base+'R', GL_COMPILE)
	drawLetter(Rdata)
	glEndList()
	glNewList(base+'S', GL_COMPILE)
	drawLetter(Sdata)
	glEndList()
	glNewList(base+' ', GL_COMPILE)
	glTranslatef(8, 0, 0)
	glEndList()

def display(self):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 1, 1)
	glPushMatrix()
	glScalef(2, 2, 2)
	glTranslatef(10, 30, 0)
	printStrokedString('A SPARE SERAPE APPEARS AS')
	glPopMatrix()
	glPushMatrix()
	glScalef(2, 2, 2)
	glTranslatef(10, 13, 0)
	printStrokedString('APES PREPARE RARE PEPPERS')
	glPopMatrix()
	glFlush()

def drawLetter(letter):
	'''Interprets the instructions from the array for that letter and renders the letter with line segments.'''
	glBegin(GL_LINE_STRIP)
	for letterItem in letter:
		letterItem.render()
	
def printStrokedString(s)
	glCallLists(len(s), GL_BYTE, s)
