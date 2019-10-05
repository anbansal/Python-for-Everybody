class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print("So far x: ",self.x)


if __name__ == '__main__':
    an = PartyAnimal()
    an.party()
    an.party()
    print(an.x)
    PartyAnimal.party(an)

    print("Type: ", type(an))
    print("Dir: ",dir(an))
    print("Type: ",type(an.x))
    print("Type: ",type(an.party))