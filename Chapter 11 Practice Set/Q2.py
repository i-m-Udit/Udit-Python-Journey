class Animals:
    def __init__(self,animals):
        self._animals=animals
class Pets(Animals):
    def __init__(self,animals,pets):
        self._pets=pets
        super().__init__(animals)
class Dogs(Pets):
    def __init__(self,animals,pets):
        super().__init__(animals,pets)
    def bark(self,bark):
        self._bark=bark
        print(self._bark)
Tommy=Dogs("Mammal","Dog")
Tommy.bark("Woff Woff!")