import random

def linear_search(array, array_size, number_to_search):
    for i in range(0, array_size):
        if (array[i] == number_to_search):
            return i
    return -1

def get_array_size():
    while True:
        try:
            size = int(input("Input a size of array: "))

            if size < 0:
                print("The size of array cannot be negative. Try agayn")
            else:
                return size

        except ValueError:
            print("Please input an integer.")


def fill_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def get_number_to_search():
    while True:
        try:
            number = int(input("Input a number for search in array: "))
            return number
        except ValueError:
            print("Please input an integer.")


def test_case():
    array_size = get_array_size()
    print(f"Sze of array: {array_size}")

    random_array = fill_array(array_size)
    print(f"Array: {random_array}")

    number_to_search = get_number_to_search()

    result = linear_search(random_array, array_size, number_to_search)
    if (result == -1):
        print("Element is not exist")
    else:
        print("Element is exist by index: ", result)

test_case()

