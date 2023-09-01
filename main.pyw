from components import Window
from components import Interface

from typing import List
import tkinter as tk

import os


class App(Window):
	def __init__(self, geometry: List[int] = [500, 500],
				title: str = "my app") -> None:
		super().__init__(geometry = geometry,
						title = title)

		self.win.iconbitmap("assets/logo.ico")

		widgets = Interface(self.win)


if __name__ == '__main__':
	app = App(geometry = [800, 550],
					title = "Untitled - Notes!")
	app.run()