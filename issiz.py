from insan import Insan



class Issiz(Insan):
    yil_degeri = {}
    etki = float
    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str, yil_degeri, statu = ["mavi yaka", "beyaz yaka", "yonetici"]):
        # tüm metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)

        self.__yil_degeri = yil_degeri
        self.__statu = statu
        self.statu_bul()

       # Issiz.yil_degeri.append(self.statu,self.yil_degeri)

    # get metodlari
    def get_yil_degeri(self):
        return self.__yil_degeri
    def get_statu(self):
        return self.__statu

    # set metodlari
    def set_yil_degeri(self, yil_degeri=int):
        self.__yil_degeri = yil_degeri
    def set_statu(self, statu):
        self.__statu = statu

    def statu_bul(self):
        etkiler = {"mavi yaka": 0.2, "beyaz yaka": 0.35, "yonetici": 0.45}
        en_uygun_statu = ""















