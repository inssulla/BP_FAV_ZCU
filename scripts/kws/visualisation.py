import tkinter
import time
from tkinter import *
from tkinter import Button, Message
import math

import scripts.simulation as simulation


Window_Width = 1040
Window_Height = 600
Start_XPosition = 690
Start_YPosition = 300
Platform_Radius = 100


def create_animation_window():
    Window = tkinter.Tk()
    Window.title("Python Guides")

    Window.geometry(f'{Window_Width}x{Window_Height}')
    Window.minsize(Window_Width, Window_Height)
    Window.maxsize(Window_Width, Window_Height)
    return Window


def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="#C3C3C3") # 9BABB8 ADC4CE
    canvas.pack(fill="both", expand=True)
    return canvas

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)

frame = Frame(Animation_canvas,padx=10,pady=10,relief=RAISED, borderwidth=3)
frame.pack()
frame.place(x=20, y=20)



label1 = Label(frame, text="Actual camera position (-180,180):", fg="grey")
label1.grid(row=2, column = 0,padx = 5, pady = 5, sticky=W)

entry1 = Entry(frame, width=17)
entry1.grid(row=2, column = 1,padx = 5, pady = 5, sticky=W)
entry1['state'] = DISABLED

label2 = Label(frame, text="Mic sound source angle (0,360):", fg="grey")
label2.grid(row=3, column = 0,padx = 5, pady = 5, sticky=W)

entry2 = Entry(frame, width=17)
entry2.grid(row=3, column = 1,padx = 5, pady = 5, sticky=W)
entry2['state'] = DISABLED

label3 = Label(frame, text="Sensors values (fl1,fl2,fl3,fl4):", fg="grey")
label3.grid(row=4, column = 0,padx = 5, pady = 5, sticky=W)

entry3 = Entry(frame, width=17)
entry3.grid(row=4, column = 1,padx = 5, pady = 5, sticky=W)
entry3['state'] = DISABLED

robot_start_position = Label(frame, text="Start camera position:")
robot_start_position.grid(row=5, column = 0,padx = 5, pady = 5, sticky=W)

mic_input_angle = Label(frame, text="Mic input angle:")
mic_input_angle.grid(row=6, column = 0,padx = 5, pady = 5, sticky=W)

sensors_input_values = Label(frame, text="Sensors input values:")
sensors_input_values.grid(row=7, column = 0,padx = 5, pady = 5, sticky=W)

output_camera_position = Label(frame, text="Output camera position:")
output_camera_position.grid(row=8, column = 0,padx = 5, pady = 5, sticky=W)

actual_camera_position = Label(frame, text="Actual camera position:")
actual_camera_position.grid(row=9, column = 0,padx = 5, pady = 5, sticky=W)


# state = Label(frame, text="State:   Active")
# state.grid(row=0, column = 1,padx = 5, pady = 5, sticky=W)

# BACKGROUND
r1 = 250  # dial lines for one minute
r2 = 270
in_degree = 0
h = iter(['0', '30', '60', '90', '120', '150', '-180/180', '-150', '-120', '-90', '-60', '-30'])
for i in range(0, 36):
    in_radian = math.radians(in_degree)  # converting to radian
    if (i % 3 == 0):
        ratio = 0.94  # Long marks ( lines )
        t1 = Start_XPosition + r2 * math.sin(in_radian)  # coordinate to add text ( hour numbers )
        t2 = Start_YPosition - r2 * math.cos(in_radian)  # coordinate to add text ( hour numbers )
        Animation_canvas.create_text(t1, t2, fill='black', font="Times 10  bold", text=next(h))  # number added
    else:
        ratio = 0.97  # small marks ( lines )

    x1 = Start_XPosition + ratio * r1 * math.sin(in_radian)
    y1 = Start_YPosition - ratio * r1 * math.cos(in_radian)
    x2 = Start_XPosition + r1 * math.sin(in_radian)
    y2 = Start_YPosition - r1 * math.cos(in_radian)
    Animation_canvas.create_line(x1, y1, x2, y2, width=1)  # draw the line for segment
    in_degree = in_degree + 10  # increment for next segment

# Robot
platform = Animation_canvas.create_oval(Start_XPosition - Platform_Radius,
                                        Start_YPosition - Platform_Radius,
                                        Start_XPosition + Platform_Radius,
                                        Start_YPosition + Platform_Radius,
                                        fill="dark gray", outline="gray", width=14)

platform1 = Animation_canvas.create_oval(Start_XPosition - Platform_Radius-6,
                                        Start_YPosition - Platform_Radius-6,
                                        Start_XPosition + Platform_Radius+6,
                                        Start_YPosition + Platform_Radius+6,
                                        outline="#413F42", width=0.5)

