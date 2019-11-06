from tkinter import *
import time


class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        # create and link a button
        exitButton = Button(self, text='Exit', command=self.clickExitButton)
        # place button at x, y
        exitButton.place(x=0, y=0)

        self.label = Label(text='', fg='Red', font=('Helvetica', 18))
        self.label.place(relx=0.5, rely=0.5)
        self.update_clock()

    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

    def clickExitButton(self):
        exit()


root = Tk()
app = App(root)
root.wm_title('First Clock')
root.geometry('320x200')
root.after(1000, app.update_clock())
root.mainloop()
