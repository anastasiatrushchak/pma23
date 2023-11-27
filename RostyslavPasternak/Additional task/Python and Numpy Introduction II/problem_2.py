class InvalidSize(ValueError):
    def __init__(self):
        super().__init__("Size error")

def first_half(list):
    if len(list) == 0:
        raise InvalidSize
    return list[:int(len(list)/2)]
def backward(list):
    if len(list) == 0:
        raise InvalidSize
    return list[::-1]

if __name__ == "__main__":
    try:
    #first_half
        print("first_half:")
        print(first_half([1, 2, 3, 4, 5]))
        print(first_half("Pasternak"))

    #backward
        print("backward:")
        print(backward([1, 2, 3, 4, 5]))
        print(backward("Pasternak"))
    except InvalidSize as e:
        print(e)