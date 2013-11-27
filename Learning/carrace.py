# from  http://maryrosecook.com/post/a-practical-introduction-to-functional-programming

# The code is still split into functions, but the functions are functional.
# There are three signs of this.
#     First, there are no longer any shared variables. time and car_positions get passed straight into race().
#     Second, functions take parameters.
#     Third, no variables are instantiated inside functions.
# All data changes are done with return values. race() recurses3 with the result of run_step_of_race().
# Each time a step generates a new state, it is passed immediately into the next step.


from random import random

def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions)

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print('')
    print('\n'.join(map(output_car, state['car_positions'])))

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})
