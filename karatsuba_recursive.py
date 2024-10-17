import random
import time

threshold_value = 2 ** 16

# Amount of digits in the number_____________________________________0_____________________________________________________________________________________________________________________________
def amount_digits(number):
    digits = 0

    while number > 0:
        digits += 1
        number //= threshold_value

    return digits

# find min amount digits of number_______________________________________________0__________________________________________________________________________________________________________________________________
def get_min_digits(multiplicand, multiplier):
    return(min(amount_digits(multiplicand), amount_digits(multiplier)))

# get shifts for splitting numbers and for the 5 step of the algorithm____________0___________________________________________________________________________________________________________________________
def get_shifts(multiplicand, multiplier):
    min_digits = get_min_digits(multiplicand, multiplier)

    shift_forHigh = min_digits * 16
    shift_forLow = shift_forHigh // 2

    return shift_forHigh, shift_forLow

# I split the number through shifts. Example data._______________________0_________________________________________________________________________________________________________________________________________
def get_parts_ofNumber(number, shift): # 6553665536, 24
    high = number >> shift # 0b110000110
    low = number - (high << shift) # (high << shift) == 0b110000110000000000000000000000000, low == 0b110000110101000010000000000000000

    return high, low

# Classical multiplication of numbers < threshold_value__________________0________________________________________________________________________________________________________________________________
def calculate_roots(multiplicand, multiplier):
    return multiplicand * multiplier

# get bool root or not_____________________________________________________0_________________________________________________________________________________________________________________________
def root_number(multiplicand, multiplier):
    return multiplicand < threshold_value or multiplier < threshold_value

# Karatsube algorithm_________________________________________________________0_______________________________________________________________________________________________________________________________________________________________________________
def karatsuba_recursive(multiplicand, multiplier):
    if root_number(multiplicand, multiplier):
        return calculate_roots(multiplicand, multiplier)

    shift_all_len, shift_Low = get_shifts(multiplicand, multiplier)

    high1, low1 = get_parts_ofNumber(multiplicand, shift_Low)
    high2, low2 = get_parts_ofNumber(multiplier, shift_Low)

    step1 = karatsuba_recursive(high1, high2)
    step2 = karatsuba_recursive(low1, low2)
    step3 = karatsuba_recursive((high1 + low1), (high2 + low2))

    result = (step1 << shift_all_len) + ((step3 - step2 - step1) << shift_Low) + step2

    return result

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def get_test_multyList(max_degree):
    test_values = []

    for i in range(2, max_degree, 1):
        test_values.append([random.randint(10, 10 ** i), random.randint(10,10 ** i)])

    return test_values

#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def execute_code(values):
    recursive_results = []

    start = time.process_time()
    for pair in values:
        recursive_results.append(karatsuba_recursive(pair[0], pair[1]))
    end = time.process_time()

    print('The running time of the recursive algorithm: ', (end - start))

    return recursive_results

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def check_correctness_algorithm(test_values, recursive_results):
    true_results = []

    for pair in test_values:
        true_results.append(pair[0] * pair[1])

    is_correct = true_results == recursive_results
    print('Correct algorithm: ', is_correct)

    return is_correct

#___________________________________________________________________________________________________________________________________________________________________________________________________________
def print_results_of_code(values, elem, recursive_results):
    print(f'Test element: {elem}')
    print(f'{values[elem][0]} * {values[elem][1]} =')
    print('Long multiplication:', values[elem][0] * values[elem][1])
    print(f'Karatsuba iterative: {recursive_results[elem]}')

#___________________________________________________________________________________________________________________________________________________________________________________________________________________
def test_case():
    test_values = get_test_multyList(1000)

    recursive_results = execute_code(test_values)

    if check_correctness_algorithm(test_values, recursive_results):
        test_elem = len(test_values) - 1
        print_results_of_code(test_values, test_elem, recursive_results)

#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________
test_case()