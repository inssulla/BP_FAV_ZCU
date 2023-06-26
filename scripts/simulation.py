
import math
import random



def solar_input_values():
    status = input('Select process: Manual = 0, Random values = 1 \n')

    if int(status) == 0:
        array = input('Add array in format: float0, float1, float2, float3: \n')
        print(f'Input: {array}')
        array = array.split(',')
        for i in range(len(array)):
            array[i] = float(array[i])
        return list(array)
    elif int(status) == 1:
        array = []
        for f in range(4):
            array.append(random.random() * 1000)
        print(f'Input: {array}')
        return list(array)
    else:
        solar_input_values()

def solar_calculating(sensors_value):

    sensors = [-135, -45, 45, 135]

    if len(sensors) == len(sensors_value):

        max_index = sensors_value.index(max(sensors_value))

        if max_index == (len(sensors) - 1):
            left_sensor_index = max_index - 1
            right_sensor_index = 0
        else:
            left_sensor_index = max_index - 1
            right_sensor_index = max_index + 1


        if sensors_value[max_index] == sensors_value[right_sensor_index]:
            max_value_sensor = sensors[max_index]
            moving_angle = 45
            result_angle = max_value_sensor + moving_angle
        elif sensors_value[max_index] == sensors_value[left_sensor_index]:
            max_value_sensor = sensors[max_index]
            moving_angle = -45
            result_angle = max_value_sensor + moving_angle
        else:
            moving_angle = ((sensors_value[right_sensor_index] - sensors_value[left_sensor_index]) / (sensors_value[right_sensor_index] + sensors_value[left_sensor_index])) / 2 * 180
            max_value_sensor = sensors[max_index]
            result_angle = max_value_sensor + moving_angle

        return result_angle
    else:
        'Error'


def calculate_solar_direction():
    sensors_value = solar_input_values()
    solar_direction = solar_calculating(sensors_value)

    if solar_direction > 180:
        solar_direction = solar_direction - 360
    elif solar_direction < -180:
        solar_direction = 360 + solar_direction

    print(f'\nOutput direction: {solar_direction}\n')


# --------------------


def mics_input_values():
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
        mics_input_values()

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


def calculate_camera_direction():

    # Correct work in case when 0 angel in y
    input_angle, camera_position = mics_input_values()  # input mics angle, current camera position

    print(f'Mics input angle: {input_angle} \nCamera position: {camera_position}')
    current_camera_position = angle_calculating(input_angle, camera_position)

    if current_camera_position > 180:
        current_camera_position = current_camera_position - 360
    elif current_camera_position < -180:
        current_camera_position = 360 + current_camera_position

    print(f'\nOutput direction: {current_camera_position}\n')



if __name__ == '__main__':

    status = input('Select status: Idle = 0, Active = 1 \n')

    if int(status) == 0:
        calculate_solar_direction()
    elif int(status) == 1:
        calculate_camera_direction()

