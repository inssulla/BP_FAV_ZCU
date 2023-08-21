import tkinter
import time
from tkinter import *
from tkinter import Button, Message
import math


Window_Width = 800
Window_Height = 600
Start_XPosition = 400
Start_YPosition = 300
Platform_Radius = 100

def create_animation_window():
    Window = tkinter.Tk()
    Window.title("Python Guides")

    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="#9BABB8") # 9BABB8 ADC4CE
    canvas.pack(fill="both", expand=True)
    return canvas

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)

def count(Window, from_angle, to_angle):

    from_angle = 0
    to_angle = 180
    result = to_angle - from_angle

    text = Label(Window, text='test')
    text.pack()

    platform = Animation_canvas.create_oval(Start_XPosition - Platform_Radius,
                                        Start_YPosition - Platform_Radius,
                                        Start_XPosition + Platform_Radius,
                                        Start_YPosition + Platform_Radius,
                                        fill="dark gray", outline="gray", width=14)
    

    

    camera_radius = 90
    mic_radius = 60
    mic_angle = 30

    second_angle = math.radians(from_angle - 90)
    second_x = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
    second_y = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
    camera = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x, second_y,
                                         width=3, fill='black')

    second_angle2 = math.radians(from_angle - 90 - mic_angle)
    second_x_mic = Start_XPosition + 0.9 * mic_radius * math.cos(second_angle2)
    second_y_mic = Start_YPosition + 0.9 * mic_radius * math.sin(second_angle2)
    mic = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x_mic, second_y_mic,
                                          width=3, fill='black')

    camera_rec = Animation_canvas.create_line(Start_XPosition + 20, Start_YPosition + 20, second_x, second_y,
                                         width=3, fill='red')

    mic_rec = Animation_canvas.create_oval(second_x_mic - 10, second_y_mic - 10, second_x_mic + 10, second_y_mic + 10,
                                           fill="red")

    second_angle_sen1 = math.radians(from_angle - 90 - 45)
    second_x_sen10 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen1)
    second_y_sen10 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen1)
    second_x_sen1 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen1)
    second_y_sen1 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen1)
    sensor1 = Animation_canvas.create_line(second_x_sen10, second_y_sen10, second_x_sen1, second_y_sen1,
                                           width=10, fill='red')

    for i in range(result):
        time.sleep(0.03)
        Animation_canvas.delete(camera)
        Animation_canvas.delete(camera_rec)
        Animation_canvas.delete(mic)
        Animation_canvas.delete(mic_rec)
        Animation_canvas.delete(sensor1)
        Window.update()

        text.config(text=i)
        text.update()

        second_angle = math.radians(i + from_angle - 90)
        second_x = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
        second_y = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
        camera = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x, second_y,
                                              width=3, fill='black', dash=(4, 2))

        second_x_rec = Start_XPosition + 0.7 * camera_radius * math.cos(second_angle)
        second_y_rec = Start_YPosition + 0.7 * camera_radius * math.sin(second_angle)
        camera_rec = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x, second_y,
                                                  width=15, fill='red')

        second_angle2 = math.radians(i + from_angle - 90 - mic_angle)
        second_x_mic = Start_XPosition + 0.9 * mic_radius * math.cos(second_angle2)
        second_y_mic = Start_YPosition + 0.9 * mic_radius * math.sin(second_angle2)
        mic = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x_mic, second_y_mic,
                                           width=3, fill='black', dash=(4, 2))
        mic_rec = Animation_canvas.create_oval(second_x_mic - 7, second_y_mic - 7, second_x_mic + 7, second_y_mic + 7, fill="red", outline="red")



        second_angle_sen1 = math.radians(i + from_angle - 90 - 45)
        second_x_sen10 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen1)
        second_y_sen10 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen1)
        second_x_sen1 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen1)
        second_y_sen1 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen1)
        sensor1 = Animation_canvas.create_line(second_x_sen10, second_y_sen10, second_x_sen1, second_y_sen1,
                                                  width=10, fill='red')

        # second_angle_sen1 = math.radians(i + from_angle - 90 - 45)
        # second_x_rec = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle)
        # second_y_rec = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle)
        # sensor2 = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x, second_y,
        #                                           width=10, fill='red')
        # second_x_rec = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle)
        # second_y_rec = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle)
        # sensor3 = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x, second_y,
        #                                           width=10, fill='red')
        # second_x_rec = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle)
        # second_y_rec = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle)
        # sensor4 = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x, second_y,
        #                                           width=10, fill='red')


        Window.update()
        # text2.config(text='Test')

    text.destroy()
    Animation_canvas.delete('all')



def start():
    print('Its working')
    count(Animation_Window, 0, 180)



if __name__ == '__main__':

    #Animation_Window = create_animation_window()
    # Animation_canvas = create_animation_canvas(Animation_Window)

    B = Button(Animation_Window, text = "Start", command = start)
    B.place(x = 20,y = 20 )


    Animation_Window.mainloop()