#!/usr/bin/python
from Tkinter import Tk
from Graphics import text_canvas
from Input import user_input

if __name__ == '__main__':
    root = Tk()
    input_handler = user_input.user_input()
    input_handler.start_instance('test.py')
    app = text_canvas.text_canvas(root, 20, input_handler)
    root.mainloop()

