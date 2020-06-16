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

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor

from .sketch import Canvas
from .renderer2d import Renderer2D
from . import processing

import __main__
import sys
import builtins

builtins.width = 360
builtins.height = 360
builtins.frameCount = -1
builtins.frameRate = None

def run(mode="P2D"):
	if hasattr(__main__, 'setup'):
		setup_method = __main__.setup
	else:
		setup_method = setup

	if hasattr(__main__, 'draw'):
		draw_method = __main__.draw
	else:
		draw_method = draw

	application = QApplication(sys.argv)
	processing.canvas = Canvas(setup_method, draw_method)
	
	if mode == "P2D":
		processing.renderer = Renderer2D(processing.canvas)
	else:
		print("Invalid Processing Mode")

	sys.exit(application.exec_())

def size(width, height):
	builtins.width = width
	builtins.height = height
	processing.canvas.resize(width, height)

def background(r, g, b):
	processing.renderer.background(QColor(r, b, g))

def strokeWeight(weight):
	processing.renderer.strokeWeight(weight)

def strokeJoin(join):
	processing.renderer.strokeJoin(join)

def strokeCap(cap):
	processing.renderer.strokeCap(cap)

def noStroke():
	processing.renderer.stroke(QColor(0, 0, 0, 0))

def stroke(r, g, b):
	processing.renderer.stroke(QColor(r, b, g))

def noFill():
	processing.renderer.fill(QColor(0, 0, 0, 0))

def fill(r, g, b):
	processing.renderer.fill(QColor(r, b, g))

def background(r, g, b):
	processing.renderer.background(QColor(r, b, g))

