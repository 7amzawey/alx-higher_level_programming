def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if a > i:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception as e:
            print(e)
            result = a + b
            continue
    return result
