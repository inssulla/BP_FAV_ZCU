
import math
import random


def input_values():
    status = input('Select process: Manual = 0, Random values = 1 \n')

    if int(status) == 0:
        input_angle = float(input('Write mics sound source angle (0,360): \n'))
        camera_position = float(input('Write start camera position (-180,180): \n'))
        return input_angle, camera_position
    elif int(status) == 1:
        input_angle = random.random() * 360
        camera_position = random.random() * 360
        return input_angle, camera_position
    else:
        input_values()

def angle_calculating(input_angle, camera_position):   # return current_camera_position

    if camera_position < 0:
        camera_position = 360 + camera_position

    # Robot params
    a = 1  # between center and mics
    b = 15  # between center and sound source (distance)
    ab_angle = 15  # angel between center and mics

    angel_value = 180 - input_angle  # + right side from mic, - left side from mic
    mic_angle = abs(angel_value)

    # angle calculating (mic_angle, a, b)
    sin_A = (math.sin(math.radians(mic_angle)) * a) / b
    angle_A = math.degrees(math.asin(sin_A))
    result_angle = 180 - mic_angle - angle_A
    # print(result_angle)

    if angel_value == 0:
        moving_angle = 180 - ab_angle
        current_camera_position = camera_position + moving_angle
        return current_camera_position
    elif angel_value == 180:
        moving_angle = ab_angle
        current_camera_position = camera_position + moving_angle
        return current_camera_position
    elif angel_value > 0:
        moving_angle = result_angle - ab_angle
        current_camera_position = camera_position + moving_angle
        return current_camera_position
    elif angel_value < 0:
        moving_angle = result_angle + ab_angle
        current_camera_position = camera_position - moving_angle
        return current_camera_position

if __name__ == '__main__':

    # Correct work in case when 0 angel in y
    input_angle, camera_position = input_values()   # input mics angle, current camera position

    print(f'Mics input angle: {input_angle} \nCamera position: {camera_position}')
    current_camera_position = angle_calculating(input_angle, camera_position)

    if current_camera_position > 180:
        current_camera_position = current_camera_position - 360
    elif current_camera_position < -180:
        current_camera_position = 360 + current_camera_position

    print(f'\nOutput direction: {current_camera_position}')


