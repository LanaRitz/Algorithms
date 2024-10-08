from collections import deque # the insertion and deletion operations will take place in O(1)

bits_per_digit = 16  # the number of bits for one "digit"
base_value = 1 << bits_per_digit  # 65536

# 1. A function for calculating the number of digits in a number_______________________________________________________________________________________________________________________________________________
def get_amount_of_digits(number):  # This function counts the number of digits of a number in the number system, i.e. how many groups of 16 bits a number contains.
    digits = 0
    while number > 0:
        digits += 1
        number >>= bits_per_digit  # shift the number to the right by 16 bits
    return digits

# 3. Функция для разделения числа на части с помощью битовых операций
def split_number(number, shift_low_bits):
    high = number >> shift_low_bits  # сдвиг вправо - убираем младшие биты / делим на 2**shift_low_bits
    low = number - (high << shift_low_bits)     # восстанавливаем младший разряд: (за счет сдвига получаем нули, поэтому требуется также разность для получения младшего разряда)/ число % 2**shift_low_bits
    return high, low

# 4. A function for calculating bit shifts in bits_____________________________________________________________________________________________________________________________________________________________
def calculate_shifts(half_min_digits):
    shift_low_bits = half_min_digits * bits_per_digit
    shift_high_bits = shift_low_bits << 1
    return shift_high_bits, shift_low_bits

# 5. A function for finding the minimum number of digits_______________________________________________________________________________________________________________________________________________________
def get_min_half_digits(multiplicand, multiplier):
    min_digits = min(get_amount_of_digits(multiplicand), get_amount_of_digits(multiplier))
    return min_digits >> 1  # divide by 2 to further divide the numbers into high and low parts

# 6. The main function for splitting input numbers by Karatsuba________________________________________________________________________________________________________________________________________________
def karatsuba_split_inputs(multiplicand, multiplier):
    half_min_digits  = get_min_half_digits(multiplicand, multiplier) # get half the digits from the smallest number

    shift_high_bits, shift_low_bits = calculate_shifts(half_min_digits )

    # Разбиваем числа на "высокую" и "низкую" части
    high1, low1 = split_number(multiplicand, shift_low_bits)
    high2, low2 = split_number(multiplier, shift_low_bits)

    return [shift_high_bits, shift_low_bits, high1, low1, high2, low2]

# 1.A function to check whether a node is finite (a node that we will no longer divide into subnodes) / a pair of numbers is small enough to be multiplied in the usual way
def is_leaf(multiplicand, multiplier):
    return multiplicand < base_value or multiplier < base_value

# 2. Function for multiplying end nodes (simple multiplication)
def multiply_leaf(multiplicand, multiplier):
    return multiplicand * multiplier

# 3.A function for splitting numbers using the Karatsuba method and adding new subtasks (nodes) to the stack for further processing.
def process_node(node_stack, multiplicand, multiplier):
    intermediate_results = karatsuba_split_inputs(multiplicand, multiplier)  # get an array of shifts and the upper and lower parts of the numbers.

    shift_high_bits = intermediate_results[0]  # Смещение для старших битов
    shift_low_bits  = intermediate_results[1]  # Смещение для младших битов

    high1 = intermediate_results[2]  # Старшая часть множимого
    low1 = intermediate_results[3]   # Младшая часть множимого
    high2 = intermediate_results[4]  # Старшая часть множителя
    low2 = intermediate_results[5]   # Младшая часть множителя

    # Добавляем дочерние узлы в стек
    node_stack.append([high1, high2, 2])  # z2 - правая ветка
    node_stack.append([low1 + high1, low2 + high2, 1])  # z1 - центральная ветка
    node_stack.append([low1, low2, 0])  # z0 - левая ветка

    return shift_high_bits, shift_low_bits

# 4. Функция для обработки стеков веток и сдвигов
def process_stacks(branch_path, m_stack, z_stack):
    last_branch = branch_path.pop()
    m_pair = m_stack.pop()

    shift_high_bits = m_pair[0]
    shift_low_bits = m_pair[1]

    z0 = z_stack[0].pop()
    z1 = z_stack[1].pop()
    z2 = z_stack[2].pop()

    # Собираем результаты с учетом сдвигов
    result = (z2 << shift_high_bits) + ((z1 - z2 - z0) << shift_low_bits) + z0
    z_stack[last_branch].append(result)

