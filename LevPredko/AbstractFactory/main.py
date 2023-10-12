from ConcreteProduct import ConcreteMitsubishi, ConcreteSteko
def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    result_a = product_a.do_something()
    result_b = product_b.do_another_thing()

    return result_a + "\n" + result_b


factory1 = ConcreteMitsubishi()
print('Client: Using "Mitsubishi"')
print(client_code(factory1))

factory2 = ConcreteSteko()
print('Client: Using "Steko"')
print(client_code(factory2))
