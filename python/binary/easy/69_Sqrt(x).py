def square(x):
    if x < 2:
        return x
    low = 2
    high = x

    while low <= high:
        mid = (low + high) // 2
        root = mid * mid
        if root < x:
            low = mid + 1
        elif root > x:
            high = mid - 1
        else:
            return mid
    return low - 1

print(square(20))

###(Newton–Raphson)
def mySqrt(x):
    if x < 2:
        return x

    y = x / 2  # начальное приближение
    while True:
        next_y = (y + x / y) / 2
        if abs(y - next_y) < 1e-6:  # условие остановки
            break
        y = next_y
    return int(next_y)  # округляем вниз