platform2 = Animation_canvas.create_oval(Start_XPosition - Platform_Radius+6,
                                        Start_YPosition - Platform_Radius+6,
                                        Start_XPosition + Platform_Radius-6,
                                        Start_YPosition + Platform_Radius-6,
                                        outline="#413F42", width=0.5)

camera_radius = 90
mic_radius = 60
mic_angle = 30
from_angle = 0

# CAMERA
second_angle = math.radians(from_angle - 90)
second_x = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
second_y = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
camera = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x, second_y,
                                      width=2.5, fill='black', dash=(4, 2))

second_line_x = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle)
second_line_y = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle)
camera_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x, second_line_y,
                                      width=1, fill='black', dash=(4, 2))

second_line_x2 = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle) * -1
second_line_y2 = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle) * -1
camera_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x2, second_line_y2,
                                           width=1, fill='black', dash=(4, 2))

second_x1 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
second_y2 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
second_x_rec = Start_XPosition + 0.65 * camera_radius * math.cos(second_angle)
second_y_rec = Start_YPosition + 0.65 * camera_radius * math.sin(second_angle)
camera_rec = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x1, second_y2,
                                          width=14, fill='#413F42')

# second_x11 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
# second_y22 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
# second_x_rec1 = Start_XPosition + 0.8 * camera_radius * math.cos(second_angle)
# second_y_rec2 = Start_YPosition + 0.8 * camera_radius * math.sin(second_angle)
# camera_rec1 = Animation_canvas.create_line(second_x_rec1, second_y_rec2, second_x11, second_y22,
#                                           width=20, fill='black')

# MIC
second_angle2 = math.radians(from_angle - 90 - mic_angle)
second_x_mic = Start_XPosition + 0.9 * mic_radius * math.cos(second_angle2)
second_y_mic = Start_YPosition + 0.9 * mic_radius * math.sin(second_angle2)
mic = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x_mic, second_y_mic,
                                   width=2.5, fill='#0348A2', dash=(4, 2))

second_line_x_mic = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2)
second_line_y_mic = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2)
mic_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic, second_line_y_mic,
                                    width=1, fill='#0348A2', dash=(4, 2))

second_line_x_mic2 = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2) * -1
second_line_y_mic2 = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2) * -1
mic_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic2, second_line_y_mic2,
                                    width=1, fill='#0348A2', dash=(4, 2))

second_angle3 = math.radians(from_angle - 90 - mic_angle + 90)
second_line_x_mic3 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3)
second_line_y_mic3 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3)
mic_line3 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic3,
                                     second_line_y_mic3,
                                     width=1, fill='#0348A2', dash=(4, 2))

second_line_x_mic4 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3) * -1
second_line_y_mic4 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3) * -1
mic_line4 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic4,
                                     second_line_y_mic4,
                                     width=1, fill='#0348A2', dash=(4, 2))

mic_rec = Animation_canvas.create_oval(second_x_mic - 8, second_y_mic - 8, second_x_mic + 8, second_y_mic + 8,
                                       fill="#0348A2", outline="#0348A2")


# SENSORS
# sen1
second_angle_sen1 = math.radians(from_angle - 90 - 45)
second_x_sen10 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen1)
second_y_sen10 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen1)
second_x_sen1 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen1)
second_y_sen1 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen1)
sensor1 = Animation_canvas.create_line(second_x_sen10, second_y_sen10, second_x_sen1, second_y_sen1,
                                          width=10, fill="#413F42")
# sen2
second_angle_sen2 = math.radians(from_angle - 90 - 135)
second_x_sen20 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen2)
second_y_sen20 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen2)
second_x_sen2 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen2)
second_y_sen2 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen2)
sensor2 = Animation_canvas.create_line(second_x_sen20, second_y_sen20, second_x_sen2, second_y_sen2,
                                       width=10, fill="#413F42")
# sen3
second_angle_sen3 = math.radians(from_angle - 90 - 225)
second_x_sen30 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen3)
second_y_sen30 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen3)
second_x_sen3 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen3)
second_y_sen3 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen3)
sensor3 = Animation_canvas.create_line(second_x_sen30, second_y_sen30, second_x_sen3, second_y_sen3,
                                       width=10, fill="#413F42")
# sen4
second_angle_sen4 = math.radians(from_angle - 90 - 315)
second_x_sen40 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen4)
second_y_sen40 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen4)
second_x_sen4 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen4)
second_y_sen4 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen4)
sensor4 = Animation_canvas.create_line(second_x_sen40, second_y_sen40, second_x_sen4, second_y_sen4,
                                       width=10, fill="#413F42")


