# Multi-frame tkinter application v2.3
from tkinter import *
import tkinter as tk
import FoodOpt

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(TitlePage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class TitlePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(background="blue")
        tk.Label(self, text="Fit", bg="blue", fg="white").pack(side="top", fill="x", pady=100, padx=200)
        tk.Button(self, text="Calorie Counter",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="extra",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="extra2",
                  command=lambda: master.switch_frame(PageThree)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #root = TK()
       # root.title("Tk dropdown example")

        # Add a grid
        mainframe = Frame(self)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        # Create a Tkinter variable
        tkvar = StringVar(self)
        tkvar2 = StringVar(self)
        # Dictionary with options
        choices = FoodOpt()
        

        # tkvar.set('Pizza') # set the default option

        popupMenu = OptionMenu(mainframe, tkvar, *choices.foodList)
        Label(mainframe, text="Choose a dish").grid(row=1, column=0)
        popupMenu.grid(row=1, column=1)

        qtyMTxt = tk.Entry(mainframe)
        Label(mainframe, text="Number of Servings").grid(row=0, column=1)
        qtyMTxt.grid(row=1,column=1)

       # tk.Button(mainframe, text='Add',command=)

        # on change dropdown value
        def change_dropdown(*args):
            print(tkvar.get())

        # link function to change dropdown
        tkvar.trace('w', change_dropdown)

    #tk.Button(self, text="Return to start page",
    #         command=lambda: master.switch_frame(TitlePage)).grid(row=4, column=0)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(TitlePage)).pack()


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(TitlePage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()