
import random


def input_values():
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
        input_values()

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



if __name__ == '__main__':

    sensors_value = input_values()
    solar_direction = solar_calculating(sensors_value)

    if solar_direction > 180:
        solar_direction = solar_direction - 360
    elif solar_direction < -180:
        solar_direction = 360 + solar_direction

    print(f'\nOutput direction: {solar_direction}')

