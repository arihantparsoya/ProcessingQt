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

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter

from .renderer2d import Renderer2D
from . import processing
import builtins
import time

class Canvas(QWidget):
	def __init__(self, setupMethod, drawMethod,
		frameRate=60):
		super().__init__()

		self.setupCompleted = False
		self.setupMethod = setupMethod
		self.drawMethod = drawMethod

		self.timer = QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(1000/frameRate)

		self.elapsedTime = time.perf_counter() # used to calculate frameRate

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, builtins.width, builtins.height)
		self.setWindowTitle('Processing')
		self.show()

	def keyPressEvent(self, event):
		# Close the window on ESCAPE
		if event.key() == Qt.Key_Escape:
			self.close()

	def paintEvent(self, e):
		builtins.frameRate = round(1/(time.perf_counter() - self.elapsedTime), 2)
		self.elapsedTime = time.perf_counter()

		if not self.setupCompleted:
			# do the setup
			self.setupCompleted = True
			processing.renderer.qp.begin(self)
			builtins.frameCount += 1
			self.setupMethod()
		else:
			# call the draw function
			processing.renderer.qp.begin(self)
			builtins.frameCount += 1
			self.drawMethod()

		processing.renderer.qp.end()
