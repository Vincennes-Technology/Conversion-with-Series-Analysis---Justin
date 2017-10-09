#!/usr/bin/python
# Justin Limbach
# Complex Calculator Rev 2 10/9/2017
# Rev 2 adds polar to rect conversions and vice versa. Also adds some basic series circuit calculations.
import math
pi = 3.1415926535897932384626433832

# Expects complex numbers in (magnitude, phase) polar format. Returns the sum.

def complex_add(complex_a, complex_b):
    real_answer = complex_a[0] + complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return real_answer, imag_answer


# Expects complex numbers in (magnitude, phase) polar format. Returns the difference of B from A

def complex_subtract(complex_a, complex_b):
    real_answer = complex_a[0] - complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return real_answer, imag_answer


# Expects complex numbers in (magnitude, phase) polar format. Returns the quotient of B from A

def complex_division(complex_a, complex_b):
    real_answer = complex_a[0] / complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return real_answer, imag_answer


# Expects complex numbers in (magnitude, phase) polar format. Returns the product of A and B

def complex_multiplication(complex_a, complex_b):
    real_answer = complex_a[0] * complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return real_answer, imag_answer


# Rectangular to Polar Conversion. Takes an x & y cartesian coordinate and returns in polar format (r, theta)

def rect_to_polar(x, y):
    angle = math.atan((y/x))
    angle = angle * (180/pi)
    magnitude = (math.sqrt((x*x)+(y*y)))
    answer = magnitude, angle
    return answer

# Polar to Rect conversion. Takes a polar format number( r, theta) and returns the x & y lengths

def polar_to_rect(polar_num):
    y = polar_num[0] * (math.sin(polar_num[1] * pi/180))
    x = polar_num[0] * (math.cos(polar_num[1] * pi/180))
    rect = x, y
    return rect

# Magnitude function for later use. Takes a real + j number and returns the magnitude
def magnitude(number):
    absolute = math.sqrt((number[0] * number[0]) + (number[1]* number[1]))
    return absolute

# Getting the basic information from the user.

# coordinate_system = raw_input('Greetings User! Shall you be working in rectangular or polar format today?:\n')
print('For this particular experiment, I (the pi) am only capable of series AC calculations with one R, L & C.\n')
frequency = input('\nWhat is the frequency of the source? (in Hz): ')
voltage = input('\nWhat is the voltage of the source? (in RMS): ')
resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')
inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')
capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')

# Some basic calculations
omega = 2 * pi * frequency
inductance = omega * inductor_value
capacitance = (1/(omega * capacitor_value))
impedance = resistor_value, (inductance + -capacitance)
mag_impedance = magnitude(impedance)
current = float(voltage) / float(mag_impedance)
v_r = current * resistor_value
v_l = current * inductance
v_c = current * capacitance
print('\nYour total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
print('That means the magnitude of your impedance is: %.2f' % mag_impedance)
print('Which then means your current is: %f A' % current)
print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))
