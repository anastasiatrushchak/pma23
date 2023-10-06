class AbstractBag:
    def display(self) -> str:
        pass
class AbstractGlove:
    def display(self) -> str:
        pass
class LeatherHandbag(AbstractBag):
    def display(self) -> str:
        return "Leather handbag on display."

class FabricHandbag(AbstractBag):
    def display(self) -> str:
        return "Fabric handbag on display."

class LeatherGlove(AbstractGlove):
    def display(self) -> str:
        return "Leather gloves on display."
class KnitGlove(AbstractGlove):
    def display(self) -> str:
        return "Knit gloves on display."
class AbstractAccessoryFactory:
    def create_bag(self) -> AbstractBag:
        pass

    def create_glove(self) -> AbstractGlove:
        pass
class LeatherFactory(AbstractAccessoryFactory):
    def create_bag(self) -> AbstractBag:
        return LeatherHandbag()

    def create_glove(self) -> AbstractGlove:
        return LeatherGlove()
class FabricFactory(AbstractAccessoryFactory):
    def create_bag(self) -> AbstractBag:
        return FabricHandbag()

    def create_glove(self) -> AbstractGlove:
        return KnitGlove()
def showcase_accessories(factory: AbstractAccessoryFactory) -> None:
    bag = factory.create_bag()
    glove = factory.create_glove()

    print(bag.display())
    print(glove.display())


leather_factory = LeatherFactory()
showcase_accessories(leather_factory)

fabric_factory = FabricFactory()
showcase_accessories(fabric_factory)
