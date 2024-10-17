from collections import deque # the insertion and deletion operations will take place in O(1)

bits_per_digit = 16  # the number of bits for one "digit"
base_value = 1 << bits_per_digit  # 65536

# A function for calculating the number of digits in a number_______________________________________________________________________________________________________________________________________________
def get_amount_of_digits(number):  # This function divides the number into groups of 16 bits, since bits_per_digit = 16.
    digits = 0

    while number > 0:
        digits += 1
        number >>= bits_per_digit  # OR [number = number / (1 << 65536)] OR [number = number // 2^16]

    return digits

# A function for dividing a number into parts using bitwise operations__________________________________________________________________________________________________________________________________
def split_number(number, low_shift):
    high = number >> low_shift  # shift to the right - remove the lower bitshigh = {int} 242886303
    low = number - (high << low_shift)     # restoring the lowest digit: (due to the shift, we get zeros, so we also need a difference to get the lowest digit)

    return high, low

# A function for calculating bit shifts in bits_____________________________________________________________________________________________________________________________________________________________
def calculate_shifts(min_digits):
    high = min_digits * bits_per_digit
    low = high >> 1

    return high, low

# A function for finding the minimum number of digits_______________________________________________________________________________________________________________________________________________________
def get_min_digits(multiplicand, multiplier):
    min_digits = min(get_amount_of_digits(multiplicand), get_amount_of_digits(multiplier))

    return min_digits

# The main function for splitting input numbers by Karatsuba________________________________________________________________________________________________________________________________________________
def karatsuba_split_inputs(multiplicand, multiplier):
    min_digits  = get_min_digits(multiplicand, multiplier) # get half the digits from the smallest number

    high_shift, low_shift = calculate_shifts(min_digits) # get shifts

    # divide the numbers into "high" and "low" parts
    high1, low1 = split_number(multiplicand, low_shift )
    high2, low2 = split_number(multiplier, low_shift )

    return [high_shift , low_shift , high1, low1, high2, low2]

# A function to check whether a node is finite (a node that we will no longer divide into subnodes) / a pair of numbers is small enough to be multiplied in the usual way_________________________
def is_leaf(multiplicand, multiplier):
    return multiplicand < base_value or multiplier < base_value

# 2. Function for multiplying end nodes (simple multiplication)_________________________________________________________________________________________________________________________________________
def multiply_leaf(multiplicand, multiplier):
    return multiplicand * multiplier

# 3.A function for splitting numbers using the Karatsuba method and adding new subtasks (nodes) to the stack for further processing._______________________________________________________________________
def process_node(tasks, multiplicand, multiplier):
    intermediate_results = karatsuba_split_inputs(multiplicand, multiplier)  # get an array of shifts and the upper and lower parts of the numbers.

    high_shift = intermediate_results[0]
    low_shift  = intermediate_results[1]

    high1 = intermediate_results[2]
    low1 = intermediate_results[3]
    high2 = intermediate_results[4]
    low2 = intermediate_results[5]

    # Adding child nodes to the stack multiplication_tasks
    tasks.append([high1, high2, 2])  # z2 - Step 1
    tasks.append([low1 + high1, low2 + high2, 1])  # z1 - Step 2
    tasks.append([low1, low2, 0])  # z0 - Step 3

    return high_shift, low_shift

# 4. A function for processing branch stacks and shifts
def process_stacks(map_branches, move_path, z_stack):
    last_branch = map_branches.pop()
    move_pair = move_path.pop()

    shift_high_bits = move_pair[0]
    shift_low_bits = move_pair[1]

    z0 = z_stack[0].pop()
    z1 = z_stack[1].pop()
    z2 = z_stack[2].pop()

    # Collect the results taking into account the shifts
    result = (z2 << shift_high_bits) + ((z1 - z2 - z0) << shift_low_bits) + z0
    z_stack[last_branch].append(result)

