class Avtomobil:
    def __init__(self, model: str):
        self.model = model
        self.__eshik_ochiq = False  

    def eshikni_och(self):
        self.__eshik_ochiq = True
        print(f"{self.model} eshiklari ochildi.")

    def eshikni_yop(self):
        self.__eshik_ochiq = False
        print(f"{self.model} eshiklari yopildi.")

    def holat(self):
        if self.__eshik_ochiq:
            print(f"{self.model}: eshik ochiq.")
        else:
            print(f"{self.model}: eshik yopiq.")


mashina = Avtomobil("Chevrolet Cobalt")
mashina.eshikni_och()
mashina.holat()
mashina.eshikni_yop()
mashina.holat()