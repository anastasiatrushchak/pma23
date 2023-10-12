from factory_class import Factory
from elite_factory_class import  EliteFactory
from common_factory_class import CommonFactory


def function(factory: Factory):
    print(factory)
    print(factory.getMeat())
    print(factory.getDairy())

eliteFactory = EliteFactory()
commonFactory = CommonFactory()
function(eliteFactory)
function(commonFactory)
