class Foydalanuvchi:
    def __init__(self, ism: str, username: str, parol: str):
        self.ism = ism
        self.username = username
        self.__parol = parol  

    def parolni_ozgartir(self, eski_parol: str, yangi_parol: str):
        if self.__parol == eski_parol:
            self.__parol = yangi_parol
            print("Parol muvaffaqiyatli o'zgartirildi.")
        else:
            print("Eski parol noto'g'ri! Parol o'zgartirilmadi.")

    def tekshir(self, parol: str) -> bool:
        natija = self.__parol == parol
        print(natija)
        return natija

user1 = Foydalanuvchi("Ali", "ali_01", "abc123")
user2 = Foydalanuvchi("Vali", "vali_99", "qwerty")

user1.tekshir("abc123")                     
user1.parolni_ozgartir("abc123", "new456")  
user1.tekshir("abc123")                      
user1.tekshir("new456")                     