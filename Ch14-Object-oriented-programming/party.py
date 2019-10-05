class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, num=0, nam='tempAnimal'):
        self.x = num
        self.name = nam
        print("I am alive, Name:",self.name," and I am Old")

    def party(self, inc=1):
        self.x += inc
        print("So far x: ", self.x)

    def __del__(self):
        print("You killed me, I was old !!!")
