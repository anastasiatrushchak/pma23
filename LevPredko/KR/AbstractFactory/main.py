from ConcreteProduct import ConcreteSmereka, ConcreteSteko


def client_code(factory):
    product_a = factory.create_first_product()
    product_b = factory.create_second_products()

    result_a = product_a.do_this_door()
    result_b = product_b.do_this_window()

    return result_a + "\n" + result_b


factory1 = ConcreteSmereka()
print('Client: Using "Smereka"')
print(client_code(factory1))
factory2 = ConcreteSteko()
print('Client: Using "Steko"')
print(client_code(factory2))
