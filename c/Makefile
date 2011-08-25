#reworking this stupid thing
#cmake on the way

INCLUDE = -I/lusr/X11/include -I/lusr/include
LIB = -L/lusr/X11/lib -L/lusr/lib -lglut -lGLU -lGL -lpthread -lm
CC = gcc -Wall -Werror ${CFLAGS} $(INCLUDE) ${LIB}
TARGETS = aaindex aapoly aargb accanti accpersp alpha3D alpha bezcurve bezmesh bezsurf checker clip colormat cube dof double drawf feedback fog fogindex font hello image light lines list material mipmap model movelight pickdepth picksquare planet polyoff polys quadric robot scene select smooth stencil stroke surface teapots tess tesswind texbind texgen texprox texsub texturesurf torus trim unproject varray wrap

all: $(TARGETS)

clean:
	rm -f *.o $(TARGETS)

aaindex: aaindex.c
	$(CC) -o $@  $^

aapoly: aapoly.c
	$(CC) -o $@  $^

aargb: aargb.c
	$(CC) -o $@  $^

accanti: accanti.c
	$(CC) -o $@  $^

accpersp: accpersp.c
	$(CC) -o $@  $^

alpha3D: alpha3D.c
	$(CC) -o $@  $^

alpha: alpha.c
	$(CC) -o $@  $^

bezcurve: bezcurve.c
	$(CC) -o $@  $^

bezmesh: bezmesh.c
	$(CC) -o $@  $^

bezsurf: bezsurf.c
	$(CC) -o $@  $^

checker: checker.c
	$(CC) -o $@  $^

clip: clip.c
	$(CC) -o $@  $^

colormat: colormat.c
	$(CC) -o $@  $^

cube: cube.c
	$(CC) -o $@  $^

dof: dof.c
	$(CC) -o $@  $^

double: double.c
	$(CC) -o $@  $^

drawf: drawf.c
	$(CC) -o $@  $^

feedback: feedback.c
	$(CC) -o $@  $^

fog: fog.c
	$(CC) -o $@  $^

fogindex: fogindex.c
	$(CC) -o $@  $^

font: font.c
	$(CC) -o $@  $^

hello: hello.c
	$(CC) -o $@  $^

image: image.c
	$(CC) -o $@  $^

light: light.c
	$(CC) -o $@  $^

lines: lines.c
	$(CC) -o $@  $^

list: list.c
	$(CC) -o $@  $^

material: material.c
	$(CC) -o $@  $^

mipmap: mipmap.c
	$(CC) -o $@  $^

model: model.c
	$(CC) -o $@  $^

movelight: movelight.c
	$(CC) -o $@  $^

pickdepth: pickdepth.c
	$(CC) -o $@  $^

picksquare: picksquare.c
	$(CC) -o $@  $^

planet: planet.c
	$(CC) -o $@  $^

polyoff: polyoff.c
	$(CC) -o $@  $^

polys: polys.c
	$(CC) -o $@  $^

quadric: quadric.c
	$(CC) -o $@  $^

robot: robot.c
	$(CC) -o $@  $^

scene: scene.c
	$(CC) -o $@  $^

select: select.c
	$(CC) -o $@  $^

smooth: smooth.c
	$(CC) -o $@  $^

stencil: stencil.c
	$(CC) -o $@  $^

stroke: stroke.c
	$(CC) -o $@  $^

surface: surface.c
	$(CC) -o $@  $^

teapots: teapots.c
	$(CC) -o $@  $^

tess: tess.c
	$(CC) -o $@  $^

tesswind: tesswind.c
	$(CC) -o $@  $^

texbind: texbind.c
	$(CC) -o $@  $^

texgen: texgen.c
	$(CC) -o $@  $^

texprox: texprox.c
	$(CC) -o $@  $^

texsub: texsub.c
	$(CC) -o $@  $^

texturesurf: texturesurf.c
	$(CC) -o $@  $^

torus: torus.c
	$(CC) -o $@  $^

trim: trim.c
	$(CC) -o $@  $^

unproject: unproject.c
	$(CC) -o $@  $^

varray: varray.c
	$(CC) -o $@  $^

wrap: wrap.c
	$(CC) -o $@  $^

