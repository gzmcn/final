from insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str,tecrube = float,maas = float, yeni_maas = 0):
        # tum metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        # sınır kosulu
        assert len(tc_no) == 11 , f"tc no 11 rakam icermelidir."
        assert len(ad) < 30, f"ad 30 karakterden fazla olamaz"
        assert len(soyad) < 30, f"soyad 30 karakterden fazla olamaz"
        assert yas >= 18, "gecersiz yas: yas 18 veya daha buyuk olmali."
        assert cinsiyet in ["k", "e"], "cinsiyet degeri e veya k olarak girilmeli"

        self.__yeni_maas = yeni_maas
        self.__sektor = self.get_dogru_sektor()
        self.__tecrube = tecrube
        self.__maas = maas

    def get_dogru_sektor(self):
        sektor = input("Lutfen sektoru girin (teknoloji, muhasebe, insaat, diger): ")
        while sektor not in ["teknoloji", "muhasebe", "insaat", "diger"]:
            print("Gecersiz sektor! Lutfen dogru bir sektor girin.")
            sektor = input("Lutfen sektoru girin (teknoloji, muhasebe, insaat, diger): ")
        return sektor

    def get_sektor(self, sektor):
        return sektor

    # get metodlari
    def get_tc_no(self):
        return super().get_tc_no()
    def get_ad(self):
       return super().get_ad()
    def get_soyad(self):
       return super().get_soyad()
    def get_yas(self):
       return  super().get_yas
    def get_cinsiyet(self):
       return  super().get_cinsiyet
    def get_uyruk(self):
       return  super().get_uyruk
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

    def get_yeni_maas(self):
        return self.__yeni_maas
    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas

    def zam_hakki(self):
        self.zam_orani = 0
        if self.__tecrube < 24:
            self.zam_orani = 0
        elif 24 <= self.__tecrube < 48:
            if self.__maas < 15000:
                self.zam_orani = (self.__maas % self.__tecrube) / 100
        elif self.__tecrube >= 48 and self.__maas < 25000:
            self.zam_orani = (self.__maas % self.__tecrube) / 200

        self.zam = self.zam_orani * self.get_maas()
        self.set_yeni_maas(self.get_maas() + self.zam)

       




    def __str__(self):
        return f"Kullanici bilgileri: {self.get_ad()}, {self.get_soyad()}, yeni maas: {self.get_yeni_maas()}, tecrube: {self.get_tecrube()}"












