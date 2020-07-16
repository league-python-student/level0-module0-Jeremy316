from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    i = simpledialog.askinteger(none, prompt='give me an interger')