# 5. The main function of the iterative algorithm__________________________________________________________________________________________________________________________________________________________
def karatsuba_multiply_iterative(multiplicand, multiplier):
    multiplication_tasks = deque([[multiplicand, multiplier, 0]])  # This stack acts as a storage for intermediate calculations, including splitting numbers into high and low parts and adding new subtasks for further processing.

    map_branches = deque()  # a map for processing nodes
    move_path = deque()  # Stores shifts for correct node joining in step 5

    z_stack = [deque(), deque(), deque()]  # For intermediate results z0, z1, z2 (step1, step2, step3)
    subtask_stage_tracker = 0 # This counter shows which branch (z0, z1, z2) is currently being calculated, and helps the algorithm determine when all three branches for the root level will be completed.

    # We go through the node stack
    while multiplication_tasks:
        current_task = multiplication_tasks.pop()

        current_multiplicand  = current_task[0]
        current_multiplier = current_task[1]

        current_branch = current_task[2]

        if is_leaf(current_multiplicand , current_multiplier): # If this is the root node, then multiply and save the result
            z_stack[subtask_stage_tracker].append(multiply_leaf(current_multiplicand , current_multiplier))

            if subtask_stage_tracker != 2: # If this is not the last stage, then we continue
                subtask_stage_tracker += 1
        else:
            # If this is not the root node, then split the numbers and add nodes to the stack
            shift_high_bits, shift_low_bits = process_node(multiplication_tasks, current_multiplicand , current_multiplier)

            map_branches.append(current_branch)
            move_path.append([shift_high_bits, shift_low_bits])

            subtask_stage_tracker = 0

        while z_stack[2]: # collecting the result
            process_stacks(map_branches, move_path, z_stack)

    return z_stack[0][0] # Returning the final result


import random
import time


# 1. Function for generating test data__________________________________________________________________________________________________________________________________________________
def generate_test_data(max_digits):  # Passing the limit of the maximum number as a power ([10^[max_digits] - 1])
    multi_data = [] # Here we will store an array of pairs of generated numbers

    random.seed(2)  # the same random numbers for good comfortable work

    for j in range(2, max_digits, 1):
        multi_data.append([random.randint(10, 10 ** j), random.randint(10, 10 ** j)]) # adding a nested list of pairs of test numbers

    return multi_data


# 2. A function for testing the performance of Karatsuba___________________________________________________________________________________
def test_karatsuba_performance(multi_list):  # Passing a list of pairs of numbers which will multiply
    iterative_results = [] # it will store the results of the iterative Karatsuba algorithm

    start = time.process_time()  # fixing the start of the algorithm
    for multi_pair in multi_list: # take a pair of test date for multiply
        iterative_results.append(karatsuba_multiply_iterative(multi_pair[0], multi_pair[1]))
    end = time.process_time()  # fixing the finish of the algorithm

    print('Iterative algo time elapsed:', end - start) # time spent on execution

    return iterative_results  # list of method results


# 3. A function to check the accuracy of Karatsuba results________________________________________________________________________________________________________________________________________
def check_accuracy(multi_list, iterative_results):
    true_results = [multi_pair[0] * multi_pair[1] for multi_pair in multi_list]

    is_accurate = iterative_results == true_results

    print('Iterative results accurate:', is_accurate)

    return is_accurate


# 4. Function for displaying test results_______________________________________________________________________________________________________________________________________________________
def print_test_results(multi_list, test_element, iterative_results):
    print(f'Test element {test_element}:')
    print(f'{multi_list[test_element][0]} * {multi_list[test_element][1]} =')

    print('Long multiplication:', multi_list[test_element][0] * multi_list[test_element][1])
    print('Karatsuba iterative:', iterative_results[test_element])


#import sys
#sys.set_int_max_str_digits(10000)  # ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit. For big [max_digits]

# 5. The main function for running tests___________________________________________________________________________________________________________________________________________________________________________
def run_tests():
    max_digits = 1000 # Random numbers containing up to [10^[max_digits] - 1] digits will be entered into the program.
    multi_data = generate_test_data(max_digits)  # Generating test data

    iterative_results = test_karatsuba_performance(multi_data)  # Get iterative Karatsuba results

    if check_accuracy(multi_data, iterative_results):  # Checking the accuracy
        test_element =  len(multi_data) - 1   # Selecting the element to be tested
        print_test_results(multi_data, test_element, iterative_results)  # Output of results


# Start tests____________________________________________________________________________________________________________________________________________________________________________________________
run_tests()