def count(Window, from_angle, to_angle):
    global state_value
    global process_value

    # camera_position = int(entry1.get())
    # mic_input = int(entry2.get())


    if state_value == 0:
        if process_value == 0:
            sim_value = simulation.calculate_solar_direction(process_value, entry3.get())
            from_angle = 0
            to_angle = int(sim_value[0])
            result = to_angle - from_angle
            label1_value.configure(text=0)
            label3_value.configure(text=entry3.get())
            label5_value.configure(text=to_angle)
        elif process_value == 1:
            sim_value = simulation.calculate_solar_direction(process_value)
            from_angle = 0
            to_angle = int(sim_value[0])
            label1_value.configure(text=0)
            label3_value.configure(text=str(sim_value[1]))
            label5_value.configure(text=to_angle)
            result = to_angle - from_angle

    elif state_value == 1:
        if process_value ==0:
            sim_value = simulation.calculate_camera_direction(process_value, int(entry2.get()), int(entry1.get()))
            from_angle = int(entry1.get())
            to_angle = int(sim_value[0])
            result = to_angle - from_angle
            label1_value.configure(text=from_angle)
            label2_value.configure(text=int(entry2.get()))
            label5_value.configure(text=to_angle)
        elif process_value ==1:
            sim_value = simulation.calculate_camera_direction(process_value)
            from_angle = int(sim_value[2])
            to_angle = int(sim_value[0])
            result = to_angle - from_angle
            label1_value.configure(text=from_angle)
            label2_value.configure(text=int(sim_value[1]))
            label5_value.configure(text=to_angle)

    # label1_value.configure(text=entry1.get())
    # label2_value.configure(text=entry2.get())
    # label3_value.configure(text=entry3.get())

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

    Animation_canvas.delete('all')

    # BACKGROUND
    r1 = 250  # dial lines for one minute
    r2 = 270
    in_degree = 0
    h = iter(['0', '30', '60', '90', '120', '150', '-180/180', '-150', '-120', '-90', '-60', '-30'])
    for i in range(0, 36):
        in_radian = math.radians(in_degree)  # converting to radian
        if (i % 3 == 0):
            ratio = 0.94  # Long marks ( lines )
            t1 = Start_XPosition + r2 * math.sin(in_radian)  # coordinate to add text ( hour numbers )
            t2 = Start_YPosition - r2 * math.cos(in_radian)  # coordinate to add text ( hour numbers )
            Animation_canvas.create_text(t1, t2, fill='black', font="Times 10  bold", text=next(h))  # number added
        else:
            ratio = 0.97  # small marks ( lines )

        x1 = Start_XPosition + ratio * r1 * math.sin(in_radian)
        y1 = Start_YPosition - ratio * r1 * math.cos(in_radian)
        x2 = Start_XPosition + r1 * math.sin(in_radian)
        y2 = Start_YPosition - r1 * math.cos(in_radian)
        Animation_canvas.create_line(x1, y1, x2, y2, width=1)  # draw the line for segment
        in_degree = in_degree + 10  # increment for next segment


    # Output angel shape
    in_radian = math.radians(to_angle)
    x1 = Start_XPosition + ratio * r1 * math.sin(in_radian)
    y1 = Start_YPosition - ratio * r1 * math.cos(in_radian)
    Animation_canvas.create_oval(x1 - 8,
                                 y1 - 8,
                                 x1 + 8,
                                 y1 + 8,
                                 fill="red", outline="dark red", width=3)


    # Robot
    platform = Animation_canvas.create_oval(Start_XPosition - Platform_Radius,
                                        Start_YPosition - Platform_Radius,
                                        Start_XPosition + Platform_Radius,
                                        Start_YPosition + Platform_Radius,
                                        fill="dark gray", outline="gray", width=14)

    platform1 = Animation_canvas.create_oval(Start_XPosition - Platform_Radius - 6,
                                             Start_YPosition - Platform_Radius - 6,
                                             Start_XPosition + Platform_Radius + 6,
                                             Start_YPosition + Platform_Radius + 6,
                                             outline="#413F42", width=0.5)

    platform2 = Animation_canvas.create_oval(Start_XPosition - Platform_Radius + 6,
                                             Start_YPosition - Platform_Radius + 6,
                                             Start_XPosition + Platform_Radius - 6,
                                             Start_YPosition + Platform_Radius - 6,
                                             outline="#413F42", width=0.5)


    camera_radius = 90
    mic_radius = 60
    mic_angle = 30

    # CAMERA
    second_angle = math.radians(from_angle - 90)
    second_x = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
    second_y = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
    camera = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x, second_y,
                                          width=2.5, fill='black', dash=(4, 2))

    second_line_x = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle)
    second_line_y = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle)
    camera_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x, second_line_y,
                                               width=1, fill='black', dash=(4, 2))

    second_line_x2 = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle) * -1
    second_line_y2 = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle) * -1
    camera_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x2, second_line_y2,
                                                width=1, fill='black', dash=(4, 2))

    second_x1 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
    second_y2 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
    second_x_rec = Start_XPosition + 0.65 * camera_radius * math.cos(second_angle)
    second_y_rec = Start_YPosition + 0.65 * camera_radius * math.sin(second_angle)
    camera_rec = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x1, second_y2,
                                              width=14, fill='#413F42')

    # MIC
    second_angle2 = math.radians(from_angle - 90 - mic_angle)
    second_x_mic = Start_XPosition + 0.9 * mic_radius * math.cos(second_angle2)
    second_y_mic = Start_YPosition + 0.9 * mic_radius * math.sin(second_angle2)
    mic = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x_mic, second_y_mic,
                                       width=2.5, fill='#0348A2', dash=(4, 2))

    second_line_x_mic = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2)
    second_line_y_mic = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2)
    mic_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic, second_line_y_mic,
                                            width=1, fill='#0348A2', dash=(4, 2))

    second_line_x_mic2 = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2) * -1
    second_line_y_mic2 = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2) * -1
    mic_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic2,
                                             second_line_y_mic2,
                                             width=1, fill='#0348A2', dash=(4, 2))

    second_angle3 = math.radians(from_angle - 90 - mic_angle + 90)
    second_line_x_mic3 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3)
    second_line_y_mic3 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3)
    mic_line3 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic3,
                                             second_line_y_mic3,
                                             width=1, fill='#0348A2', dash=(4, 2))

    second_line_x_mic4 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3) * -1
    second_line_y_mic4 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3) * -1
    mic_line4 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic4,
                                             second_line_y_mic4,
                                             width=1, fill='#0348A2', dash=(4, 2))

    mic_rec = Animation_canvas.create_oval(second_x_mic - 8, second_y_mic - 8, second_x_mic + 8, second_y_mic + 8,
                                           fill="#0348A2", outline="#0348A2")  # #413F42

    # SENSORS
    # sen1
    second_angle_sen1 = math.radians(from_angle - 90 - 45)
    second_x_sen10 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen1)
    second_y_sen10 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen1)
    second_x_sen1 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen1)
    second_y_sen1 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen1)
    sensor1 = Animation_canvas.create_line(second_x_sen10, second_y_sen10, second_x_sen1, second_y_sen1,
                                           width=10, fill="#413F42")
    # sen2
    second_angle_sen2 = math.radians(from_angle - 90 - 135)
    second_x_sen20 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen2)
    second_y_sen20 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen2)
    second_x_sen2 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen2)
    second_y_sen2 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen2)
    sensor2 = Animation_canvas.create_line(second_x_sen20, second_y_sen20, second_x_sen2, second_y_sen2,
                                           width=10, fill="#413F42")
    # sen3
    second_angle_sen3 = math.radians(from_angle - 90 - 225)
    second_x_sen30 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen3)
    second_y_sen30 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen3)
    second_x_sen3 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen3)
    second_y_sen3 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen3)
    sensor3 = Animation_canvas.create_line(second_x_sen30, second_y_sen30, second_x_sen3, second_y_sen3,
                                           width=10, fill="#413F42")
    # sen4
    second_angle_sen4 = math.radians(from_angle - 90 - 315)
    second_x_sen40 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen4)
    second_y_sen40 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen4)
    second_x_sen4 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen4)
    second_y_sen4 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen4)
    sensor4 = Animation_canvas.create_line(second_x_sen40, second_y_sen40, second_x_sen4, second_y_sen4,
                                           width=10, fill="#413F42")

    Window.update()

    if to_angle > from_angle:
        negative_value = 1
        result = result * negative_value
    elif to_angle < from_angle:
        negative_value = -1
        result = result * negative_value
    for i in range(result):
        i = (i + 1) * negative_value
        time.sleep(0.03)
        Animation_canvas.delete(camera)
        Animation_canvas.delete(camera_line)
        Animation_canvas.delete(camera_line2)
        Animation_canvas.delete(camera_rec)
        # Animation_canvas.delete(camera_rec1)
        Animation_canvas.delete(mic)
        Animation_canvas.delete(mic_line)
        Animation_canvas.delete(mic_line2)
        Animation_canvas.delete(mic_line3)
        Animation_canvas.delete(mic_line4)
        Animation_canvas.delete(mic_rec)
        Animation_canvas.delete(sensor1)
        Animation_canvas.delete(sensor2)
        Animation_canvas.delete(sensor3)
        Animation_canvas.delete(sensor4)
        Window.update()

        label4_value.configure(text=i + from_angle)
        label4_value.update()


        # CAMERA
        second_angle = math.radians(i + from_angle - 90)
        second_x = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
        second_y = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
        camera = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x, second_y,
                                              width=2.5, fill='black', dash=(4, 2))

        second_line_x = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle)
        second_line_y = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle)
        camera_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x, second_line_y,
                                              width=1, fill='black', dash=(4, 2))

        second_line_x2 = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle) * -1
        second_line_y2 = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle) * -1
        camera_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x2, second_line_y2,
                                                   width=1, fill='black', dash=(4, 2))

        second_x1 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
        second_y2 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
        second_x_rec = Start_XPosition + 0.65 * camera_radius * math.cos(second_angle)
        second_y_rec = Start_YPosition + 0.65 * camera_radius * math.sin(second_angle)
        camera_rec = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x1, second_y2,
                                                  width=14, fill='#413F42')

        # second_x11 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
        # second_y22 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
        # second_x_rec1 = Start_XPosition + 0.8 * camera_radius * math.cos(second_angle)
        # second_y_rec2 = Start_YPosition + 0.8 * camera_radius * math.sin(second_angle)
        # camera_rec1 = Animation_canvas.create_line(second_x_rec1, second_y_rec2, second_x11, second_y22,
        #                                           width=20, fill='black')

        # MIC
        second_angle2 = math.radians(i + from_angle - 90 - mic_angle)
        second_x_mic = Start_XPosition + 0.9 * mic_radius * math.cos(second_angle2)
        second_y_mic = Start_YPosition + 0.9 * mic_radius * math.sin(second_angle2)
        mic = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x_mic, second_y_mic,
                                           width=2.5, fill='#0348A2', dash=(4, 2))

        second_line_x_mic = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2)
        second_line_y_mic = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2)
        mic_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic, second_line_y_mic,
                                           width=1, fill='#0348A2', dash=(4, 2))

        second_line_x_mic2 = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2) * -1
        second_line_y_mic2 = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2) * -1
        mic_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic2,
                                                 second_line_y_mic2,
                                                 width=1, fill='#0348A2', dash=(4, 2))

        second_angle3 = math.radians(i + from_angle - 90 - mic_angle + 90)
        second_line_x_mic3 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3)
        second_line_y_mic3 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3)
        mic_line3 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic3,
                                                 second_line_y_mic3,
                                                 width=1, fill='#0348A2', dash=(4, 2))

        second_line_x_mic4 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3) * -1
        second_line_y_mic4 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3) * -1
        mic_line4 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic4,
                                                 second_line_y_mic4,
                                                 width=1, fill='#0348A2', dash=(4, 2))

        mic_rec = Animation_canvas.create_oval(second_x_mic - 8, second_y_mic - 8, second_x_mic + 8, second_y_mic + 8,
                                               fill="#0348A2", outline="#0348A2") # #413F42


        # SENSORS
        # sen1
        second_angle_sen1 = math.radians(i + from_angle - 90 - 45)
        second_x_sen10 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen1)
        second_y_sen10 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen1)
        second_x_sen1 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen1)
        second_y_sen1 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen1)
        sensor1 = Animation_canvas.create_line(second_x_sen10, second_y_sen10, second_x_sen1, second_y_sen1,
                                                  width=10, fill="#413F42")
        # sen2
        second_angle_sen2 = math.radians(i + from_angle - 90 - 135)
        second_x_sen20 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen2)
        second_y_sen20 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen2)
        second_x_sen2 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen2)
        second_y_sen2 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen2)
        sensor2 = Animation_canvas.create_line(second_x_sen20, second_y_sen20, second_x_sen2, second_y_sen2,
                                               width=10, fill="#413F42")
        # sen3
        second_angle_sen3 = math.radians(i + from_angle - 90 - 225)
        second_x_sen30 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen3)
        second_y_sen30 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen3)
        second_x_sen3 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen3)
        second_y_sen3 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen3)
        sensor3 = Animation_canvas.create_line(second_x_sen30, second_y_sen30, second_x_sen3, second_y_sen3,
                                               width=10, fill="#413F42")
        # sen4
        second_angle_sen4 = math.radians(i + from_angle - 90 - 315)
        second_x_sen40 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen4)
        second_y_sen40 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen4)
        second_x_sen4 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen4)
        second_y_sen4 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen4)
        sensor4 = Animation_canvas.create_line(second_x_sen40, second_y_sen40, second_x_sen4, second_y_sen4,
                                               width=10, fill="#413F42")



        Window.update()
        # text2.config(text='Test')

    #Animation_canvas.delete('all')



