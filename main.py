from insan import Insan
from issiz import Issiz
from calisan import Calisan


def main():
    calisan = Calisan("12345678901", "ali", "demir", 44, "e", "turk", 30, 12000)
    calisan.zam_hakki()  # Zam hesaplama iþlemi
    print(calisan.get_maas())
    print(calisan)

main()


