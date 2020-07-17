from tkinter import messagebox, simpledialog, Tk
from pkg_resources._vendor.packaging.markers import Variable

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0 
    # ASK A QUESTION AND CHECK THE ANSWER
    Answer = simpledialog.askstring(None, prompt='Which is a better color red or blue?')
    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct
    if Answer == "blue":
        messagebox.showinfo(message= 'Correct, Blue is a good color 1 point')
        score += 1
    
        
    if Answer == "red":
            messagebox.showerror(message= 'Eh, its to redish 0 points')
            score += 0
    #      // 4.  if the user's answer was correct, add one to their score 
    
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    Answer = simpledialog.askstring(None, prompt='What do you think is the correct answer, correct or incorrect?')
    
    if Answer == "correct":
        messagebox.showinfo(message= 'Correct! 1 point')
        
    if Answer == "incorrect":
            messagebox.showerror(message= 'Correct! 0 points')
            
  
         
         
         
    # After all the questions have been asked, tell the user their final score

    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
window.mainloop()