def refresh(Window):
    global state_value
    global process_value

    # camera_position = int(entry1.get())
    # mic_input = int(entry2.get())

    if state_value == 0:
        if entry3.get() == '':
            from_angle = 0
        else:
            if process_value == 0:
                sim_value = simulation.calculate_solar_direction(process_value, entry3.get())
                from_angle = 0
                to_angle = int(sim_value[0])
                label1_value.configure(text=0)
                label3_value.configure(text=entry3.get())
                label5_value.configure(text=to_angle)
            entry1['state'] = NORMAL
            entry2['state'] = NORMAL
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1['state'] = DISABLED
            entry2['state'] = DISABLED
            label2_value.configure(text='')

    elif state_value == 1:
        if entry2.get() == '':
            from_angle = int(entry1.get())
        else:
            if process_value == 0:
                sim_value = simulation.calculate_camera_direction(process_value, int(entry2.get()), int(entry1.get()))
                from_angle = int(entry1.get())
                to_angle = int(sim_value[0])
                label1_value.configure(text=from_angle)
                label2_value.configure(text=int(entry2.get()))
                label5_value.configure(text=to_angle)
            entry3['state'] = NORMAL
            entry3.delete(0, END)
            entry3['state'] = DISABLED
            label3_value.configure(text='')

    Animation_canvas.delete('all')

    # BACKGROUND
    r1 = 250  # dial lines for one minute
    r2 = 270
    in_degree = 0
    h = iter(['0', '30', '60', '90', '120', '150', '-180/180', '-150', '-120', '-90', '-60', '-30'])
    for i in range(0, 36):
        in_radian = math.radians(in_degree)  # converting to radian
        if (i % 3 == 0):
            ratio = 0.94  # Long marks ( lines )
            t1 = Start_XPosition + r2 * math.sin(in_radian)  # coordinate to add text ( hour numbers )
            t2 = Start_YPosition - r2 * math.cos(in_radian)  # coordinate to add text ( hour numbers )
            Animation_canvas.create_text(t1, t2, fill='black', font="Times 10  bold", text=next(h))  # number added
        else:
            ratio = 0.97  # small marks ( lines )

        x1 = Start_XPosition + ratio * r1 * math.sin(in_radian)
        y1 = Start_YPosition - ratio * r1 * math.cos(in_radian)
        x2 = Start_XPosition + r1 * math.sin(in_radian)
        y2 = Start_YPosition - r1 * math.cos(in_radian)
        Animation_canvas.create_line(x1, y1, x2, y2, width=1)  # draw the line for segment
        in_degree = in_degree + 10  # increment for next segment

    if entry2.get() != '' or entry3.get() != '':
        # Output angel shape
        in_radian = math.radians(to_angle)
        x1 = Start_XPosition + ratio * r1 * math.sin(in_radian)
        y1 = Start_YPosition - ratio * r1 * math.cos(in_radian)
        Animation_canvas.create_oval(x1 - 8,
                                     y1 - 8,
                                     x1 + 8,
                                     y1 + 8,
                                     fill="red", outline="dark red", width=3)

    # Robot
    platform = Animation_canvas.create_oval(Start_XPosition - Platform_Radius,
                                            Start_YPosition - Platform_Radius,
                                            Start_XPosition + Platform_Radius,
                                            Start_YPosition + Platform_Radius,
                                            fill="dark gray", outline="gray", width=14)

    platform1 = Animation_canvas.create_oval(Start_XPosition - Platform_Radius - 6,
                                             Start_YPosition - Platform_Radius - 6,
                                             Start_XPosition + Platform_Radius + 6,
                                             Start_YPosition + Platform_Radius + 6,
                                             outline="#413F42", width=0.5)

    platform2 = Animation_canvas.create_oval(Start_XPosition - Platform_Radius + 6,
                                             Start_YPosition - Platform_Radius + 6,
                                             Start_XPosition + Platform_Radius - 6,
                                             Start_YPosition + Platform_Radius - 6,
                                             outline="#413F42", width=0.5)

    camera_radius = 90
    mic_radius = 60
    mic_angle = 30

    # CAMERA
    second_angle = math.radians(from_angle - 90)
    second_x = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
    second_y = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
    camera = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x, second_y,
                                          width=2.5, fill='black', dash=(4, 2))

    second_line_x = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle)
    second_line_y = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle)
    camera_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x, second_line_y,
                                               width=1, fill='black', dash=(4, 2))

    second_line_x2 = Start_XPosition + 2.5 * camera_radius * math.cos(second_angle) * -1
    second_line_y2 = Start_YPosition + 2.5 * camera_radius * math.sin(second_angle) * -1
    camera_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x2, second_line_y2,
                                                width=1, fill='black', dash=(4, 2))

    second_x1 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle)
    second_y2 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle)
    second_x_rec = Start_XPosition + 0.65 * camera_radius * math.cos(second_angle)
    second_y_rec = Start_YPosition + 0.65 * camera_radius * math.sin(second_angle)
    camera_rec = Animation_canvas.create_line(second_x_rec, second_y_rec, second_x1, second_y2,
                                              width=14, fill='#413F42')


    # MIC
    second_angle2 = math.radians(from_angle - 90 - mic_angle)
    second_x_mic = Start_XPosition + 0.9 * mic_radius * math.cos(second_angle2)
    second_y_mic = Start_YPosition + 0.9 * mic_radius * math.sin(second_angle2)
    mic = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_x_mic, second_y_mic,
                                       width=2.5, fill='#0348A2', dash=(4, 2))

    second_line_x_mic = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2)
    second_line_y_mic = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2)
    mic_line = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic, second_line_y_mic,
                                            width=1, fill='#0348A2', dash=(4, 2))

    second_line_x_mic2 = Start_XPosition + 3.8 * mic_radius * math.cos(second_angle2) * -1
    second_line_y_mic2 = Start_YPosition + 3.8 * mic_radius * math.sin(second_angle2) * -1
    mic_line2 = Animation_canvas.create_line(Start_XPosition, Start_YPosition, second_line_x_mic2,
                                             second_line_y_mic2,
                                             width=1, fill='#0348A2', dash=(4, 2))

    second_angle3 = math.radians(from_angle - 90 - mic_angle + 90)
    second_line_x_mic3 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3)
    second_line_y_mic3 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3)
    mic_line3 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic3,
                                             second_line_y_mic3,
                                             width=1, fill='#0348A2', dash=(4, 2))

    second_line_x_mic4 = second_x_mic + 2.6 * mic_radius * math.cos(second_angle3) * -1
    second_line_y_mic4 = second_y_mic + 2.6 * mic_radius * math.sin(second_angle3) * -1
    mic_line4 = Animation_canvas.create_line(second_x_mic, second_y_mic, second_line_x_mic4,
                                             second_line_y_mic4,
                                             width=1, fill='#0348A2', dash=(4, 2))

    mic_rec = Animation_canvas.create_oval(second_x_mic - 8, second_y_mic - 8, second_x_mic + 8, second_y_mic + 8,
                                           fill="#0348A2", outline="#0348A2")  # #413F42

    # SENSORS
    # sen1
    second_angle_sen1 = math.radians(from_angle - 90 - 45)
    second_x_sen10 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen1)
    second_y_sen10 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen1)
    second_x_sen1 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen1)
    second_y_sen1 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen1)
    sensor1 = Animation_canvas.create_line(second_x_sen10, second_y_sen10, second_x_sen1, second_y_sen1,
                                           width=10, fill="#413F42")
    # sen2
    second_angle_sen2 = math.radians(from_angle - 90 - 135)
    second_x_sen20 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen2)
    second_y_sen20 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen2)
    second_x_sen2 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen2)
    second_y_sen2 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen2)
    sensor2 = Animation_canvas.create_line(second_x_sen20, second_y_sen20, second_x_sen2, second_y_sen2,
                                           width=10, fill="#413F42")
    # sen3
    second_angle_sen3 = math.radians(from_angle - 90 - 225)
    second_x_sen30 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen3)
    second_y_sen30 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen3)
    second_x_sen3 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen3)
    second_y_sen3 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen3)
    sensor3 = Animation_canvas.create_line(second_x_sen30, second_y_sen30, second_x_sen3, second_y_sen3,
                                           width=10, fill="#413F42")
    # sen4
    second_angle_sen4 = math.radians(from_angle - 90 - 315)
    second_x_sen40 = Start_XPosition + 0.9 * camera_radius * math.cos(second_angle_sen4)
    second_y_sen40 = Start_YPosition + 0.9 * camera_radius * math.sin(second_angle_sen4)
    second_x_sen4 = Start_XPosition + 0.85 * camera_radius * math.cos(second_angle_sen4)
    second_y_sen4 = Start_YPosition + 0.85 * camera_radius * math.sin(second_angle_sen4)
    sensor4 = Animation_canvas.create_line(second_x_sen40, second_y_sen40, second_x_sen4, second_y_sen4,
                                           width=10, fill="#413F42")

    Window.update()

