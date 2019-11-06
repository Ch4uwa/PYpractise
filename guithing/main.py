import tkinter as tk
import time


class App(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=tk.BOTH, expand=1)
        # create and link a button
        exitButton = tk.Button(self, text='Exit', command=self.clickExitButton)
        # place button at x, y
        exitButton.place(x=0, y=0)

        self.label = tk.Label(text='', fg='Red', font=('Helvetica', 18))
        self.label.place(relx=0.5, rely=0.5)
        self.update_clock()

    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

    def clickExitButton(self):
        exit()


root = tk.Tk()
app = App(root)
root.wm_title('First Clock')
root.geometry('320x200')
root.after(1000, app.update_clock())
root.mainloop()
