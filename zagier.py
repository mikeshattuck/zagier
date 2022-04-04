#!/usr/bin/python
import math
import sys

def involutionI(x,y,z):
	if x < (y-z):
		return ([
			x + (2*z),
			z,
			y-x-z,
			False,
			False
		])
	elif (y-z) < x < (2*y):
		return ([
			(2*y) - x,
			y,
			x-y+z,
			False,
			False
		])
	elif x > (2*y):
		return ([
			x - (2*y),
			x-y+z,
			y,
			False,
			False
		])
	else:
		#Error?
		return

def involutionG(x,y,z):
	return([
		x,
		z,
		y,
		False,
		False])

def isFixed(a,b):
	return a[0] == b[0] and a[1] == b[1] and a[2] == b[2]

def printHeader(num):
	print"Solutions to " + str(num) + " = x^2 + 4yz"
	print"(x,y,z)\t\t\tFixed by I\tFixed by G\tSum of Squares Solution"

def printWindmill(a):
	isFixedInI = a[3]
	isFixedInG = a[4]
	solution = ""
	
	if isFixedInG == True:
		solution = str(a[0]) + "^2 + " + str(a[1]*2) + "^2"
	
	print("(%d,%d,%d)" % (a[0],a[1],a[2]) + "\t\t" + str(isFixedInI) + "\t\t" + str(isFixedInG) + "\t\t" + solution)

def exists(list,w):
	for i in list:
		if i[0] == w[0] and i[1] == w[1] and i[2] == w[2]:
			return True
	return False

def findWindmills(num):
	windmills = []
	x = 1
	x_max = math.floor((num-4) ** 0.5)		#We only need to test up to (prime-4)^1/2 

	while (x <= x_max):
		yz = (num - x**2)/4					#Solve for yz in p = x^2 + 4yz
		y = 1
		y_max = math.floor(yz ** 1/2)
		while (y <= y_max):
			z = yz/y							#Solve for z since x,y are known
			if num == x**2 + 4*y*z:
				w = [x,y,z, False, False]		#We have our windmill w
				wI = involutionI(x,y,z)		#Involute our windmill to a new windmill wI
				
				if isFixed(w,wI):			#Testing if our first windmill is fixed by the first involution
					w[3] = True
					wI = None
				else:
					w[3] = False				#It is not so the second involution is not fixed either
					wI[3] = False
				

				if isFixed(w, involutionG(w[0],w[1],w[2])):
					w[4] = True
				else:
					w[4] = False

				if wI != None:
					if isFixed(wI, involutionG(wI[0],wI[1],wI[2])):
						wI[4] = True
					else:
						wI[4] = False

				#Add our windmill if it is not already in S
				if exists(windmills,w) == False:
					windmills.append(w)

				#Add our involuted windmill if it is not already in S
				if wI != None:
					if exists(windmills,wI) == False:
						windmills.append(wI)

			y += 1
		x += 1
	return windmills


inputs = map(int,sys.argv[1:])
input_number = inputs[0]
if input_number % 4 != 1 or input_number < 3:
	print "Please enter a valid 4k+1 number greater than 2"
else:
	S = findWindmills(input_number)
	length = len(S)
	print "S contains " + str(len(S)) + " windmills"
	printHeader(input_number)
	for w in S:
		printWindmill(w)

