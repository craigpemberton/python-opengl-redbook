'''Illustrates the use of texture proxies.'''
'''This program only prints out some messages about whether certain size textures are supported and then exits.'''

def __init__(self):
	glTexImage2D(GL_PROXY_TEXTURE_2D, 0, GL_RGBA8, 64, 64, 0, GL_RGBA, GL_UNSIGNED_BYTE, None)
	proxyComponents = glGetTexLevelParameteriv(GL_PROXY_TEXTURE_2D, 0, GL_TEXTURE_COMPONENTS)
	print 'proxyComponents are', proxyComponents
	if(proxyComponents == GL_RGBA8):
		print 'proxy allocation succeeded'
	else
		print 'proxy allocation failed'
	glTexImage2D(GL_PROXY_TEXTURE_2D, 0, GL_RGBA16, 2048, 2048, 0, GL_RGBA, GL_UNSIGNED_SHORT, None)
	proxyComponents = glGetTexLevelParameteriv(GL_PROXY_TEXTURE_2D, 0, GL_TEXTURE_COMPONENTS)
	print 'proxyComponents are %d\n', proxyComponents)
	if(proxyComponents == GL_RGBA16)
		print 'proxy allocation succeeded'
	else
		print 'proxy allocation failed'

def display(self):
	exit(0)
