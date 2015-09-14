from TwitterFollowBot import TwitterBot
from tkinter import Tk, Frame, BOTH

class Follower(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent, background="white")

		self.parent = parent

		self.initUI()

	def initUI(self):
		self.parent.title("twitbot by @tylerdarby_")
		self.pack(fill=BOTH, expand=1)


def main():
	root = Tk()
	root.geometry("800x500+300+300")

	app = Follower(root)
	root.mainloop()


if __name__ == '__main__':
	main() 