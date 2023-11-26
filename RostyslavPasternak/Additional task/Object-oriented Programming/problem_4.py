from ComplexNumber import ComplexNumber


def test_ComplexNumber(a, b):
    py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)

    if my_cnum.real != a or my_cnum.imag != b:
        print("__init__() set self.real and self.imag incorrectly")

    #conjugate()
    if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
        print("conjugate() failed for", py_cnum)

    #__str__().
    if str(py_cnum) != str(my_cnum):
        print("__str__() failed for", py_cnum)

    #__abs__().

    if abs(py_cnum) != abs(my_cnum):
        print("__abs__() failed for", py_cnum)

    #__eq__().
    another_cnum = ComplexNumber(a, b)
    if (py_cnum == complex(a, b)) != (my_cnum == another_cnum):
        print("__eq__() failed for", py_cnum)

    #__add__().
    add_result = py_cnum + complex(2, 3)
    my_add_result = my_cnum + ComplexNumber(2, 3)
    if add_result != my_add_result or add_result != complex(a + 2, b + 3):
        print("__add__() failed for", py_cnum)

    #__sub__().
    sub_result = py_cnum - complex(2, 3)
    my_sub_result = my_cnum - ComplexNumber(2, 3)
    if sub_result != my_sub_result or sub_result != complex(a - 2, b - 3):
        print("__sub__() failed for", py_cnum)

    #__mul__().
    mul_result = py_cnum * complex(2, 3)
    my_mul_result = my_cnum * ComplexNumber(2, 3)
    if mul_result != my_mul_result or mul_result != complex(a * 2 - b * 3, a * 3 + b * 2):
        print("__mul__() failed for", py_cnum)

    #__truediv__().
    div_result = py_cnum / complex(2, -1)
    my_div_result = my_cnum / ComplexNumber(2, -1)
    if div_result != my_div_result:
        print("__truediv__() failed for", py_cnum)
    print("All tests passed")


if __name__ == "__main__":
    test_ComplexNumber(3, 2)