def start_refresh():
    refresh(Animation_Window)

def start():
    global start_b

    start_b['state'] = DISABLED
    try:
        count(Animation_Window, 0, 180)
        start_b['state'] = NORMAL
    except:
        start_b['state'] = NORMAL

    # count(Animation_Window, 0, 180)

def state():
    global state
    global state_value
    global process_value
    global entry1
    global entry2
    global entry3
    global label1
    global label2
    global label3

    if process_value == 1:   # Auto
        if state_value == 1:   # Active
            state_value = 0
            state.configure(text="State:   Idle")
            entry1['state'] = DISABLED
            entry2['state'] = DISABLED
            entry3['state'] = DISABLED
            label1.configure(fg="grey")
            label2.configure(fg="grey")
            label3.configure(fg="grey")
        else:   # Idle
            state_value = 1
            state.configure(text="State:   Active")
            entry1['state'] = DISABLED
            entry2['state'] = DISABLED
            entry3['state'] = DISABLED
            label1.configure(fg="grey")
            label2.configure(fg="grey")
            label3.configure(fg="grey")
    else:   # Manual
        if state_value == 1:   # Active
            state_value = 0
            state.configure(text="State:   Idle")
            entry1['state'] = DISABLED
            entry2['state'] = DISABLED
            entry3['state'] = NORMAL
            label1.configure(fg="grey")
            label2.configure(fg="grey")
            label3.configure(fg="black")

        else:   # Idle
            state_value = 1
            state.configure(text="State:   Active")
            entry1['state'] = NORMAL
            entry2['state'] = NORMAL
            entry3['state'] = DISABLED
            label1.configure(fg="black")
            label2.configure(fg="black")
            label3.configure(fg="grey")


