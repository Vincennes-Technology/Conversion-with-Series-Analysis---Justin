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
    absolute = math.sqrt((number[0] * number[0]) + (number[1] * number[1]))
    return absolute

# Function used to take two Tuples representing x + xj and put them in parallel


# Getting the basic information from the user. Mode selection, whether parallel or series
mode_select = raw_input('Hello! Will you be doing a series or parallel circuit calculation?:')

# Series Branch Calculations
if (mode_select == 'Series') or (mode_select == 'series'):
    print('For this particular experiment, I (the pi) am only capable of series AC calculations with one R, L & C.\n')
    print('If a value is not present, please type 0')
    frequency = input('\nWhat is the frequency of the source? (in Hz): ')
    voltage = input('\nWhat is the voltage of the source? (in RMS): ')
    resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')
    inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')
    inductor_resistance = input('\nWhat is the resistance of the wiring of the inductor? (in Ohms): ')
    capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')

# Some basic calculations
    omega = 2 * pi * frequency
    total_resistance = inductor_resistance + resistor_value
    inductance = omega * inductor_value
    mag_inductance = (inductor_resistance, inductance)
    mag_inductance = magnitude(mag_inductance)
    capacitance = (1/(omega * capacitor_value))
    impedance = total_resistance, (inductance + -capacitance)
    mag_impedance = magnitude(impedance)
    current = float(voltage) / float(mag_impedance)
    v_r = current * resistor_value
    v_l = current * inductance
    v_c = current * capacitance

# Phase angle calculations (tests for positive/negative phase)
    if inductance > capacitance:
        argument_send = impedance[1] / impedance[0]
    else:
        if capacitance > inductance:
            argument_send = impedance[0] / impedance[1]
        else:
            argument_send = 0
    phase_radians = math.atan(argument_send)
    phase_angle = phase_radians * 180/pi

# Printing out the results
    if capacitance > inductance:
        print('Your current will lead your voltage by %f degrees ' % phase_angle)
    if inductance > capacitance:
        print('Your current will lag your voltage by %f degrees' % phase_angle)
    print('\nYour total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
    print('That means the magnitude of your impedance is: %.2f' % mag_impedance)
    print('Which then means your current is: %e A' % current)
    print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))

# Parallel branch.
if (mode_select == 'Parallel') or (mode_select == 'parallel'):
    print('This experiment I will be performing parallel calculations. One R,L, and C is expected')
    print('If a value is not present, please type 0')
    frequency = input('\nWhat is the frequency of the source? (in Hz): ')
    voltage = input('\nWhat is the voltage of the source? (in RMS): ')
    resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')
    inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')
    inductor_resistance = input('\nWhat is the resistance of the wiring of the inductor? (in Ohms): ')
    capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')

# Some basic calculations. Polar format is utilized!
    omega = 2 * pi * frequency
    inductance = inductor_resistance, omega * inductor_value
    capacitance = 0, 1 / (omega * capacitor_value)
    polar_capacitance = rect_to_polar(capacitance[0], -capacitance[1])
    polar_inductance = rect_to_polar(inductance[0], inductance[1])
    resistance = resistor_value, 0
    one = 1, 0
    inverse_p_capacitance = complex_division(one, polar_capacitance)
    inverse_p_inductance = complex_division(one, polar_inductance)
    inverse_p_resistance = complex_division(one, resistance)
    denominator = complex_add(inverse_p_capacitance, inverse_p_inductance)
    denominator_f = complex_add(denominator, inverse_p_resistance)
    total_impedance = complex_division(one, denominator_f)
    






