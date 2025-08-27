# complete the function
def get_expected_cost(beds, baths):
    
    value = 80000 + (30000 * beds) + (10000 * baths)
    return value

# use the get_expected_cost function to fill in each value
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):

    cost = (sqft_walls + sqft_ceiling) / sqft_per_gallon * cost_per_gallon
    return cost

# set the project_cost variable to the cost of the project
project_cost = get_cost(432, 144, 400, 15)

import math

test_value = 2.17
rounded_value = math.ceil(test_value)
print(rounded_value)

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):

    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    gallons_to_buy = math.ceil(gallons_needed)
    cost = cost_per_gallon * gallons_to_buy
    return cost

get_actual_cost(432, 144, 400, 15) 