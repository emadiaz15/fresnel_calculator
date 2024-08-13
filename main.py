# Developed by: Your Name and Surname

from gui.interface import FresnelApp
import tkinter as tk

def main():
    # Initialize the Tkinter root widget
    root = tk.Tk()
    # Instantiate the FresnelApp with the root widget
    app = FresnelApp(root)
    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
