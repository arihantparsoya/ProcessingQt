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
import math

def translate(x, y):
	processing.renderer.translate(x, y)

def push():
	processing.renderer.push()
	
def pop():
	processing.renderer.pop()

def applyMatrix(a, b, c, d, e, f):
	processing.renderer.applyMatrix(a, b, c, d, e, f)

def resetMatrix():
	return

def rotate(angle):
	processing.renderer.rotate(math.degrees(angle))

def scale(*args):
	processing.renderer.scale(*args)

def shearX(angle):
	processing.renderer.shearX(math.degrees(angle))

def shearY(angle):
	processing.renderer.shearY(math.degrees(angle))

