#
# Copyright (C) 2020 Arihant Parsoya
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from . import processing

shapeKind = None
vertices = []
isBezier = False
isCurve = False
isQuadratic = False
isContour = False

def beginShape(kind=None):
	global shapeKind, vertices
	shapeKind = kind
	vertices = []

def vertex(x, y):
	global vertices
	vertices.append([x, y])

def curveVertex(x, y):
	global vertices, isCurve
	isCurve = True
	vertices.append([x, y])

def quadraticVertex(cx, cy, x3, y3):
	global vertices, isQuadratic
	isQuadratic = True
	vertices.append([cx, cy, x3, y3])

def bezierVertex(x2, y2, x3, y3, x4, y4):
	global vertices, isBezier
	isBezier = True
	vertices.append([x2, y2, x3, y3, x4, y4])

def endShape(mode=None):
	global vertices, isCurve, isBezier, isQuadratic, isContour, shapeKind
	processing.renderer.endShape(mode, vertices, isCurve, isBezier, isQuadratic, isContour, shapeKind)
	isBezier = False
	isCurve = False
	isQuadratic = False
	isContour = False
