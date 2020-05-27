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

def point(x, y):
	processing.renderer.point(x, y, width, height)

def line(x1, y1, x2, y2):
	processing.renderer.line(x1, y1, x2, y2)

def square(x, y, s):
	processing.renderer.square(x, y, s) 

def rect(x, y, width, height):
	processing.renderer.rect(x, y, width, height)

def circle(x, y, r):
	processing.renderer.circle(x, y, r)

def ellipse(x, y, width, height):
	processing.renderer.ellipse(x, y, width, height)

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
	processing.renderer.quad(x1, y1, x2, y2, x3, y3, x4, y4)

def triangle(x1, y1, x2, y2, x3, y3):
	processing.renderer.triangle(x1, y1, x2, y2, x3, y3)
