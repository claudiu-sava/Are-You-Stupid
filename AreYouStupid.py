import random
from tkinter import *

window = Tk()
window.geometry("350x300")
window.title("Are you stupid?")
window.resizable(False, False)

noButtonPaddings = [70, 50] # padx = (0, 70), pady = (0, 50)
quotes = []
with open("vars.config") as configFile:
  for line in configFile:
    quotes.append(line)


def mainPage():
  stupidLabel = Label(window, text = "Are you stupid?", font=('Helvetica bold',30))
  stupidLabel.pack(side = TOP, pady = (50, 0))

  yesButton = Button(window, text = "YES", height = 3, width = 12, command = lambda: yes())
  yesButton.pack(side = LEFT, anchor = S, padx = (70, 0), pady = (0, 50))

  noButton = Button(window, text = "NO", height = 3, width = 12, command = lambda: no())
  noButton.pack(side = RIGHT, anchor = S, padx = (0, noButtonPaddings[0]), pady = (0, noButtonPaddings[1]))
  window.mainloop()


def checkAgain():
  for widget in window.winfo_children():
    widget.destroy()
  mainPage()


def yes():
  for widget in window.winfo_children():
    widget.destroy()
  quoteToShow = random.choice(quotes)

  letters = len(quoteToShow)
  if letters >= 40:
    letterSize = 20
  elif letters >=30:
    letterSize = 30
  else:
    letterSize = 40

  if letters >= 70:
    stupidLabelTopPadding = 70
  else:
    stupidLabelTopPadding = 100

  stupidLabel = Label(window, text = quoteToShow, font=('Helvetica', letterSize), wraplength=350, justify="center")
  stupidLabel.pack(side = TOP, pady = (stupidLabelTopPadding , 0))

  tryAgainButton = Button(window, text = "Check again", command = lambda: checkAgain())
  tryAgainButton.pack(anchor = S, side = RIGHT, padx = (0, 10), pady = (0, 10))


def no():
  for widget in window.winfo_children():
    widget.destroy()
  noButtonPaddings[0] = random.randint(5, 100)
  noButtonPaddings[1] = random.randint(20, 100)
  mainPage()

mainPage()

