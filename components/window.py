from typing import List

import tkinter as tk


class Window:
	def __init__(self, geometry: List[int] = [500, 500],
						title: str = "my app") -> None:
		self.geometry = geometry
		self.window_size = self.tk_geometry(self.geometry)

		self.win = tk.Tk()
		self.win.geometry(self.window_size)
		self.win.title(title)

	def tk_geometry(self, input_geometry: List[int]) -> str:
		return f"{input_geometry[0]}x{input_geometry[1]}"

	def run(self):
		self.win.mainloop()