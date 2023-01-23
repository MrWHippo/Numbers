from Fractions import fraction

count = 0

def addition_test(num1, den1, num2, den2, num3, den3):
    print(f"Testing {num1}/{den1} + {num2}/{den2} = {num3}/{den3}")
    f1 = fraction(num1,den1)
    f2 = fraction(num2, den2)
    result = f1.add(f2)
    if ((result.num == num3) and (result.den == den3)) or (result.num == 0 and num3 == 0) or (result.den == 0 and den3 == 0):
        return True
    else:
        return False

def subtraction_test(num1, den1, num2, den2, num3, den3):
    print(f"Testing {num1}/{den1} - {num2}/{den2} = {num3}/{den3}")
    f1 = fraction(num1,den1)
    f2 = fraction(num2, den2)
    result = f1.sub(f2)
    if ((result.num == num3) and (result.den == den3)) or (result.num == 0 and num3 == 0) or (result.den == 0 and den3 == 0):
        return True
    else:
        return False

def multiplication_test(num1, den1, num2, den2, num3, den3):
    print(f"Testing {num1}/{den1} * {num2}/{den2} = {num3}/{den3}")
    f1 = fraction(num1,den1)
    f2 = fraction(num2, den2)
    result = f1.multi(f2)
    if (result.num == num3) and (result.den == den3):
        return True
    else:
        return False

def division_test(num1, den1, num2, den2, num3, den3):
    print(f"Testing {num1}/{den1} / {num2}/{den2} = {num3}/{den3}")
    f1 = fraction(num1,den1)
    f2 = fraction(num2, den2)
    result = f1.div(f2)
    if (result.num == num3) and (result.den == den3):
        return True
    else:
        return False

tests = [lambda:addition_test(1,3,1,2,5,6), lambda: addition_test(6,7,1,2,19,14), lambda: addition_test(0,3,1,4,1,4), lambda: addition_test(-1,3,2,3,1,3), lambda: subtraction_test(1,5,-4,9,29,45), lambda: subtraction_test(4,5,2,3,2,15), lambda: subtraction_test(2,3,1,3,1,3), lambda: subtraction_test(1,8,1,8,0,8), lambda: multiplication_test(-3,5,4,5,-12,25), lambda: multiplication_test(1,2,4,5,2,5), lambda: multiplication_test(1,5,2,6,1,15), lambda: multiplication_test(2,5,5,7,2,7), lambda: multiplication_test(2,5,0,5,0,1), lambda: multiplication_test(-1,6,-8,3,4,9), lambda: division_test(-8,3,-1,2,16,3), lambda: division_test(2,7,5,7,2,5), lambda: division_test(2,5,4,5,1,2), lambda: division_test(1,15,2,6,1,5), lambda: division_test(1,9,0,1,1,0), lambda: division_test(1,-9,-6,2,1,27)]

for test in tests:
    if test():
        print("PASS")
        count += 1
    else:
        print("FAIL")

if count == len(tests):
    print("All passed")