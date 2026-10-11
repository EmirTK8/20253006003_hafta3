# Ad Soyad: Emir Talha Karaman
# Öğrenci Numarası: 20253006003
# Tarih: 11.10.2026
#
# Fonksiyonların Birim Testleri (Görev 1, Görev 2, Görev 3, Görev 5 & Bonus)

import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


# --- Görev 1 Testleri ---

def test_envanter_metni_dolu():
    """Eşyalar varken beklenen envanter metninin dönmesini test eder."""
    sonuc = envanter_metni(True, False, True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_bos():
    """Hiç eşya yoksa boş metin dönmesini test eder."""
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_tum_esyalar():
    """Tüm eşyalar varken tam liste dönmesini test eder."""
    sonuc = envanter_metni(True, True, True)
    assert sonuc == "Sende: bol kredi, hiper motor, yetenekli bir pilot"


def test_hedef_menusu():
    """Hedeflerin numaralandırılmış liste olarak dönmesini test eder."""
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen


def test_hedef_menusu_tek_hedef():
    """Tek hedef olduğunda düzgün formatlanmasını test eder."""
    beklenen = "Nereye gitmek istersin?\n[1] orion"
    assert hedef_menusu(["orion"]) == beklenen


# --- Görev 2 Testleri ---

def test_gorev_kaydi(capsys):
    """Standart parametrelerle görev kaydı çıktısını test eder."""
    from uzay_oyunu.kayit import gorev_kaydi

    gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe"
    )
    captured = capsys.readouterr()
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        " 1. Kredi kazan\n"
        " 2. Pilot bul\n"
        " 3. Hiperdrive al\n"
        " sorumlu: Ayşe\n"
    )
    assert captured.out == beklenen


def test_gorev_kaydi_unpacking(capsys):
    """* ve ** açarak çağırma biçimini test eder."""
    from uzay_oyunu.kayit import gorev_kaydi

    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler)
    captured = capsys.readouterr()
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        " 1. Kredi kazan\n"
        " 2. Pilot bul\n"
        " 3. Hiperdrive al\n"
        " sorumlu: Ayşe\n"
    )
    assert captured.out == beklenen


# --- Görev 3 Testleri ---

def test_galaksi_kur_varsayilan_yakit():
    """Yakıt verilmediğinde varsayılan 50 olmasını test eder."""
    from uzay_oyunu.galaksi import galaksi_kur

    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["konum"] == "mars"
    assert g["yakit"] == 50


def test_galaksi_kur_gecersiz_baslangic():
    """Geçersiz başlangıç gezegeninde ValueError fırlatılmasını test eder."""
    from uzay_oyunu.galaksi import galaksi_kur

    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "dünya")


def test_veri_yukle():
    """galaksi.json dosyasından verilerin doğru yüklendiğini test eder."""
    from uzay_oyunu.galaksi import veri_yukle

    g = veri_yukle()
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100
    assert "sirius" in g["baglantilar"]
    assert g["baglantilar"]["dünya"] == ["centauri", "sirius"]


# --- Görev 5 & Bonus Testleri ---

def test_hamle_sayaci():
    """Her çağrıda sayacın 1 arttığını ve bağımsız çalıştığını test eder."""
    from uzay_oyunu.araclar import hamle_sayaci

    sayac1 = hamle_sayaci()
    assert sayac1() == 1
    assert sayac1() == 2
    assert sayac1() == 3

    sayac2 = hamle_sayaci()
    assert sayac2() == 1
    assert sayac1() == 4


def test_en_bagli_gezegenler():
    """Gezegenlerin bağlantı sayısına göre sıralandığını test eder."""
    from uzay_oyunu.araclar import en_bagli_gezegenler
    from uzay_oyunu.galaksi import veri_yukle

    g = veri_yukle()
    sirali = en_bagli_gezegenler(g)
    beklenen = ["sirius", "centauri", "dünya", "orion", "kara_delik"]
    assert sirali == beklenen


def test_en_bagli_gezegenler_esitlik():
    """Bağlantı sayısı eşitse alfabetik sıraya bakılmasını test eder."""
    from uzay_oyunu.araclar import en_bagli_gezegenler

    ornek = {
        "baglantilar": {
            "z": ["x"],
            "b": ["x", "y"],
            "a": ["x", "y"],
        }
    }
    assert en_bagli_gezegenler(ornek) == ["a", "b", "z"]


def test_sure_olc(capsys):
    """Süre ölçen dekoratörün çalıştığını test eder."""
    from uzay_oyunu.araclar import sure_olc

    @sure_olc
    def ornek_hesapla(x):
        return x * x

    assert ornek_hesapla(5) == 25
    captured = capsys.readouterr()
    assert "saniye" in captured.out
