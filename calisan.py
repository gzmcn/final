from insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str,tecrube = int,maas = int):
        # tüm metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)

        

        self.__sektor = self.__get_dogru_sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def __get_dogru_sektor(self):
        sektor = input("Lütfen sektörü girin (teknoloji, muhasebe, inþaat, diðer): ")
        while sektor not in ["teknoloji", "muhasebe", "inþaat", "diðer"]:
            print("Geçersiz sektör! Lütfen doðru bir sektör girin.")
            sektor = input("Lütfen sektörü girin (teknoloji, muhasebe, inþaat, diðer): ")
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
        if self.__tecrube <24:
            self.zam_orani = 0
        elif self.__tecrube >24 and self.__tecrube <48 and self.__maas<15000:
            self.zam_orani = self.__maas%self.__tecrube
        elif self.__tecrube >= 48 and self.__maas < 25000:
            self.zam_orani = (self.__maas%self.__tecrube)/2
        self.__maas = self.zam_orani * self.__maas

        self.__maas = self.__maas + self.zam_orani












