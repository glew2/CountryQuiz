# Do You Know Your Countries?
# Grant Lewison, ATCS Freshman 2023
from tkinter import *
import random
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.country_list = []
        file=open("countries", "r")
        for line in file:
            l=line.strip()
            self.country_list.append(l)
        random.shuffle(self.country_list)
        self.points=0
        self.create_widgets()
    def create_widgets(self):
        Label(self, text="Country Knowledge Test!", font="COMIC 14", bg="IndianRed1").grid(
            row=0, column=0, columnspan=2)
        self.rule_label = Label(self, text="Rules:")
        self.rule_label.grid(row=1, column=0)
        rules= "You will be given a country to start. You will take the last letter of this country, and submit" \
               "back to me a new country beginning with this letter, repeating for 10 rounds. Good luck."
        self.rule_text=Text(self, width=25, height=8, wrap=WORD)
        self.rule_text.grid(row=1, column=1)
        self.rule_text.insert(0.0, rules)

        self.countryLabel = Label(self, text="", font="system 17")
        self.countryLabel.grid(row=3, column=0, columnspan=2)
        self.getButton = Button(self, text="Generate Country",
                                command=self.display_country, bg="DodgerBlue2", fg="white")
        self.getButton.grid(row=4, column=0, columnspan=2)
        self.correctLabel = Label(self, text="", font="system 4", fg="green")
        self.correctLabel.grid(row=6, column=0, columnspan=2)
        self.point_label = Label(self, text="Points: 0", font="system 15")
        self.point_label.grid(row=7, column=0, columnspan=2)
        Label(self, text="").grid(row=8, column=0, columnspan=2)
        Button(self, text="Give Up Button", bg="red", fg="white", command=root.destroy).grid(row=9, column=0,
                                                                                             columnspan=2)

    def display_country(self):
        self.rule_text.destroy()
        self.rule_label.destroy()
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=4, column=0, columnspan=2)
        self.getButton.destroy()
        Button(self, text="Submit Guess", command=self.country_submitted, bg="DodgerBlue2", fg="white").grid(
            row=5, column=0, columnspan=2)
        self.countryLabel['text'] = "Country: " + self.country_list[0]
    def country_submitted(self):
        guess = self.guess_ent.get()
        if guess.title() in self.country_list and str(self.country_list[0])[-1]==guess.lower()[0]:
            self.points+=1
            self.point_label['text'] = "Points:", self.points
            self.country_list.remove(self.country_list[0])
            self.country_list.remove(guess.title())
            self.countryLabel['text'] = "Country: " + self.country_list[0]
            self.correctLabel['text'] = "Correct!"
        else:
            self.correctLabel['text']=""
            self.countryLabel['text'] = "Incorrect or Already Used Country. Try Again: " + self.country_list[0]
        if self.points==10:
            self.countryLabel['text'] = "Congratulations! You win!"
            self.guess_ent.destroy()

root=Tk()
root.title("Country Knowledge Tester by Grant Lewison")
app = Application(root)
root.mainloop()