def process():
    global process
    global process_value
    global state_value
    global entry1
    global entry2
    global entry3
    global label1
    global label2
    global label3

    if state_value == 1:
        if process_value == 1:
            refresh_b['state'] = NORMAL
            process_value = 0
            process.configure(text="Process:   Manual")
            entry1['state'] = NORMAL
            entry2['state'] = NORMAL
            label1.configure(fg='black')
            label2.configure(fg='black')
        else:
            refresh_b['state'] = DISABLED
            process_value = 1
            process.configure(text="Process:   Auto")
            entry1['state'] = DISABLED
            entry2['state'] = DISABLED
            label1.configure(fg="grey")
            label2.configure(fg="grey")
    else:
        if process_value == 1:
            refresh_b['state'] = NORMAL
            process_value = 0
            process.configure(text="Process:   Manual")
            entry3['state'] = NORMAL
            label3.configure(fg='black')
        else:
            refresh_b['state'] = DISABLED
            process_value = 1
            process.configure(text="Process:   Auto")
            entry3['state'] = DISABLED
            label3.configure(fg="grey")


start_b = Button(frame, text = "Start", command = start,width=14)
start_b.grid(row=10, column = 0,padx = 5, pady = 5, sticky=W)

refresh_b = Button(frame, text = "Refresh", command = start_refresh,width=14, state=DISABLED)
refresh_b.grid(row=10, column = 1,padx = 5, pady = 5, sticky=W)

