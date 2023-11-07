class InvalidSize(ValueError):
    def __init__(self):
        super().__init__("Size error")
def isolate(*num, pos=3, spaces=5):
    if len(num) < pos:
        raise InvalidSize
    else:
        print(*num[:pos], sep=' ' * spaces, end=' ')
        print(*num[pos:])
        # result = (' '* spaces).join(map(str, num[:pos])) + ' ' + ' '.join(map(str, num[pos:]))
        # print(result)
        # return result


try:
    isolate(1, 2, 3, 4, 5)
    isolate(1, 2, 3, 4, 5, 6, 7, 8, pos=5)
    isolate(1, 2, 3, 4, 5, spaces=3)
except InvalidSize as e:
    print(e)