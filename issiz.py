from insan import Insan



class Issiz(Insan):
    yil_degeri = {}
    etki = {}

    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str, yil_degeri=None, statu=["mavi yaka", "beyaz yaka", "yonetici"]):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__yil_degeri = yil_degeri if yil_degeri is not None else {}

    def get_yil_degeri(self):
        return self.__yil_degeri

    def get_statu(self):
        return self.__statu

    def set_yil_degeri(self, yil_degeri):
        self.__yil_degeri = yil_degeri

    def set_statu(self, statu):
        self.__statu = statu

    def statu_bul(self):
        etkiler = {"mavi yaka": 0.2, "beyaz yaka": 0.35, "yonetici": 0.45}
        en_uygun_statu = ""
        max_etki = 0

        for statu, yil_degeri in self.__yil_degeri.items():
            if statu in etkiler:
                etki = etkiler.get(statu) * yil_degeri
                if etki > max_etki:
                    max_etki = etki
                    en_uygun_statu = statu

        self.__en_uygun_statu = en_uygun_statu


    def yil_degeri_ekle(self, statu, yil_degeri):
        try:
            yil_degeri = int(yil_degeri)
            if yil_degeri < 0:
                raise ValueError("Yil degeri negatif olamaz.")
            self.__yil_degeri[statu] = yil_degeri
            self.statu_bul()
        except ValueError as e:
            print("Hata:", str(e))
        except TypeError:
            print("Hata: Yil degeri bir sayi olmalidir.")



    def __str__(self):
        return self.__en_uygun_statu


issiz = Issiz("12345678901", "ali", "demir", 44, "e", "turk")
issiz.yil_degeri_ekle("mavi yaka", 1)
issiz.yil_degeri_ekle("beyaz yaka", 10)
issiz.yil_degeri_ekle("yonetici", 2)
print(issiz)


