# 5. The main function of the iterative algorithm____________________________________________________________________________________________________________
def karatsuba_multiply_iterative(multiplicand, multiplier):
    node_stack = deque([[multiplicand, multiplier, 0]])  # Корневой узел
    branch_path = deque()  # a map for processing nodes
    move_stack = deque()  # Stores shifts for correct node joining in step 5
    z_stack = [deque(), deque(), deque()]  # For intermediate results z0, z1, z2
    leaf_count = 0 # it tells you at what stage of execution the Karatsuba algorithm is located (z0, z1, z2)

    # We go through the node stack
    while node_stack:
        current_node = node_stack.pop()
        multiplicand_temp = current_node[0]
        multiplier_temp = current_node[1]
        branch = current_node[2]

        if is_leaf(multiplicand_temp, multiplier_temp): # If this is the root node, then multiply and save the result
            z_stack[leaf_count].append(multiply_leaf(multiplicand_temp, multiplier_temp))

            # If this is not the last stage, then we continue
            if leaf_count != 2:
                leaf_count += 1
        else:
            # If this is not the root node, then split the numbers and add nodes to the stack
            shift_high_bits, shift_low_bits = process_node(node_stack, multiplicand_temp, multiplier_temp)
            branch_path.append(branch)
            move_stack.append([shift_high_bits, shift_low_bits])
            leaf_count = 0

        # Собираем результаты, когда стек правой ветки (z2) не пуст
        while z_stack[2]:
            process_stacks(branch_path, move_stack, z_stack)

    # Возвращаем финальный результат
    return z_stack[0][0]


import random
import time


# 1. Function for generating test data_____________________________________________________________________________________________________
def generate_test_data(max_digits):  # Passing the limit of the maximum number as a power ([10^[max_digits] - 1])
    multi_list = [] # Here we will store an array of pairs of generated numbers
    random.seed(2)  # the same random numbers for good comfortable work
    for j in range(2, max_digits, 1):  # There is no point in raising 10 to 1 degree, so I started with 2
        multi_list.append([random.randint(10, 10 ** j), random.randint(10, 10 ** j)]) # adding a nested list of pairs of test numbers
    return multi_list


# 2. A function for testing the performance of Karatsuba___________________________________________________________________________________
def test_karatsuba_performance(multi_list):  # Passing a list of pairs of numbers which will multiply
    iterative_results = [] # it will store the results of the iterative Karatsuba algorithm
    start = time.process_time()  # fixing the start of the algorithm
    for multi_pair in multi_list: # take a pair of test date for multiply
        iterative_results.append(karatsuba_multiply_iterative(multi_pair[0], multi_pair[1]))
    end = time.process_time()  # Конец измерения времени
    print('Iterative algo time elapsed:', end - start) # время затраченное на выполнение
    return iterative_results  # список результатов метода


# 3. Функция для проверки точности результатов Карацубы
def check_accuracy(multi_list, iterative_results):
    true_results = [multi_pair[0] * multi_pair[1] for multi_pair in multi_list] # Вычисляем точные результаты
    is_accurate = iterative_results == true_results # Проверяем точность
    print('Iterative results accurate:', is_accurate)
    return is_accurate # Возвращаем результат проверки


# 4. Функция для вывода результатов теста
def print_test_results(multi_list, test_element, iterative_results):
    print(f'Test element {test_element}:')
    print(f'{multi_list[test_element][0]} * {multi_list[test_element][1]} =')
    print('Long multiplication:', multi_list[test_element][0] * multi_list[test_element][1])
    print('Karatsuba iterative:', iterative_results[test_element])


#import sys
#sys.set_int_max_str_digits(10000)  # ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit. For big [max_digits]

# 5. The main function for running tests_____________________________________________________________________________________________________________________________________________________
def run_tests():
    max_digits = 1000 # Random numbers containing up to [10^[max_digits] - 1] digits will be entered into the program.
    multi_list = generate_test_data(max_digits)  # Generating test data
    iterative_results = test_karatsuba_performance(multi_list)  # Тест производительности
    if check_accuracy(multi_list, iterative_results):  # Проверка точности
        test_element = max_digits - 3  # Выбор тестируемого элемента
        print_test_results(multi_list, test_element, iterative_results)  # Вывод результатов


# Start tests__________________________________________________________________________________________________________________________________________________________________________________
run_tests()
