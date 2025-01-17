import math
import os
from datetime import datetime

pi = math.pi
now = datetime.now()
today = now.date()
answer = True
print(today)

def check_input(user_input):
    if user_input in ['S', 'P', 'T', 'O', 'R', 'B']:
        return False
    else:
        print('You must input a correct type.')
        return True

def recommend_psi(t_type, c_type):
    pressure_map = {
        'P': 32,
        'T': 35,
        'O': 30
    }

    if c_type == 'R':
        pressure_map['P'] = 30
        pressure_map['T'] = 32
        pressure_map['O'] = 28
    elif c_type == 'B':
        pressure_map['P'] = 34
        pressure_map['T'] = 36
        pressure_map['O'] = 32
    elif c_type == 'S':
        return 'not available; Solid Tires do not need air pressure. Therefore 0'
    return pressure_map.get(t_type)

def calculate_volume(width, aspect, diameter):
    return (pi*width**2*aspect*(width*aspect+2540*diameter))/10_000_000_000

w = int(input('Enter the width of the tire in mm (ex205): '))
a = int(input('Enter the aspect ratio of the tire (ex60): '))
d = int(input('Enter the diameter of the wheel in inches (ex15): '))
volume = calculate_volume(w, a, d)
while answer == True:
    tire_type = input('Enter your tire type (Passenger, Truck/SUV, Other): ').strip().upper()
    t = list(tire_type)[0]
    answer = check_input(t)
    if (answer == True):
        continue
    construction = input('What construction type is your tire? (Radial, Bias, or Solid): ').strip().upper()
    c = list(construction)[0]
    answer = check_input(c)
recommended = recommend_psi(t, c)

print(f'The approximate volume is {volume:.2f} liters')
print(f'Recommended Tire Pressure is {recommended}psi.')

try:
    with open('./volumes.txt', mode='at') as file:
        file.write(f'Date: {today}{os.linesep}Width: {w}{os.linesep}Aspect Ratio: {a}{os.linesep}Diameter: {d}{os.linesep}Volume to nearest tenth: {volume:.2f}{os.linesep}Recommended PSI: {recommended}{os.linesep}')
except Exception as e:
    print(f'Error: {e}')