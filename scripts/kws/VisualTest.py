
import tkinter
import time
from tkinter import Button
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

Window_Width = 800
Window_Height = 600
Ball_Start_XPosition = 50
Ball_Start_YPosition = 50
Ball_Radius = 30
Ball_min_movement = 5
Refresh_Sec = 0.01


def create_animation_window():
    Window = tkinter.Tk()
    Window.title("Python Guides")

    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="Blue")
    canvas.pack(fill="both", expand=True)
    return canvas

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)

def test():
    print('Its working')
    animate_ball(Ball_min_movement, Ball_min_movement)

def animate_ball(xinc, yinc):
    ball = Animation_canvas.create_oval(Ball_Start_XPosition - Ball_Radius,
                              Ball_Start_YPosition - Ball_Radius,
                              Ball_Start_XPosition + Ball_Radius,
                              Ball_Start_YPosition + Ball_Radius,
                              fill="Red", outline="Black", width=4)
    while True:
        Animation_canvas.move(ball, xinc, yinc)
        Animation_Window.update()
        time.sleep(Refresh_Sec)
        ball_pos = Animation_canvas.coords(ball)
        # unpack array to variables
        al, bl, ar, br = ball_pos
        if al < abs(xinc) or ar > Animation_Window.winfo_width() - abs(xinc):
            xinc = -xinc
        if bl < abs(yinc) or br > Animation_Window.winfo_height() - abs(yinc):
            yinc = -yinc





def display_text():
   global entry
   string= entry.get()
   # label.configure(text=string)
   print(string)

#Initialize a Label to display the User Input
label=Label(Animation_canvas, text="", font=("Courier 22 bold"))
label.pack()


#Create an Entry widget to accept User Input
entry = Entry(Animation_canvas, width= 40)
entry.pack()
entry.place(x = 100,y = 150 )




# Animation_Window = create_animation_window()
# Animation_canvas = create_animation_canvas(Animation_Window)
# B = Button(Animation_Window, text = "Start", command = display_text)
# B.place(x = 100,y = 100 )

B = Button(Animation_canvas, text = "Start", command = display_text)
B.place(x = 100,y = 100 )
# animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)

Animation_Window.mainloop()


