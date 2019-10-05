from party import PartyAnimal


class NewPartySpecies(PartyAnimal):
    points = 0
    name = ''

    def __init__(self, point=0, nam='tempNewAnimal'):
        self.name = nam
        self.points = point
        print("I am alive, Name:", self.name, " and I am New")

    def six(self):
        self.points += 6
        print(self.name, " has points : ", self.points)
        self.party(6)

    def four(self):
        self.points += 4
        print(self.name, " has points : ", self.points)
        self.party(4)

    def __del__(self):
        print("You killed me, I was New!!!")


if __name__ == '__main__':
    an = PartyAnimal(0, "OldAnimal_1")
    anNew = NewPartySpecies()
    an.party()
