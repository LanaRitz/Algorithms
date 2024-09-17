# Последовательный алгоритм Карацуба.
# Алгоритм Карацубы — метод быстрого умножения со сложностью вычисления nlog23.
# Алгоритм, умножение в столбик, требует n2 операций.
# При длине чисел короче нескольких десятков знаков, быстрее работает обычное умножение.

#0) разбить числа пополам на a,b,c,d
#1) (a*c)*10^4 + (((a+b)*(c+d))-(b*d)-(a*c))*10^2 + (b*d)
#2) тестирующая функция


def split_number(number):
    str_number = str(number)
    mid_index = len(str_number) // 2

    part1 = str_number[0:mid_index]
    part2 = str_number[mid_index:len(str_number)]

    return int(part1), int(part2)

def split_two_numbers(x, y):
    a, b = split_number(x)
    c, d = split_number(y)

    return a, b, c, d

def calculate_karatsuba(a, b, c, d):
    ac = a * c
    bd = b * d
    ab_cd = (a + b) * (c + d)

    n = max(len(str(a)), len(str(b)))

    result = (ac * 10 ** (2 * n)) + ((ab_cd - bd - ac) * 10 ** n) + bd

    return result

def multiply_large_numbers(x, y):
    if len(str(x)) > 30 or len(str(y)) > 30:
        a, b, c, d = split_two_numbers(x, y)
        return calculate_karatsuba(a, b, c, d)
    else:
        return x * y

def test_multiply_large_numbers(test_cases):
    for i, (x, y) in enumerate(test_cases):
        result = multiply_large_numbers(x, y)
        print(f"Тестовый случай {i + 1}:")
        print(f"  x = {x}")
        print(f"  y = {y}")
        print(f"  Результат умножения: {result}")
        print("-" * 40)

if __name__ == '__main__':
    test_cases = [
        (14568, 65336),  #Небольшое нечетная одинаковая длина (убирала проверку на >30 в методе multiply_large_numbers(x, y))
        (1246, 568),     #Небольшое четное/нечет разная длина (убирала проверку на >30 в методе multiply_large_numbers(x, y))
        (123456789012345678901234567890, 987654321098765432109876543210),  #Длинные числа, больше 30 знаков
        (12345678901234567890, 98765432109876543210),  #Меньше, около 30 знаков
        (9999999999999999999999999999999999999999, 9999999999999999999999999999999999999999),  #Очень большие числа
    ]

    test_multiply_large_numbers(test_cases)

