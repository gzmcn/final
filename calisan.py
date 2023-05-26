from insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str,tecrube = int,maas = int, sektor = ["teknoloji", "muhasebe", "insaat", "diger"]):
        # tüm metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)

        

        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def zam_hakki(self):
        self.zam_orani = 0
        if self.__tecrube <24:
            self.zam_orani = 0
        if self.__tecrube >24 and self.__tecrube <48 and self.__maas<15000:
            self.zam_orani = self.__maas%self.__tecrube
        if self.__tecrube >= 48 and self.__maas < 25000:
            self.zam_orani = (self.__maas%self.__tecrube)/2
        self.__maas = self.zam_orani * self.__maas









