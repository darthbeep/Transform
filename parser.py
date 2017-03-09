from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""


def parse_file( fname, points, transform, screen, color ):
	ident(transform)
	mode = "read"
	stop = "no"
	f = open(fname, 'r')
	cont = f.readline()
	while cont != "" and cont != "nope\n":
		#print_matrix(transform)
		if cont == "nope\n":
			print "no"
		if cont == "line\n":
			nl = f.readline()
			sl = nl.split()
			add_edge(points, float(sl[0]), float(sl[1]), float(sl[2]), float(sl[3]), float(sl[4]), float(sl[5]))
		if cont == "ident\n":
			#""
			ident(transform)
		if cont == "scale\n":
			nl = f.readline()
			sl = nl.split()
			temp = make_scale(float(sl[0]), float(sl[1]), float(sl[2]))
			matrix_mult(temp, transform)
		if cont == "move\n":
			nl = f.readline()
			sl = nl.split()
			temp = make_translate(float(sl[0]), float(sl[1]), float(sl[2]))
			#print_matrix(temp)
			matrix_mult(temp, transform)
			#print_matrix(temp)
		if cont == "apply\n":
			matrix_mult(transform, points)
		if cont == "rotate\n":
			nl = f.readline()
			sl = nl.split()
			if sl[0] == "x":
				temp = make_rotX(float(sl[1]))
				matrix_mult(temp, transform)
			if sl[0] == "y":
				temp = make_rotY(float(sl[1]))
				matrix_mult(temp, transform)
			if sl[0] == "z":
				temp = make_rotZ(float(sl[1]))
				matrix_mult(temp, transform)
		if cont == "display\n":
			clear_screen(screen)
			draw_lines(points, screen, color)
			display(screen)
		if cont == "save\n":
			nl = f.readline()
			sl = nl.split()
			save_extension(screen, sl[0])
		cont = f.readline()
	#matrix_mult(transform, points)
	#print_matrix(transform)
#parse_file("script", 0, 0, 0, 0)