active_b = Button(frame, text = "Change", command = state,width=14)
active_b.grid(row=0, column = 1,padx = 5, pady = 5, sticky=W)
state_value = 1

state = Label(frame, text="State:   Active")
state.grid(row=0, column = 0,padx = 5, pady = 5, sticky=W)

idle_b = Button(frame, text = "Change", command = process,width=14)
idle_b.grid(row=1, column = 1,padx = 5, pady = 5, sticky=W)
process_value = 1

process = Label(frame, text="Process:   Auto")
process.grid(row=1, column = 0,padx = 5, pady = 5, sticky=W)

label1_value = Label(frame, text="")
label1_value.grid(row=5, column = 1,padx = 5, pady = 5)

label2_value = Label(frame, text="")
label2_value.grid(row=6, column = 1,padx = 5, pady = 5)

label3_value = Label(frame, text="")
label3_value.grid(row=7, column = 1,padx = 5, pady = 5)

label4_value = Label(frame, text="")
label4_value.grid(row=9, column = 1,padx = 5, pady = 5)

label5_value = Label(frame, text="")
label5_value.grid(row=8, column = 1,padx = 5, pady = 5)


if __name__ == '__main__':

    #Animation_Window = create_animation_window()
    # Animation_canvas = create_animation_canvas(Animation_Window)

    # frame = Frame(Animation_canvas,padx=10,pady=10)
    # frame.pack()
    # frame.place(x=20, y=20)
    #
    # angle = Label(frame, text="Angle")
    # angle.grid(row=0, column = 0,padx = 5, pady = 5)
    #
    # entry = Entry(frame, width=8)
    # entry.grid(row=0, column = 2,padx = 5, pady = 5)
    #
    # B = Button(frame, text = "Start", command = display_text).grid(row=1, column = 0,padx = 5, pady = 5, sticky=W)

    # B.pack()
    # B.place(x=20, y=20)


    Animation_Window.mainloop()