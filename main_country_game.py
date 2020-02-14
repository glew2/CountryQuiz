from tkinter import *
import random
import time
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
        Label(self, text="Welcome To The Country Knowledge Test!", font="COMIC 14").grid(row=0, column=0, columnspan=3)
        self.rule_label1 = Label(self, text="Rules: I will give you a country to start. "
                                            "You will take the last "
                "letter of this country, and list back to me a ", font="COMIC 8")
        self.rule_label1.grid(row=1, column=0, columnspan=3)
        self.rule_label2 = Label(self, text="new country beginning with that letter. Good luck, and press start "
                         "when you are ready to begin.", font="COMIC 8")
        self.rule_label2.grid(row=2, column=0, columnspan=3)
        self.countryLabel = Label(self, text="", font="system 17")
        self.countryLabel.grid(row=3, column=0, columnspan=3)
        self.getButton = Button(self, text="Get A Country", command=self.display_country)
        self.getButton.grid(row=4, column=1)
        Label(self, text="").grid(row=6, column=0, columnspan=3)
        self.point_label = Label(self, text="Points: 0")
        self.point_label.grid(row=7, column=1)
        Button(self, text="Give Up Button", command=root.destroy).grid(row=8, column=2)
    def display_country(self):
        self.rule_label1.destroy()
        self.rule_label2.destroy()
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=5, column=1)
        self.getButton.destroy()
        Button(self, text="Submit Country", command=self.country_submitted).grid(row=4, column=1)
        self.countryLabel['text'] = self.country_list[0]
    def country_submitted(self):
        guess = self.guess_ent.get()
        if guess.title() in self.country_list and str(self.country_list[0])[-1]==guess.lower()[0]:
            self.points+=1
            self.point_label['text'] = "Points:", self.points
            self.country_list.remove(self.country_list[0])
            self.country_list.remove(guess.title())
            self.countryLabel['text'] = self.country_list[0]
        else:
            self.countryLabel['text'] = "Incorrect or Already Used Country. Try Again: " + self.country_list[0]
        if self.points==15:
            self.countryLabel['text'] = "Congratulations! You win!"


root=Tk()
root.title("Country Knowledge Tester by Grant Lewison")
root.geometry("500x500")
app = Application(root)
root.mainloop()