import random
from tkinter import Tk, Label, Entry, Button

class OtterGame:
  def __init__(self, master):
    self.master = master
    master.title("Otter Number Guessing Game")

    self.secret_number = random.randint(1, 100)
    self.guess_count = 0

    # darkmode
    bg_color = "black"
    text_color = "white"  #makes this shit actually readble

    self.instruction_label = Label(master, text="I'm thinking of a number between 1 and 100. Can you guess it?", bg=bg_color, fg=text_color)
    self.instruction_label.pack()

    self.guess_entry = Entry(master, bg=bg_color, fg=text_color)
    self.guess_entry.pack()

    self.guess_button = Button(master, text="Guess!", command=self.check_guess, bg=bg_color, fg=text_color)
    self.guess_button.pack()

    self.feedback_label = Label(master, text="", bg=bg_color, fg=text_color)
    self.feedback_label.pack()

  def check_guess(self):
    try:
      guess = int(self.guess_entry.get())
      self.guess_count += 1

      if guess == self.secret_number:
        self.feedback_label.config(text=f"You guessed it in {self.guess_count} tries! Hooray!", bg="green", fg="purple")
        self.guess_button.config(state="disabled")
      elif guess < self.secret_number:
        self.feedback_label.config(text="Too low! Try again.", bg="red", fg="purple")
      else:
        self.feedback_label.config(text="Too high! Try again.", bg="red", fg="purple")

      self.guess_entry.delete(0, 'end')  # 200 pumps the text box thingy
    except ValueError:
      self.feedback_label.config(text="Please enter a valid number.", bg="red", fg="purple")

if __name__ == '__main__':
  root = Tk()
  root.configure(bg="black")  # background 4 main
  game = OtterGame(root)
  root.mainloop()
  #go listen to $uicideboy$ instead of reading my shitty comments
