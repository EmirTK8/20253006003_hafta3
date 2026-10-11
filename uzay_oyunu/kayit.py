# Ad Soyad: Emir Talha Karaman
# Öğrenci Numarası: 20253006003
# Tarih: 11.10.2026
#
# Görev 2 – Esnek parametreler (*adimlar, oncelik, **ekler)


def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler) -> str:
    """Görev adımlarını ve ek bilgileri ekrana yazdırır ve metni döndürür.

    'oncelik' parametresi yalnızca adıyla (keyword-only) verilebilir.
    """
    satirlar = [f"[{oncelik.upper()}] {baslik}"]

    for i, adim in enumerate(adimlar, 1):
        satirlar.append(f" {i}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f" {anahtar}: {deger}")

    metin = "\n".join(satirlar)
    print(metin)
    return metin


if __name__ == "__main__":
    # 1. Çağrı: argümanları tek tek vererek çağırma
    print("=== 1. Çağrı: Doğrudan Değerlerle ===")
    gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe",
    )

    # 2. Çağrı: listeyi * ve sözlüğü ** ile açarak çağırma
    print("\n=== 2. Çağrı: *liste ve **sozluk Açarak ===")
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    gorev_kaydi(
        "Kara deliğe atla",
        *adimlar_listesi,
        oncelik="yüksek",
        **ek_bilgiler,
    )
