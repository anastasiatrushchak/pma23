from Faсtory import ConcreteToyBoys,ConcreteToyGirls
def Boys(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()


    result_a = product_a.forboys()
    result_b = product_b.forboys()


    return result_a + "\n" + result_b



def Girls(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()


    result_a = product_a.forgirls()
    result_b = product_b.forgirls()


    return result_a + "\n" + result_b

factory1 = ConcreteToyBoys()
print('For Boys:')
print(Boys(factory1))
print()
factory2 = ConcreteToyGirls()
print('For Girls:')
print(Girls(factory2))