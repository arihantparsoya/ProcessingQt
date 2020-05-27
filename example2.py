from ProcessingQt import *
import random 

def setup():
	size(500, 500)

def draw():
	background(255, 255, 255) # only (r, g, b) API is supported for now

	s = 50
	strokeWeight(5)

	for x in range(s):
		for y in range(s):
			fill(255, 0, 0)
			point(random.randint(0, width), random.randint(0, height))

	print(frameRate)

run()