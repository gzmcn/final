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

        beyazyaka1 = beyaz_yaka("40445674801", "ayse", "kemer", 32, "k", "turk", 80, 24695)
        beyazyaka2 = beyaz_yaka("12345678901", "ali", "demir", 44, "e", "turk", 30, 12442)
        beyazyaka3 = beyaz_yaka("92734872832", "yesim", "berra", 33, "k", "turk", 44, 44837)

        
        issizler = [issiz1, issiz2, issiz3]
        for issiz in issizler:
            try:
                issiz.statu_bul()
                print(issiz)
            except Exception as e:
                print("An error occurred:", str(e))

        calisanlar = [calisan1, calisan2, calisan3]
        for calisan in calisanlar:
            try:
                calisan.zam_hakki()
                print(calisan.get_yeni_maas())
                print(calisan)
            except Exception as e:
                print("An error occurred:", str(e))

        maviyakalar = [maviyaka1, maviyaka2, maviyaka3]
        for maviyaka in maviyakalar:
            try:
                maviyaka.zam_hakki()
                print(maviyaka.get_yeni_maas())
                print(maviyaka)
            except Exception as e:
                print("An error occurred:", str(e))

        beyazyakalar = [beyazyaka1, beyazyaka2, beyazyaka3]
        for beyazyaka in beyazyakalar:
            try:
                beyazyaka.zam_hakki()
                print(beyazyaka.get_yeni_maas())
                print(beyazyaka)
            except Exception as e:
                print("An error occurred:", str(e))

        data ={
            "calisan1": {
            "tc_no": "12345678901",
            "ad": "ali",
            "soyad": "demir",
            "yas": 44,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 30/12,   # 12'ye bolerek yila ceviriyoruz
            "maas": calisan1.get_maas(),
            "sektor": calisan1.get_sektor(),
            "yeni maas": calisan1.get_yeni_maas()
        },
        "calisan2": {
            "tc_no": "40445674801",
            "ad": "ayse",
            "soyad": "kemer",
            "yas": 32,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 70/12,
            "maas": calisan2.get_maas(),
            "sektor": calisan2.get_sektor(),
            "yeni maas": calisan2.get_yeni_maas()
        },
        "calisan3": {
            "tc_no": "22241078301",
            "ad": "veli",
            "soyad": "kul",
            "yas": 25,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 12/12,
            "maas": calisan3.get_maas(),
            "sektor": calisan3.get_sektor(),
            "yeni maas": calisan3.get_yeni_maas()
        },
        "maviyaka1": {
            "tc_no": "22241078301",
            "ad": "veli",
            "soyad": "kul",
            "yas": 25,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 12/12,
            "maas": maviyaka1.get_maas(),
            "sektor": maviyaka1.get_sektor(),
            "yeni maas": maviyaka1.get_yeni_maas()
        },
        "maviyaka2": {
            "tc_no": "12345678901",
            "ad": "mehmet",
            "soyad": "demir",
            "yas": 40,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 50/12,
            "maas": maviyaka2.get_maas(),
            "sektor": maviyaka2.get_sektor(),
            "yeni maas": maviyaka2.get_yeni_maas()
        },
        "maviyaka3": {
            "tc_no": "83659375027",
            "ad": "ayse",
            "soyad": "oz",
            "yas": 46,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 27/12,
            "maas": maviyaka3.get_maas(),
            "sektor": maviyaka3.get_sektor(),
            "yeni maas": maviyaka3.get_yeni_maas()
        },
        "beyazyaka1": {
            "tc_no": "40445674801",
            "ad": "ayse",
            "soyad": "kemer",
            "yas": 32,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 80/12,
            "maas": beyazyaka1.get_maas(),
            "sektor": beyazyaka1.get_sektor(),
            "yeni maas": beyazyaka1.get_yeni_maas()
        },
        "beyazyaka2": {
            "tc_no": "12345678901",
            "ad": "ali",
            "soyad": "demir",
            "yas": 44,
            "cinsiyet": "e",
            "uyruk": "turk",
            "tecrube": 30/12,
            "maas": beyazyaka2.get_maas(),
            "sektor": beyazyaka2.get_sektor(),
            "yeni maas": beyazyaka2.get_yeni_maas()
        },
            "beyazyaka3": {
            "tc_no": "92734872832",
            "ad": "yesim",
            "soyad": "berra",
            "yas": 33,
            "cinsiyet": "k",
            "uyruk": "turk",
            "tecrube": 18/12,
            "maas": beyazyaka3.get_maas(),
            "sektor": beyazyaka3.get_sektor(),
            "yeni maas": beyazyaka3.get_yeni_maas()
        }

    }
        data_list = []
        for key, value in data.items():
            value["kisi_tipi"] = key  # Add a new key-value pair for "kisi_tipi"
            data_list.append(value)

        df = pd.DataFrame(data_list)
        pd.set_option("display.max_columns", None)
        print(df)

        yuksek_maas = df[df["maas"] > 15000]
        print(yuksek_maas)
          


        # df.rename(columns={'maas': 'yeni_maas'}, inplace=True)
        df_buyukten_kucuge = df.sort_values(by='yeni maas', ascending=False)
        print(df_buyukten_kucuge)

        beyazyaka_df = df[(df['kisi_tipi'].str.contains('beyazyaka')) & (df['tecrube'] > 3)]
        print(beyazyaka_df)

        yeni1_df = df[df["yeni maas"] > 10000]
        sutunlar = ["tc_no", "yeni maas"]
        cikti_df = yeni1_df[sutunlar].iloc[1:5]
        print(cikti_df)

        yeni_df = df[["ad", "soyad", "sektor", "yeni maas"]]
        print(yeni_df)

    except Exception as e:
        print("An error occurred:", str(e))

    except AssertionError as ae:
        print("Assertion Error:", str(ae))

    except ValueError as ve:
        print("Value Error:", str(ve))


main()



