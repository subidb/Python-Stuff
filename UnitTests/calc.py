# def divide3(x, y):
#     err1 = "Error, Cannot divide by 0!"
#     try:
#         return x/y
#     except ZeroDivisionError:
#         print("Error!: Cannot divide by zero")
#
#
# divide3(2, 0)


def divide1(x, y):
    if y == 0:
        raise ValueError('Error: Cannot divide by zero!')
    return x / y


def divide2(x, y):
    print(x / y)


def power_recur(x, exp):
    if x == 0:
        return 0
    if exp < 0:
        exp = abs(exp)
        if exp == 0:
            z = 1
        else:
            z = x * power_recur(x, exp - 1)
        return 1 / z

    if exp == 0:
        return 1
    else:
        return x * power_recur(x, exp - 1)


# print(power_recur(3, -2))


def power_recur2(x, exp):
    if x == 0:
        return 0
    if exp < 0:
        return (1 / x) * power_recur2(x, exp + 1)
    if exp == 0:
        return 1
    else:
        return x * power_recur2(x, exp - 1)


# print(power_recur2(2, -2))


def power_iter(x, exp):
    if x == 0:
        return 0
    if exp < 0:
        exp = abs(exp)
        y = 1
        for i in range(exp):
            y = x * y
        return 1 / y
    y = 1
    for i in range(exp):
        y = x * y
    return y


def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + n


def squarelist(list1):
    list2 = [x * x for x in list1]
    return list2


l1 = [1, 3, 4]
print(squarelist(l1))
# list1 = []
# list2 = []
# list3 = list1
#
# if list1 == list2:  # true because both lists are empty
#     print("True")
# else:
#     print("False")
#
# if list1 is list2:  #false because lists are at different memorylocations(list 1 and list 2 refer to diff ..memlocas)
#     print("True")
# else:
#     print("False")
#
# if list1 is list3:  # true because both lists are pointing to the same object
#     print("True")
# else:
#     print("False")


# def power_recur3(x, exp):
#     if exp < 0:
#         if exp == 0:
#             v = 1
#         else:
#             v = x * power_recur2(x, exp + 1)
#         return 1 / v
#
#     if exp == 0:
#         return 1
#     else:
#         return x * power_recur2(x, exp - 1)
#
#
# print(power_recur3(2, -2))
