#compound value
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    return present_value * (1+rate_per_period) ** periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print future_value(500, .04, 10, 10)


import math

def area_regular_polygon(num_sides, length_sides):
    return ((num_sides * length_sides ** 2) / 4.0000) / math.tan(math.pi / num_sides)

print area_regular_polygon(5,7)
print area_regular_polygon(7,3.0000)
print '---'

print (5 * 7 ** 2) * 0.25
print (5 * 7 ** 2) / 4.0

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

print max_of_3(89,45,344)

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
