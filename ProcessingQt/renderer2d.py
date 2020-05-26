#
# Copyright (C) 2017-2019 Arihant Parsoya
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

class Renderer2D:
	def __init__(self, context):
		self.ctx = context
		self.qp = QPainter(self.ctx)

		# Initiate Properties
		#self.fill = QColor(255, 255, 255)
		#self.stroke = QColor(0, 0, 0)
		self.tint = QColor(0, 0, 0)
		self.isFill = True
		self.isStroke = True
		self.isSmooth = True # Antialiasing

		# Stroke Properties
		#self.strokeWeight = 1
		#self.strokeJoin = Qt.RoundJoin
		#self.strokeCap = Qt.RoundCap

		self.pen = QPen(QColor(0, 0, 0), 1, Qt.SolidLine, 
			Qt.RoundCap, Qt.RoundJoin)
		self.brush = QColor(255, 255, 255)

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
		self.qp.begin(self.ctx)
		self.qp.setPen(QColor(0, 0, 0, 0))
		self.qp.setBrush(color)
		self.qp.drawRect(0, 0, self.ctx.size().width(), self.ctx.size().height())
		self.qp.end()

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

	def renderPath(self, path):
		self.qp.begin(self.ctx)

		if self.isStroke:
			self.qp.setPen(self.pen)
		if self.isFill:
			self.qp.setBrush(self.brush)

		if self.isSmooth:
			self.qp.setRenderHint(QPainter.Antialiasing, True)
			self.qp.setRenderHint(QPainter.HighQualityAntialiasing, True)
			self.qp.setRenderHint(QPainter.SmoothPixmapTransform, True)

		self.qp.drawPath(path)
		self.qp.end()
