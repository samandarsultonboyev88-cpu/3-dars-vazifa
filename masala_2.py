class Kitob:
    def __init__(self, nomi: str, muallif: str):
        self.nomi = nomi
        self.muallif = muallif
        self.__ijarada = False 

    def ijaraga_ber(self):
        if not self.__ijarada:
            self.__ijarada = True
            print(f'"{self.nomi}" kitobi ijaraga berildi.')
        else:
            print(f'"{self.nomi}" kitobi allaqachon ijarada.')

    def qaytarish(self):
        if self.__ijarada:
            self.__ijarada = False
            print(f'"{self.nomi}" kitobi kutubxonaga qaytarildi.')
        else:
            print(f'"{self.nomi}" kitobi hozir kutubxonada.')

    def holat(self):
        if self.__ijarada:
            print(f'"{self.nomi}" ({self.muallif}) — hozir ijarada.')
        else:
            print(f'"{self.nomi}" ({self.muallif}) — kutubxonada mavjud (ijaraga berilmagan).')


kitob = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
kitob.ijaraga_ber()
kitob.holat()
kitob.qaytarish()
kitob.holat()