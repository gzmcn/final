class Insan():

    def __init__(self, tc_no, ad: str, soyad: str, yas:int, cinsiyet, uyruk: str):
        # sınır kosulu
        assert len(tc_no) == 11 , f"tc no 11 rakam içermelidir."
        assert len(ad) < 30, f"ad 30 karakterden fazla olamaz"
        assert len(soyad) < 30, f"soyad 30 karakterden fazla olamaz"


        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

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
    
    # set metodlari
    def set_tc_no(self, tc_no):
       self.__tc_no = tc_no
    def set_tc_no(self, ad):
       self.__ad = ad
    def set_tc_no(self, soyad):
       self.__soyad = soyad
    def set_tc_no(self, yas):
       self.__yas = yas
    def set_tc_no(self, cinsiyet):
       self.__cinsiyet = cinsiyet
    def set_tc_no(self, uyruk):
       self.__uyruk = uyruk

    #__str__ ile kullanici bilgileri
    

    