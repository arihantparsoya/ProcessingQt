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

from PyQt5.QtGui import QPainter, QColor, QPainterPath, QPen
from PyQt5.QtCore import Qt
from .constants import *

class Renderer2D:
	def __init__(self, context):
		self.ctx = context
		self.qp = QPainter()

		# Initiate Properties
		self.tint = QColor(0, 0, 0)
		self.isSmooth = True # Antialiasing

		# Stroke Properties
		self.pen = QPen(QColor(0, 0, 0), 1, Qt.SolidLine, 
			Qt.RoundCap, Qt.RoundJoin)
		# Fill Properties
		self.brush = QColor(255, 255, 255)

		self.curveTightness = 0

	def stroke(self, color):
		self.pen.setColor(color)

	def strokeWeight(self, width):
		self.pen.setWidth(width)

	def strokeJoin(self, join):
		if join == "MITER":
			self.pen.setJoinStyle(Qt.MiterJoin)
		elif join == "BEVEL":
			self.pen.setJoinStyle(Qt.BevelJoin)
		elif join == "ROUND":
			self.pen.setJoinStyle(Qt.RoundJoin)
		else: 
			print("Invalid Stroke Join")

	def strokeCap(self, cap):
		if cap == "PROJECT":
			self.pen.setJoinStyle(Qt.SquareCap)
		elif cap == "SQUARE":
			self.pen.setJoinStyle(Qt.FlatCap)
		elif cap == "ROUND":
			self.pen.setJoinStyle(Qt.RoundCap)
		else: 
			print("Invalid Stroke Cap")

	def fill(self, color):
		self.brush = color

	def background(self, color):
		#self.qp.begin(self.ctx)
		self.qp.setPen(QColor(0, 0, 0, 0))
		self.qp.setBrush(color)
		self.qp.drawRect(0, 0, self.ctx.size().width(), self.ctx.size().height())
		#self.qp.end()

	def point(self, x, y):
		path = QPainterPath()
		path.moveTo(x, y)
		path.lineTo(x + 0.1, y)

		self.renderPath(path)

	def rect(self, x, y, width, height):
		path = QPainterPath()
		path.moveTo(x, y)
		path.lineTo(x + width, y)
		path.lineTo(x + width, y + height)
		path.lineTo(x, y + height)
		path.lineTo(x, y)

		self.renderPath(path)

	def line(self, x1, y1, x2, y2):
		path = QPainterPath()
		path.moveTo(x1, y1)
		path.lineTo(x2, y2)

		self.renderPath(path)

	def square(self, x, y, s):
		self.rect(x, y, s, s) 

	def circle(self, cx, cy, r):
		self.ellipse(cx, cy, r, r)

	def ellipse(self, x, y, w, h):
		kappa = 0.5522847498
		ox = w/2 * kappa # control point offset horizontal
		oy = h/2 * kappa # control point offset vertical
		xe = x + w # x-end
		ye = y + h # y-end
		xm = x + w/2 # x-middle
		ym = y + h/2 # y-middle

		path = QPainterPath()
		path.moveTo(x, ym)
		path.cubicTo(x, ym - oy, xm - ox, y, xm, y)
		path.cubicTo(xm + ox, y, xe, ym - oy, xe, ym)
		path.cubicTo(xe, ym + oy, xm + ox, ye, xm, ye)
		path.cubicTo(xm - ox, ye, x, ym + oy, x, ym)

		self.renderPath(path)		

	def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
		path = QPainterPath()
		path.moveTo(x1, y1)
		path.lineTo(x2, y2)
		path.lineTo(x3, y3)
		path.lineTo(x4, y4)
		path.lineTo(x1, y1)

		self.renderPath(path)

	def triangle(self, x1, y1, x2, y2, x3, y3):
		path = QPainterPath()
		path.moveTo(x1, y1)
		path.lineTo(x2, y2)
		path.lineTo(x3, y3)
		path.lineTo(x1, y1)

		self.renderPath(path)

	def endShape(self, mode, vertices, isCurve, isBezier, isQuadratic, isContour, shapeKind):
		if len(vertices) == 0:
			return 
		closeShape = mode == CLOSE

		if closeShape and not isContour:
			vertices.append(vertices[0])

		if isCurve and (shapeKind == POLYGON or shapeKind == None):
			s = 1 - self.curveTightness
			path = QPainterPath()
			path.moveTo(vertices[1][0], vertices[1][1])

			for i in range(1, len(vertices) - 2):
				v = vertices[i]
				b = []
				b.append([v[0], v[1]])
				b.append([
					v[0] + (s * vertices[i + 1][0] - s * vertices[i - 1][0]) / 6,
					v[1] + (s * vertices[i + 1][1] - s * vertices[i - 1][1]) / 6
				])
				b.append([
					vertices[i + 1][0] +
						(s * vertices[i][0] - s * vertices[i + 2][0]) / 6,
					vertices[i + 1][1] + (s * vertices[i][1] - s * vertices[i + 2][1]) / 6
				])
				b.append([vertices[i + 1][0], vertices[i + 1][1]])
				path.cubicTo(
					b[1][0],
					b[1][1],
					b[2][0],
					b[2][1],
					b[3][0],
					b[3][1]
				)

			if closeShape:
				path.lineTo(vertices[i + 1][0], vertices[i + 1][1])
			self.renderPath(path)

		elif isBezier and (shapeKind == POLYGON or shapeKind == None):
			path = QPainterPath()
			path.moveTo(vertices[0][0], vertices[0][1])

			for v in vertices:
				if len(v) == 2:
					path.lineTo(v[0], v[1])
				else:
					path.cubicTo(
						v[0],
						v[1],
						v[2],
						v[3],
						v[4],
						v[5],
					)
			self.renderPath(path)

		elif isQuadratic and (shapeKind == POLYGON or shapeKind == None):
			path = QPainterPath()
			path.moveTo(vertices[0][0], vertices[0][1])
			for v in vertices:
				if len(v) == 2:
					path.lineTo(v[0], v[1])
				else:
					path.quadTo(
						v[0],
						v[1],
						v[2],
						v[3],
					)
			self.renderPath(path)

		else:
			if shapeKind == POINTS:
				for p in vertices:
					self.point(p[0], p[1])
			elif shapeKind == LINES:
				for i in range(0, len(vertices) - 1, 2):
					self.line(vertices[i][0], vertices[i][1], vertices[i + 1][0], vertices[i + 1][1])
			elif shapeKind == TRIANGLES:
				for i in range(0, len(vertices) - 2, 3):
					self.triangle(vertices[i][0], vertices[i][1], 
						vertices[i + 1][0], vertices[i + 1][1],
						vertices[i + 2][0], vertices[i + 2][1])
			elif shapeKind == TRIANGLE_STRIP:
				for i in range(len(vertices) - 2):
					self.triangle(vertices[i][0], vertices[i][1], 
						vertices[i + 1][0], vertices[i + 1][1],
						vertices[i + 2][0], vertices[i + 2][1])
			elif shapeKind == TRIANGLE_FAN:
				for i in range(1, len(vertices) - 1):
					self.triangle(vertices[0][0], vertices[0][1], 
							vertices[i][0], vertices[i][1],
							vertices[i + 1][0], vertices[i + 1][1])
			elif shapeKind == QUADS:
				for i in range(0, len(vertices) - 3, 4):
					self.quad(vertices[i][0], vertices[i][1], 
							vertices[i + 1][0], vertices[i + 1][1],
							vertices[i + 2][0], vertices[i + 2][1],
							vertices[i + 3][0], vertices[i + 3][1])
			elif shapeKind == QUAD_STRIP:
				for i in range(0, len(vertices) - 3, 2):
					self.quad(vertices[i][0], vertices[i][1], 
							vertices[i + 1][0], vertices[i + 1][1],
							vertices[i + 2][0], vertices[i + 2][1],
							vertices[i + 3][0], vertices[i + 3][1])
			else:
				path = QPainterPath()
				path.moveTo(vertices[0][0], vertices[0][1])
				for p in vertices:
					path.lineTo(p[0], p[1])
				self.renderPath(path)

		return

	def renderPath(self, path):
		self.qp.setPen(self.pen)
		self.qp.setBrush(self.brush)

		if self.isSmooth:
			self.qp.setRenderHint(QPainter.Antialiasing, True)
			self.qp.setRenderHint(QPainter.HighQualityAntialiasing, True)
			self.qp.setRenderHint(QPainter.SmoothPixmapTransform, True)

		self.qp.drawPath(path)

	def push(self):
		self.qp.save()

	def pop(self):
		self.qp.restore()

	def applyMatrix(self, a, b, c, d, e, f):
		self.qp.setWorldTransform([
				a, c, e,
				b, d, f,
				0, 0, 1
			])

	def resetMatrix(self):
		self.qp.setWorldTransform(QMatrix([
				[1, 0, 0],
				[0, 1, 0],
				[0, 0, 1]
			]))

	def rotate(self, angle):
		self.qp.rotate(angle)

	def scale(self, *args):
		if len(args) == 1:
			self.qp.scale(args[0], args[0])
		elif len(args) == 2:
			self.qp.scale(args[0], args[1])

	def shearX(self, angle):
		self.qp.shear(angle, 0)

	def shearY(self, angle):
		self.qp.shear(0, angle)

	def translate(self, x, y):
		self.qp.translate(x, y)
