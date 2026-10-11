# Ad Soyad: Emir Talha Karaman
# Öğrenci Numarası: 20253006003
# Tarih: 11.10.2026
#
# Görev 5 – Closure ve lambda
# Bonus – Süre ölçen sarmalayıcı (decorator)

import time
from typing import Any, Callable


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında 1 artıran sayaç fonksiyonu (closure)."""
    sayac = 0

    def arttir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return arttir


def en_bagli_gezegenler(galaksi: dict) -> list:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    baglantilar = galaksi["baglantilar"]
    return sorted(baglantilar.keys(), key=lambda p: (-len(baglantilar[p]), p))


def sure_olc(fonksiyon: Callable) -> Callable:
    """Fonksiyonun çalışma süresini ölçen sarmalayıcı (decorator)."""
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    try:
        from uzay_oyunu.galaksi import veri_yukle
    except ModuleNotFoundError:
        from galaksi import veri_yukle

    g = veri_yukle()
    print("En bağlı gezegenler:", en_bagli_gezegenler(g))

    # Bonus: Süre ölçüm testi
    olculen = sure_olc(en_bagli_gezegenler)
    print("Süre ölçümlü sonuç:", olculen(g))
