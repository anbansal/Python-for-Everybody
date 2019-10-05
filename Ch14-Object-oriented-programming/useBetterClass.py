class PartyAnimal:
    x = 0

    def __init__(self, num=0):
        print("I am alive")
        self.x = num

    def party(self, inc=1):
        self.x += inc
        print("So far x: ", self.x)

    def __del__(self):
        print("You killed me")


if __name__ == '__main__':
    an = PartyAnimal()
    an.party()
    an.party(34)
    print(an.x)
    PartyAnimal.party(an)

    print("Type: ", type(an))
    print("Dir: ", dir(an))
    print("Type: ", type(an.x))
    print("Type: ", type(an.party))
