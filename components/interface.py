import tkinter as tk
from tkinter.filedialog import *

import os

class Interface:

	__file = None

	def __init__(self, root) -> None:
		self.root = root

		# Create a text area
		self.text = tk.Text(bd = 0,
					  		font = ("Consolas", 13),
							
							)
		self.text.pack(padx = 0, pady = 0,
				expand = 1, fill = tk.BOTH)

		# Create a menu
		mainmenu = tk.Menu(self.root)
		self.root.config(menu = mainmenu)

		filemenu = tk.Menu(mainmenu, tearoff = 0)
		filemenu.add_command(label = "Open", command = self.__openFile)
		filemenu.add_command(label = "New", command = self.__newFile)
		filemenu.add_command(label = "Save", command = self.__saveFile)
		filemenu.add_command(label = "Save as", command = self.__saveasFile)
		filemenu.add_separator()
		filemenu.add_command(label = "Exit", command = self.__quitApp)

		mainmenu.add_cascade(label = "File", menu = filemenu)

	def __quitApp(self) -> None:
		self.root.destroy()

	def __openFile(self) -> None:
		global file_name

		file_name = askopenfilename(defaultextension = "*.*", 
										filetypes = [ ("All Files", "*.*"),
													("Text Documents", "*.txt") ])
		self.__file = file_name

		if self.__file == "":
			# No file to open
			self.__file = None
			print(self.__file)
		else:
			self.root.title(os.path.basename(self.__file) + " - Notes!")
			self.text.delete(1.0, tk.END)

			with open(self.__file, "r") as file:
				self.text.insert(1.0, file.read())

	def __newFile(self) -> None:
		self.root.title("Untitled - Notes!")
		self.__file = None
		self.text.delete(1.0, tk.END)

	def __saveasFile(self) -> None:
		self.__file = asksaveasfilename(initialfile = "Untitled.txt",
									defaultextension = ".txt",
										filetypes=[("All Files", "*.*"),
													("Text Documents", "*.txt")])
		if self.__file == "":
			self.__file = None
		else:
			# Try to save the file
			with open(self.__file, "w") as file:
				file.write(self.text.get(1.0, tk.END))

			self.root.title(os.path.basename(self.__file) + " - Notes!")

	def __saveFile(self) -> None:
		if self.__file == None:
			# Save as new file
			self.__saveasFile()
		else:
			with open(self.__file, "w") as file:
				file.write(self.text.get(1.0, tk.END))