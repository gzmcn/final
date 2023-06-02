from gettext import install
from insan import Insan
from issiz import Issiz
from calisan import Calisan
from maviYaka import mavi_yaka
from beyazYaka import beyaz_yaka


def main():
    insan1 = Insan("40445674801", "ayse", "kemer", 32, "k", "turk")
    insan2 = Insan("22241078301", "veli", "kul", 25, "e", "turk")

    issiz1 = Issiz("83345035901", "ali", "veli", 38, "e", "turk")
    issiz2 = Issiz("44392672731", "riza", "demir", 23, "e", "turk")
    issiz3 = Issiz("20396378341", "toprak", "fuat", 33, "e", "turk")

    issiz1.yil_degeri_ekle("mavi yaka", 1)
    issiz1.yil_degeri_ekle("beyaz yaka", 10)
    issiz1.yil_degeri_ekle("yonetici", 2)

    issiz2.yil_degeri_ekle("mavi yaka", 1)

    issiz3.yil_degeri_ekle("mavi yaka", 6)
    issiz3.yil_degeri_ekle("beyaz yaka", 1)

    calisan1 = Calisan("12345678901", "ali", "demir", 44, "e", "turk", 30, 17442)
    calisan2 = Calisan("40445674801", "ayse", "kemer", 32, "k", "turk", 70, 58695)
    calisan3 = Calisan("22241078301", "veli", "kul", 25, "e", "turk", 12, 9246)

    maviyaka1 = mavi_yaka("22241078301", "veli", "kul", 25, "e", "turk", 12, 9246)
    maviyaka2 = mavi_yaka("12345678901", "mehmet", "demir", 40, "e", "turk", 50, 19442)
    maviyaka3 = mavi_yaka("83659375027", "ayse", "oz", 46, "k", "turk", 27, 11384)

    beyazyaka1 = beyaz_yaka("40445674801", "ayse", "kemer", 32, "k", "turk", 70, 58695)
    beyazyaka2 = beyaz_yaka("12345678901", "ali", "demir", 44, "e", "turk", 30, 17442)
    beyazyaka3 = beyaz_yaka("92734872832", "yesim", "berra", "k", "turk", 44, 44837)

    print(insan1)
    print(insan2)

    print(issiz1)
    print(issiz2)
    print(issiz3)

    issizler = [issiz1, issiz2, issiz3]
    for issiz in issizler:
        issiz.statu_bul()
        print(issiz)

    calisanlar = [calisan1, calisan2, calisan3]
    for calisan in calisanlar:
        calisan.zam_hakki()
        print(calisan.get_maas())
        print(calisan)

    maviyakalar = [maviyaka1, maviyaka2, maviyaka3]
    for maviyaka in maviyakalar:
        maviyaka.zam_hakki()
        print(maviyaka.get_maas())
        print(maviyaka)

    beyazyakalar = [beyazyaka1, beyazyaka2, beyazyaka3]
    for beyazyaka in beyazyakalar:
        beyazyaka.zam_hakki()
        print(beyazyaka.get_maas())
        print(beyazyaka)



main()


