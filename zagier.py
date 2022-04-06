#!/usr/bin/python
import math
import sys

#This is the first involution in Zagier's one sentence proof
#Note the two "False" values are only to initialize these flags that we may
#set later. This should be cleaner
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

#This is the second involution in Zagier's one sentence proof
#Note the two "False" values are only to initialize these flags that we may
#set later. This should be cleaner
def involutionG(x,y,z):
	return([
		x,
		z,
		y,
		False,
		False])

def isFixed(a,b):
	return a[0] == b[0] and a[1] == b[1] and a[2] == b[2]

def printHeader(num, count):
	print("Solution Set S for " + str(num) + " = x^2 + 4yz" + " contains " + str(count) + " windmills")
	print(f"{'(x,y,z)' : <20}{'Fixed by I' : <20}{'Fixed by G' : <20}{'Solution': <20}")

def printWindmill(a):
	isFixedInI = "Yes" if a[3] == True else "No"
	isFixedInG = "Yes" if a[4] == True else "No"
	x = str(a[0])
	y = str(a[1])
	z = str(a[2])
	point = "(" + x + "," + y + "," + z + ")"

	solution = ""
	
	if isFixedInG == "Yes":
		solution = str(a[0]) + "^2 + " + str(a[1]*2) + "^2"
	
	#print("(%d,%d,%d)" % (a[0],a[1],a[2]) + "\t\t" + str(isFixedInI) + "\t\t" + str(isFixedInG) + "\t\t" + solution)
	print(f"{point : <20}{isFixedInI : <20}{isFixedInG : <20}{solution: <20}")

def exists(list,w):
	for i in list:
		if i[0] == w[0] and i[1] == w[1] and i[2] == w[2]:
			return True
	return False

def findWindmills(num):
	windmills = []
	x = 1
	#Since the general solution is p = x^2 + 4yz, then the largest allowable value for x is square root of (p - 4(1)(1) )
	x_max = math.floor(math.sqrt(num-4))

	while (x <= x_max):
		#With our x value known, we can solve for the quantity yz as: yz = (p-x^2)/4. Using yz, we can iterate over
		#y to find y,z pairs to test in our general solution
		yz = int((num - x**2))

		#Make sure y * z is an integer with our x value (sometimes it isn't since we are iterating on all x values between 1 and x max)
		if yz % 4 == 0:			

			yz = yz /4
			
			y = 1

			#Setting our y max value to half of the yz quantity seems to hit all of our windmills and matches our brute force
			#solutions. Using the square root of yz was missing a few windmills. This will require further thought.
			y_max = yz / 2

			while (y <= y_max):

				z = int(yz/y)

				if num == x**2 + 4*y*z:

					#We have found a solution to the general equation p = x^2 + 4yz (this is a windmill)
					w = [x,y,z, False, False]		
					
					#Involute our windmill to a new windmill wI
					wI = involutionI(x,y,z)		

					#Testing if our first windmill is fixed. I.e., it matches the involuted windmill
					if isFixed(w,wI):			
						w[3] = True		#Set fixed by I to true
						wI = None		#Set our new involuted windmill to None so we don't add it again since it is W
					#Else it is a new windmill (which won't be fixed since it would involute back to w)
					else:
						w[3] = False	#Set fixed by I to false (it is not fixed)			
						wI[3] = False	#Set fixed by I to false (it is not fixed)
					

					#At this point we either have one or two new windmills to add to our list. We want to see if either
					#of them are fixed by the second involution G which is our solution to p = a^2 + b^2
					if isFixed(w, involutionG(w[0],w[1],w[2])):
						w[4] = True			#Our windmill w is fixed by G
					else:
						w[4] = False		#Our windmill w is not fixed by G

					if wI != None:			#Did we get a second windmill by our involution I?
						if isFixed(wI, involutionG(wI[0],wI[1],wI[2])):		#If yes, is it fixed by G?
							wI[4] = True									#Yes, set fixed by G flag to true
						else:
							wI[4] = False									#No, set fixed by G flag to false

					#Add our windmill w if it is not already in the set S 
					if exists(windmills,w) == False:
						windmills.append(w)

					#Add our involuted windmill wI if it is not fixed and is not already in S
					if wI != None:
						if exists(windmills,wI) == False:
							windmills.append(wI)

				y += 1
		x += 1

	return windmills

def main(argv):

	try:
		num = int(sys.argv[1])
	except:
		print("Please input a number when calling zagier.py")
		sys.exit(2)

	if num % 4 != 1 or num < 3:
		print("Please enter a valid 4k+1 number greater than 2")
		sys.exit(2)
	else:
		S = findWindmills(num)
		length = len(S)
		printHeader(num,length)
		for w in S:
			printWindmill(w)

if __name__ == "__main__":
   main(sys.argv[1:])