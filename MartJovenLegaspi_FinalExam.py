from tkinter import *

class Final:
    def __init__(self, win):
        self.num1 = Label(win, text = "Enter the first number:")
        self.num1.place(x = 25, y = 25)
        self.en1 = Entry(bd = 3)
        self.en1.place(x = 170, y = 25)
        self.num2 = Label(win, text = "Enter the second number:")
        self.num2.place(x =25, y = 60)
        self.en2 = Entry(bd=3)
        self.en2.place(x = 170, y = 60)
        self.num3 = Label(win, text = "Enter the third number:")
        self.num3.place(x =25, y = 95)
        self.en3 = Entry(bd=3)
        self.en3.place(x = 170, y = 95)
        self.res = Button(win, text = "The smallest number among the three is:", command = self.small)
        self.res.place(x = 25, y = 140)
        self.er = Entry(bd=3)
        self.er.place(x=260, y=140)

    def small(self):
        self.er.delete(0, 'end')
        n1 = int(self.en1.get())
        n2 = int(self.en2.get())
        n3 = int(self.en3.get())
        result = [n1, n2, n3]
        self.er.insert(END, str(min(result)))

window = Tk()
gui = Final(window)
window.title("Final Exam")
window.geometry("400x200+10+10")
window.mainloop()