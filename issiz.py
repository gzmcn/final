from insan import Insan



class Issiz(Insan):
    yil_degeri = {}

    def __init__(self, tc_no, ad: str, soyad: str, yas: int, cinsiyet, uyruk: str, yil_degeri = int):
        # tüm metodlari ve degiskenleri tekrar yazmamak icin super fonksiyonunu kullaniyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)

        self.__yil_degeri = yil_degeri

    # get metodlari
    def get_yil_degeri(self):
        return self.__yil_degeri

    # set metodlari
    def set_yil_degeri(self, yil_degeri):
        self.__yil_degeri = yil_degeri







