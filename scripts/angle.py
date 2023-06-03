
import math


def angle_calculating(input_angle, camera_position):   # return current_camera_position

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

    input_angle = 270   # input mics angle
    camera_position = 270   # current camera position

    current_camera_position = angle_calculating(input_angle, camera_position)
    print(current_camera_position)


