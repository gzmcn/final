from calisan import Calisan

class beyaz_yaka(Calisan):
    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str, tecrube=float, maas= None, tesvik_primi = 2000):
        # tum metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas)

        self.__tecrube = tecrube
        self.__tesvik_primi = tesvik_primi
        self.__maas = maas if maas is not None else 0.0


    # get metodlari
    def get_tesvik_primi(self):
        return self.__tesvik_primi
    def get_maas(self):
        return self.__maas

    # set metodlari
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi
    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        self.zam = 0
        if self.__tecrube < 24:
            self.zam = self.__tesvik_primi
        elif 24 <= self.__tecrube < 48 and self.__maas < 15000:
            self.zam = ((self.__maas % self.__tecrube) * 5) + self.__tesvik_primi
        elif self.__tecrube >= 48 and self.__maas < 25000:
            self.zam = ((self.__maas % self.__tecrube) * 4) + self.__tesvik_primi

      # self.zam = self.zam_orani * self.__maas
      # self.__maas = self.zam + self.
        self.set_maas(self.get_maas() + self.zam)

      # print(self.zam_orani)
        print(self.zam)

    def __str__(self):
        return f"Kullanici bilgileri: {self.get_ad()}, {self.get_soyad()}, yeni maas: {self.__maas}, tecrube: {self.__tecrube}"



