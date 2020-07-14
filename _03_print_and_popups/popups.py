from tkinter import messagebox, simpledialog, Tk

window = Tk()

window.withdraw()

print( 'hello from the print method' )

messagebox.showinfo(title='my first message box', message= 'my first message box')

name = simpledialog.askstring(None, prompt= "What's you name?")

messagebox.showerror(None, message="It's" + name + ",run!!!!" )

print( "This is a print with a string variable: " + name)


window.mainloop()