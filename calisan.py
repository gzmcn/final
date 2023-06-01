from insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str,tecrube = float,maas = float):
        # tum metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)

        

        self.__sektor = self.get_dogru_sektor()
        self.__tecrube = tecrube
        self.__maas = maas

    def get_dogru_sektor(self):
        sektor = input("Lutfen sektoru girin (teknoloji, muhasebe, insaat, diger): ")
        while sektor not in ["teknoloji", "muhasebe", "insaat", "diger"]:
            print("Gecersiz sektor! Lutfen dogru bir sektor girin.")
            sektor = input("Lutfen sektoru girin (teknoloji, muhasebe, insaat, diger): ")
        return sektor

    # get metodlari
    def get_sektor(self):
        return self.__sektor
    def get_tecrube(self):
        return self.__tecrube
    def get_maas(self):
        return self.__maas
    
    # set metodlari
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        self.zam_orani = 0
        if self.__tecrube < 24:
            self.zam_orani = 0
        elif 24 <= self.__tecrube < 48 and self.__maas < 15000:
            self.zam_orani = (self.__maas * self.__tecrube) / 100
        elif self.__tecrube >= 48 and self.__maas < 25000:
            self.zam_orani = (self.__maas * self.__tecrube) / 200

        # self.zam = self.zam_orani * self.__maas
        # self.set_maas(self.get_maas() + self.zam)
        self.zam = self.zam_orani
        self.set_maas(self.get_maas() + self.zam)

        print(self.zam_orani)
        print(self.zam)




    def __str__(self):
        return f"Kullanici bilgileri: {self.get_ad()}, {self.get_soyad()}, yeni maas: {self.__maas}, tecrube: {self.__tecrube}"












