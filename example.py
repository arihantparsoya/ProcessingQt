from ProcessingQt import *

def setup():
	size(500, 500)

def draw():
	background(255, 255, 255)

	strokeWeight(1)
	rect(10, 10, 50, 50)
	fill(255, 0, 0)
	circle(100, 100, 30)

	strokeWeight(10)
	stroke(0, 255, 0)
	triangle(200, 200, 250, 200, 250, 250)

run()