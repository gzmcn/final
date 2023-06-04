from gettext import install
from insan import Insan
from issiz import Issiz
from calisan import Calisan
from maviYaka import mavi_yaka
from beyazYaka import beyaz_yaka
import pandas as pd



def main():
    try:


        insan1 = Insan("40445674801", "ayse", "kemer", 32, "k", "turk")
        insan2 = Insan("22241078301", "veli", "kul", 25, "e", "turk")

        print(insan1)
        print(insan2)

        issiz1 = Issiz("83345035901", "ali", "veli", 38, "e", "turk")
        issiz2 = Issiz("44392672731", "riza", "demir", 23, "e", "turk")
        issiz3 = Issiz("20396378341", "toprak", "fuat", 33, "e", "turk")

        issiz1.yil_degeri_ekle("mavi yaka", 1)
        issiz1.yil_degeri_ekle("beyaz yaka", 10)
        issiz1.yil_degeri_ekle("yonetici", 2)

        issiz2.yil_degeri_ekle("mavi yaka", 1)

        issiz3.yil_degeri_ekle("mavi yaka", 6)
        issiz3.yil_degeri_ekle("beyaz yaka", 1)

        calisan1 = Calisan("12345678901", "ali", "demir", 44, "e", "turk", 30, 12442)
        calisan2 = Calisan("40445674801", "ayse", "kemer", 32, "k", "turk", 70, 24695)
        calisan3 = Calisan("22241078301", "veli", "kul", 25, "e", "turk", 12, 9246)

        maviyaka1 = mavi_yaka("22241078301", "veli", "kul", 25, "e", "turk", 12, 9246)
        maviyaka2 = mavi_yaka("12345678901", "mehmet", "demir", 40, "e", "turk", 50, 19442)
        maviyaka3 = mavi_yaka("83659375027", "ayse", "oz", 46, "k", "turk", 27, 11384)

        beyazyaka1 = beyaz_yaka("40445674801", "ayse", "kemer", 32, "k", "turk", 70, 24695)
        beyazyaka2 = beyaz_yaka("12345678901", "ali", "demir", 44, "e", "turk", 30, 12442)
        beyazyaka3 = beyaz_yaka("92734872832", "yesim", "berra", 33, "k", "turk", 44, 44837)

        data ={
            "calisan1": {
            "tc_no": "12345678901",
            "ad": "ali",
            "soyad": "demir",
            "yas": 44,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 30,
            "maas": 12442
        },
        "calisan2": {
            "tc_no": "40445674801",
            "ad": "ayse",
            "soyad": "kemer",
            "yas": 32,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 70,
            "maas": 24695
        },
        "calisan3": {
            "tc_no": "22241078301",
            "ad": "veli",
            "soyad": "kul",
            "yas": 25,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 12,
            "maas": 9246
        },
        "maviyaka1": {
            "tc_no": "22241078301",
            "ad": "veli",
            "soyad": "kul",
            "yas": 25,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 12,
            "maas": 9246
        },
        "maviyaka2": {
            "tc_no": "12345678901",
            "ad": "mehmet",
            "soyad": "demir",
            "yas": 40,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 50,
            "maas": 19442
        },
        "maviyaka3": {
            "tc_no": "83659375027",
            "ad": "ayse",
            "soyad": "oz",
            "yas": 46,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 27,
            "maas": 11384
        },
        "beyazyaka1": {
            "tc_no": "40445674801",
            "ad": "ayse",
            "soyad": "kemer",
            "yas": 32,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 70,
            "maas": 24695
        },
        "beyazyaka2": {
            "tc_no": "12345678901",
            "ad": "ali",
            "soyad": "demir",
            "yas": 44,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 30,
            "maas": 12442
        },
            "beyazyaka3": {
            "tc_no": "92734872832",
            "ad": "yesim",
            "soyad": "berra",
            "yas": 33,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 18,
            "maas": 13902
        }

    }
        data_list = []
        for key, value in data.items():
            value["kisi_tipi"] = key  # Add a new key-value pair for "kisi_tipi"
            data_list.append(value)

        df = pd.DataFrame(data_list)
        print(df)
          

        issizler = [issiz1, issiz2, issiz3]
        for issiz in issizler:
            issiz.statu_bul()
            print(issiz)

        calisanlar = [calisan1, calisan2, calisan3]
        for calisan in calisanlar:
            calisan.zam_hakki()
            print(calisan.get_yeni_maas())
            print(calisan)

        maviyakalar = [maviyaka1, maviyaka2, maviyaka3]
        for maviyaka in maviyakalar:
            maviyaka.zam_hakki()
            print(maviyaka.get_yeni_maas())
            print(maviyaka)

        beyazyakalar = [beyazyaka1, beyazyaka2, beyazyaka3]
        for beyazyaka in beyazyakalar:
            beyazyaka.zam_hakki()
            print(beyazyaka.get_yeni_maas())
            print(beyazyaka)

    except Exception as e:
        print("An error occurred:", str(e))


main()



