# (c) Maximilian Spiekermann, 2016
# Module for advanced mathamatical operations with Python 3.x.x

# Fixes floating-point issues
# Has issues: addition of negative decimal numbers

# EXPERIMENTAL
def add (*args):

    len_dec = 1
    total   = 0.0

    for arg in args:
        arg = float(arg)
        arg = str(arg)
        arg = list(arg)
        arg = arg[arg.index(".")+1:]
        if len(arg) > len_dec:
            len_dec = len(arg)

    for arg in args:
        total += arg
        total = round(total*(10**len_dec))/(10**len_dec)

    return total

def add_old (*args):

    sum_1   = 0
    sum_2   = 0
    sum_3   = []
    len_dec = 1

    total   = 0

    # sum_1 = Ganze Zahl
    for arg in args:

        arg = float (arg)
        arg = str (arg)
        arg = list (arg)
        arg = arg[:arg.index(".")]
        arg = int(''.join(arg))
        sum_1 += arg

    # sum_2 = Dezimalzahl
    for arg in args:

        arg = float (arg)
        arg = str (arg)
        arg = list (arg)
        arg = arg[arg.index(".")+1:]
        if len(arg) > len_dec:
            len_dec = len(arg)
    for arg in args:

        arg = float (arg)
        arg = str (arg)
        arg = list (arg)
        arg = arg[arg.index(".")+1:]
        for _ in range (len_dec-len(arg)):
            arg.append("0")
        arg = ''.join(arg)
        sum_2 += int(arg)

    # sum_3 = Dezimalzahl -> Ganze Zahl
    sum_2 = list(str(sum_2))
    if len(sum_2)-len_dec == 0:
        sum_3 = 0
    else:
        for x in range(0, len(sum_2)-len_dec):
            sum_3.append(sum_2[0])
            sum_2 = sum_2[1:]
        sum_3 = ''.join(sum_3)
    sum_2 = ''.join(sum_2)


    # total = (sum_1+sum_3).(sum_2)
    total = int(sum_1) + int(sum_3)
    total = list(str(total))
    total.append (".")
    total.append (sum_2)
    total = ''.join(total)
    total = float(total)
    return total

def devidable (num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

def devidable_old (num1, num2):
    math = num1/num2
    math1 = int(math)
    if (math1 != math):
        math1 = float
    else:
        math1 = int
    if (math1 == int):
        return True
    else:
        return False

def roundto (num, accuracy = 10):
    if (accuracy <= 0):
        return "Invalid use of the 'roundto'-function!\n"
    if (accuracy < 1):
        accuracy = list(str(accuracy))
        return round(num*(10**len(accuracy[accuracy.index(".")+1:])))/(10**len(accuracy[accuracy.index(".")+1:]))
    else:
        return round(num/accuracy)*accuracy
