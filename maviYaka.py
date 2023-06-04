from calisan import Calisan

class mavi_yaka(Calisan):
    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str,tecrube = float,maas = float, yipranma_payi = 0.5):
        # tum metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
    
        self.__yeni_maas = 0
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yipranma_payi = yipranma_payi

    # get metodlari
    def get_tc_no(self):
       return  self.__tc_no
    def get_ad(self):
       return  self.__ad
    def get_soyad(self):
       return  self.__soyad
    def get_yas(self):
       return  self.__yas
    def get_cinsiyet(self):
       return  self.__cinsiyet
    def get_uyruk(self):
       return  self.__uyruk
    def get_tecrube(self):
        return self.__tecrube
    def get_maas(self):
        return self.__maas
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    # set metodlari
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
    def set_maas(self, maas):
        self.__maas = maas
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def get_yeni_maas(self):
        return self.__yeni_maas
    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas

    def zam_hakki(self):
        self.zam_orani = 0
        if self.__tecrube < 24:
            self.zam_orani = (self.__yipranma_payi * 10) / 100
        elif 24 <= self.__tecrube < 48 and self.__maas < 15000:
            self.zam_orani = ((self.__maas % self.__tecrube) / 2 + (self.__yipranma_payi * 10)) / 100
        elif self.__tecrube >= 48 and self.__maas < 25000:
            self.zam_orani = ((self.__maas % self.__tecrube) / 3 + (self.__yipranma_payi * 10)) / 100

        self.zam = self.zam_orani * self.get_maas()
        # self.set_maas(self.get_maas() + self.zam)
        self.set_yeni_maas(self.get_maas() + self.zam)
       

    def __str__(self):
        return f"Kullanici bilgileri: {self.get_ad()}, {self.get_soyad()}, yeni maas: {self.get_yeni_maas()}, tecrube: {self.__tecrube}"



