list = [25, 50, 10, 15]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def calc_total(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def calc_total_plus(list):
    sum = 0
    sum = sum(list)
    return sum


print(is_even(15))
print(is_even(54))
print(calc_total(list))
