from insan import Insan
from issiz import Issiz
from calisan import Calisan
from maviYaka import mavi_yaka


def main():
   
    calisan = Calisan("12345678901", "ali", "demir", 44, "e", "turk", 30, 13442)
    calisan.zam_hakki()  # Zam hesaplama iþlemi
    print(calisan.get_maas())
    print(calisan)
    
    maviyaka = mavi_yaka("12345678901", "mehmet", "demir", 40, "e", "turk", 50, 19442)
    maviyaka.zam_hakki()
    print(maviyaka.get_maas())
    print(maviyaka.get_maas())
    print(maviyaka)

main()


