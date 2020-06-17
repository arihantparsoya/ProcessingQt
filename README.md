# ProcessingQt

A python library for Processing software. 

### Requirements

ProcessingQt is built using PyQt5. PyQt5 is built on top of Qt software which needs to be installed separately. To install PyQt5, refer: https://doc.bccnsoft.com/docs/PyQt5/installation.html.

## APIs

### Structure
* setup()
* draw()
* [TODO]noLoop()
* [TODO]redraw()
* fullScreen()
* push()
* pop()


### Setting
* background()
* fill()
* noFill()
* stroke()
* noStroke()

### 2D Primitives
* arc(x, y, w, h, start, stop)
* ellipse(x, y, width, height)
* circle(x, y, radius)
* line(x1, y1, x2, y2)
* point(x, y)
* quad(x1, y1, x2, y2, x3, y3, x4, y4)
* rect(x, y, width, height)
* square(x, y, size)
* triangle(x1, y1, x2, y2, x3, y3)

### Attributes
* strokeCap()
* strokeWeight(weight)
* strokeJoin()

### Curves
* bezier()
* curve()

### Vertex
* beginContour()
* beginShape()
* bezierVertex()
* curveVertex()
* endContour()
* endShape()
* quadraticVertex()
* vertex()

### Transform
* applyMatrix()
* resetMatrix()
* rotate()
* rotateX()
* rotateY()
* rotateZ()
* scale()
* shearX()
* shearY()
* translate()

### Constants
* CLOSE
* POINTS
* LINES
* TRIANGLES
* TRIANGLE_FAN
* TRIANGLE_STRIP
* QUADS
* QUAD_STRIP

### Events

### Missing APIs
* Font
* Image
